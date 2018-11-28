#include <algorithm>
#include <functional>
#include <numeric>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <cassert>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <bitset>
#include <sstream>

using namespace std;

#define forn(i, n) for(int i = 0; i < int(n); ++i)
#define for1(i, n) for(int i = 1; i <= int(n); ++i)
#define ford(i, n) for(int i = int(n) - 1; i >= 0; --i)
#define fore(i, l, r) for(int i = int(l); i < int(r); ++i)
#define sz(v) int((v).size())
#define all(v) (v).begin(), (v).end()
#define pb push_back
#define X first
#define Y second

typedef long long li;
typedef long double ld;
typedef pair<int, int> pt;

template<typename T> T abs(T a) { return a < 0 ? -a : a; }
template<typename T> T sqr(T a) { return a*a; }

const int INF = (int)1e9;
const ld EPS = 1e-9;
const ld PI = 3.1415926535897932384626433832795;

const int H = 3;
const int N = 20;
int A[H];
int M[H];
int mul[H][N];

struct hash{
    int h[H];
    
    hash(){ memset(h, 0, sizeof(int) * H); }

    bool operator < (const hash& c) const{
        forn(i, H)
            if(h[i] != c.h[i])
                return h[i] < c.h[i];
        return false;
    }
    
    bool operator == (const hash& c) const{
        forn(i, H)
            if(h[i] != c.h[i])
                return false;
        return true;
    }
};

inline bool isPrime(int a){
    for(int i = 2; i*i <= a; ++i)
        if(a % i == 0)
            return false;
    return true;
}

set<hash> dic[N];

#include <fstream>
void readDic(){
    cerr << "Starting dic reading" << endl;

    ifstream in("dic.txt");
    string s;
    while(in >> s){
        hash cur;
        forn(i, sz(s))
            forn(j, H)
                cur.h[j] = (cur.h[j] + mul[j][i] * 1ll * s[i]) % M[j];
                
        dic[sz(s)].insert(cur);
    }

    in.close();
    
    cerr << "Dic read in " << clock() << endl;
}

int n;
string s;
int z[6][4010];

int solve(int, int);

int solve(int last, int idx){
    if(idx == n)
        return 0;
    if(z[last][idx] == -1){
        int& res = z[last][idx];
        res = INF;

        for(int ln = 1; ln <= 10 && idx + ln <= n; ++ln){
            hash cur;
            for(int i = idx; i < idx + ln; ++i)
                forn(j, H)
                    cur.h[j] = (cur.h[j] + mul[j][i - idx] * 1ll * s[i]) % M[j];
                    
            {
                if(dic[ln].count(cur)){
                    res = min(res, solve(min(5, last + ln), idx + ln));
                    continue;
                }
            }
                    
            int maxD = idx + ln;
            
            {
                for(int p1 = idx; p1 < idx + ln; ++p1){
                    if(last + p1 - idx < 5)
                        continue;

                    for(int c = 'a'; c <= 'z'; ++c){
                        if(c == s[p1])
                            continue;
                        hash nc(cur);
                        
                        forn(j, H){
                            nc.h[j] = (nc.h[j] + mul[j][p1 - idx] * 1ll * (c - s[p1])) % M[j];
                            if(nc.h[j] < 0)
                                nc.h[j] += M[j];
                        }
                            
                        if(dic[ln].count(nc)){  
                            res = min(res, solve(min(5, idx + ln - p1), idx + ln) + 1);
                            maxD = p1;
                            break;
                        }
                    }
                    
                    if(maxD != idx + ln)
                        break;
                }
            }
            
            {
                bool found = false;
                for(int p1 = idx; p1 < maxD; ++p1){
                    for(int p2 = p1 + 1; p2 < maxD; ++p2){
                        if(last + p1 - idx < 5 || p2 - p1 < 5 || found)
                            continue;
                            
                        for(int c1 = 'a'; c1 <= 'z'; ++c1){
                            if(s[p1] == c1)
                                continue;
                            for(int c2 = 'a'; c2 <= 'z'; ++c2){
                                if(s[p2] == c2)
                                    continue;
                                    
                                hash nc(cur);
                                forn(j, H){
                                    nc.h[j] = (nc.h[j] + mul[j][p1 - idx] * 1ll * (c1 - s[p1])) % M[j];
                                    if(nc.h[j] < 0)
                                        nc.h[j] += M[j];

                                    nc.h[j] = (nc.h[j] + mul[j][p2 - idx] * 1ll * (c2 - s[p2])) % M[j];
                                    if(nc.h[j] < 0)
                                        nc.h[j] += M[j];
                                }
                                
                                if(dic[ln].count(nc)){
                                    res = min(res, solve(min(5, idx + ln - p2), idx + ln) + 2);
                                    found = true;
                                    break;
                                }
                            }
                            if(found)
                                break;
                        }
                        if(found)
                            break;
                    }
                    if(found)
                        break;
                }
            }
        }
    }
    
    return z[last][idx];
}

int main(){
    #ifdef ssu1
        freopen("input.txt", "rt", stdin);
        //freopen("output.txt", "wt", stdout);
    #endif

    {
        int cnt = 0;
        for(int i = 1000000000; cnt < H; ++i)
            if(isPrime(i))
                M[cnt++] = i;
                
        cnt = 0;
        for(int i = 1000; cnt < H; ++i)
            if(isPrime(i))
                A[cnt++] = i;
                
        forn(i, H){
            mul[i][0] = 1;
            for(int j = 1; j < N; ++j)
                mul[i][j] = (mul[i][j - 1] * 1ll * A[i]) % M[i];
        }
    }
    
    readDic();

    forn(i, 11)
        cerr << i << " " << sz(dic[i]) << endl;
    
    int tests;
    cin >> tests;

    forn(test, tests){
        int start = clock();
        
        printf("Case #%d: ", test + 1);
        
        cin >> s;
        n = sz(s);
        memset(z, -1, sizeof(z));
        
        cout << solve(5, 0) << endl;
        fprintf(stderr, "Case #%d solved in %d\n", test + 1, clock() - start);
    } 
    
    return 0;
}
