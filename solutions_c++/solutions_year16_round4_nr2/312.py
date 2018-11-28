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

int main(int argc, char *argv[]){
	READ(T);
	FOR(t,T){
		READ(n);
		READ(k);
		vector<double> v(n);
		FOR(i,n) cin>>v[i];
		sort(all(v));
		double res = -1;
		int bestmask = -1;
		
		FOR(i,k+1){
			
			vector<double> m(n+1,0);
			m[0]=1;
			FOR(r, n){
				bool b = false;
				if(r<i) b = true; 
				if(r>=i+n-k) b=true;
				
				if(!b) continue;
				vector<double> m2(n+1,0);
				FOR(j, sz(m)){
					double p = m[j];
					if(p==0) continue;
					m2[j] += (1.0-v[r])*p;
					m2[j+1] += (v[r])*p;
				}
				m = m2;
			}
			if(m[k/2]>res){
				res = m[k/2];
			}
		}
		//cout<<bestmask<<endl;
		//FOR(i, n) cout<<((bestmask>>i) & 1); cout<<endl;
		//FOR(i, n) cout<<v[i]<<" "; cout<<endl;
		//while(bestmask){cout<<(bestmask&1); bestmask>>1;}cout<<endl;
		cout<<setprecision(12)<<"Case #"<<(t+1)<<": "<<res<<endl;
		next: continue;
	}
	return 0;
}