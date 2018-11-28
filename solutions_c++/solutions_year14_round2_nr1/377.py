#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <queue>
#include <string>
#include <cstring>

using namespace std;

#define FOR(i,a,b)   	for(int (i)=(a);(i)<(b);(i)++)
#define PB           	push_back
#define INF          	(1 << 29)
#define DEBUG(___x)     cout<<#___x<<" = ["<<___x<<"]"<<endl
#define SORT(___a)      sort(___a.begin(),___a.end())
#define RSORT(___a)     sort(___a.rbegin(),___a.rend())
#define PI           	3.141592653589793238
#define MP           	make_pair
#define PII          	pair<int,int>
#define ALL(___v)       (___v).begin(), (___v).end()
#define VS           	vector<string>
#define VI           	vector<int>
#define S            	size()
#define B				begin()
#define E				end()
#define print(___v)     {cout<<"[";if(___v.S)cout<<___v[0];FOR(___i,1,___v.S)cout<<","<<___v[___i];cout<<"]\n";}
#define clr(___x, ___v)	memset(___x, ___v , sizeof ___x);
#define tr(container, it) for(typeof(container.begin()) it = container.begin(); it != container.end(); it++)


int tu(int val) {return (1 << val);}
bool iset(int mask, int id) {if((mask & tu(id) ) != 0)return true;return false;}
void doset(int &mask, int id) {mask |= tu(id);}
void dounset(int &mask, int id) {mask = mask & (~tu(id));}

typedef long long 					bint;
template<typename T> string tos( T a ) 	{ stringstream ss; string ret; ss << a; ss >> ret; return ret;}

string compress(string word) {
    int l = word.S;
    string ret = "" + tos(word[0]);
    for(int i = 1; i < l; i++) {
        if(word[i] != word[i-1]) {
            ret += tos(word[i]);
        }
    }
    return ret;
}

VI calc(string par) {
    int l = par.S, cnt = 0;
    VI ret;
    
    for(int i = 0; i < l; ) {
        cnt = 0;
        int id = i;
        while(i < l && par[i] == par[id]) {
            i++;
            cnt++;
        }
        
        ret.PB(cnt);
    }
    return ret;
}

int N, cum[200];
string ins[200];
VI vals[200];

int main() {


	freopen("A-large.in", "r", stdin);
	freopen("A_large_out.txt", "w", stdout);
	
	int T;
	cin >> T;
	FOR(t,0,T) {

        clr(cum, 0);
                
        cin >> N;
        FOR(i,0,N) {
            cin >> ins[i];
        }
        
        printf("Case #%d: ", t+1);
        
        bool ok = true;
        string st = compress(ins[0]);
        FOR(i,1,N) {
            string nt = compress(ins[i]);
            if(st != nt) {
                ok = false;
                break;
            }
        }
        if(!ok) {
            printf("Fegla Won\n");
            continue;
        }
        
        int res = 0;
        FOR(i,0,N) {
            vals[i] = calc(ins[i]);
        }
        int la = vals[0].S;
        FOR(i,0,la) {
            
            FOR(j,0,N) {
                cum[i] += vals[j][i];
            }
        }
        
        FOR(i,0,la) {
            
            set<int> iset;
            VI arr;
            FOR(j,0,N) {
                int val = vals[j][i];
                if(iset.count(val))continue;
                
                arr.PB(val);
                iset.insert(val);
            }
            //print(arr);
            int cres = INF;
            int la = arr.S;
            FOR(j,0,la) {
                int cst = 0;
                FOR(k,0,N) {
                    cst += abs(arr[j] - vals[k][i]);
                }
                cres = min(cres, cst);
            }
            //DEBUG(cum[i]);
            res += cres;
        }
        
        printf("%d\n", res);
	}

	return 0;
}

