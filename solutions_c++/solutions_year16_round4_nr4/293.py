#define _CRT_SECURE_NO_WARNINGS

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
#include <fstream>
#include <queue>
#include <cstring>
#include <string>
#include <complex>
#include <unordered_map>
#include <valarray>

#define vi vector<int>
#define vpii vector< pair<int,int> >
#define pii pair<int,int>
#define mp(x,y) make_pair(x,y)
#define all(x) (x).begin(),(x).end()
#define FOREACH(it,x) for (auto it = (x).begin(); it!=(x).end(); ++it) 
#define sz(x) (int)(x).size()
#define FOR(i,n) for (ll i = 0; i < ll(n); i++)
#define ROF(i,n) for (ll i = ((ll)n-1); i >= 0; i--)
#define FOR1(i,n) for (ll i = 1; i < ll(n); i++)
#define REP(i,a,b) for (ll i = a; i < ll(b); i++)
#define READ(a) int a; scanf("%d", &a);
#define READV(v,n) vi v(n);FOR(i,n){scanf("%d", &v[i]);}
#define WRITE(v) FOR(i,sz(v))cout<<v[i]<<" ";
#define gmin(a,b) { if (b < a) a = b; }
#define gmax(a,b) { if (b > a) a = b; }
#define pb push_back
#define ff first
#define ss second
#define oo ((1LL<<62)+((1LL<<31)-1))
#define MOD 1000000007ll
const double PI = std::atan(1.0)*4;

typedef long long ll;
typedef unsigned long long ull;
using namespace std;

bool check(vector<vi> &m){
	FOR(p,sz(m)){
		vi perm;
		FOR(i, sz(m)) perm.pb(i);

		do{
			vi filled(sz(m), 0);
			FOR(i, sz(m)) if(m[p][i]==0) filled[i]=1;
			FOR(i, sz(m)){
				int p2 = perm[i];
				if(p2 == p) continue;
				FOR(j, sz(filled)){
					if(filled[j]==0 && m[p2][j]==1){
						filled[j]=1;
						break;
					}
				}
			}
			FOR(i, sz(m)){
				if(filled[i]==0) goto nextperm;
			}
			return false;
			nextperm: continue;
		}while(next_permutation(all(perm)));
	}
	return true;
}

int main(int argc, char *argv[]){
	READ(T);
	FOR(t,T){
		READ(n);
		vector<vi> m(n, vi(n));
		FOR(i,n){
			FOR(j,n){
				char c;
				cin>>c;
				m[i][j]=c-'0';
			}
		}
		int res = oo;
		FOR(mask, 1<<(n*n)){
			auto m2 = m;
			int c = 0;
			FOR(i, n){
				FOR(j,n){
					int b = (mask>>((i*n)+j)) & 1;
					if(b && m[i][j]) goto nextmask;
					if(b){
						m2[i][j] = 1;
						c++;
					}
				}
			}
			/*cerr<<mask<<","<<c<<endl;
			FOR(i,n) FOR(j, n) cerr<<m2[i][j]<<",";cerr<<endl;
			*/
			if(check(m2)) gmin(res, c);
			nextmask: continue;
		}

		cout<<"Case #"<<(t+1)<<": "<<res<<endl;
		next: continue;
	}
	return 0;
}