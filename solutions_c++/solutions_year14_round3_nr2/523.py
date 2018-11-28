#include <fstream>
#include <iostream>
#include <vector>
#include <bitset>
#include <string.h>
#include <algorithm>
#include <iomanip>
#include <math.h>
#include <time.h>
#include <stdlib.h>
#include <set>
#include <map>
#include <string>
#include <queue>
#include <deque>

using namespace std;

const char infile[] = "input.in";
const char outfile[] = "output.out";

ifstream fin(infile);
ofstream fout(outfile);

const int MAXN = 105;
const int oo = 0x3f3f3f3f;
const int MOD = 1000000007;

typedef vector<int> Graph[MAXN];
typedef vector<int> :: iterator It;

const inline int min(const int &a, const int &b) { if( a > b ) return b;   return a; }
const inline int max(const int &a, const int &b) { if( a < b ) return b;   return a; }
const inline void Get_min(int &a, const int b)    { if( a > b ) a = b; }
const inline void Get_max(int &a, const int b)    { if( a < b ) a = b; }

int N, t;
string s[MAXN];
int G[MAXN][MAXN] , Ans[MAXN][MAXN], aux[MAXN][MAXN];
/*
inline void Multiply(int A[MAXN][MAXN], int B[MAXN][MAXN], int C[MAXN][MAXN]) {
    for(int i = 0 ; i < N ; ++ i)
        for(int j = 0 ; j < N ; ++ j)
            for(int k = 0 ; k < N ; ++ k)
                C[i][j] = (C[i][j] + 1LL * A[i][k] * B[k][j]) % MOD;
}

inline void lgPow(int P) {
    memset(Ans, 0, sizeof(Ans));
    for(int i = 0 ; i < N ; ++ i)
        Ans[i][i] = 1;
    for( ; P ; P >>= 1) {
        if(P & 1) {
            memset(aux, 0, sizeof(aux));
            Multiply(Ans, G, aux);
            memcpy(Ans, aux, sizeof(aux));
        }
        memset(aux, 0, sizeof(aux));
        Multiply(G, G, aux);
        memcpy(G, aux, sizeof(aux));
    }
}*/

int st[MAXN];
bitset <MAXN> was;
bitset <MAXN> Used;

inline bool validate() {
    was.reset();
    string stt;
    //cerr << '\n';
    for(int i = 0; i < N ; ++ i)
        stt += s[st[i]];
    //cerr << stt << '\n';
    for(int j = 0 ; j < stt.size() ; ++ j) {
        if(was[stt[j] - 'a']) {
            //cerr << "0\n";
            return false;
        }
        while(j + 1 < stt.size() && stt[j] == stt[j + 1])
            ++ j;
        was[stt[j] - 'a'] = 1;
    }
    //cerr << "1\n";
    return true;
}

int ans;

inline void Back(int k) {
    if(k == N) {
        ans = (ans + validate()) % MOD;
        return;
    }
    for(int i = 0 ; i < N ; ++ i)
        if(!Used[i]) {
            Used[i] = 1;
            st[k] = i;
            Back(k + 1);
            Used[i] = 0;
        }
}

int main() {
    cin.sync_with_stdio(false);
    #ifndef ONLINE_JUDGE
    freopen(infile, "r", stdin);
    freopen(outfile, "w", stdout);
    #endif
    cin >> t;
    for(int test = 1 ; test <= t ; ++ test) {
        cin >> N;
        for(int i = 0 ; i < N ; ++ i)
            cin >> s[i];
        /*for(int i = 0 ; i < N ; ++ i) {
            for(int j = 0 ; j < N ; ++ j) {
                if(i != j && s[i][s[i].size() - 1] == s[j][0])
                    G[i][j] = 1;
                    else G[i][j] = 0;
            }
        }
        lgPow(N - 1);
        int ans = 0;
        for(int i = 0 ; i < N ; ++ i, cerr <<'\n')
            for(int j = 0 ; j < N ; ++ j)
                ans = (1LL * ans + 1LL * Ans[i][j]) % MOD, cerr << Ans[i][j] << ' ';
        */
        ans = 0;
        Used.reset();
        Back(0);
        cout << "Case #" << test << ": " << ans << '\n';
    }
    fin.close();
    fout.close();
    return 0;
}
