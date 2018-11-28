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

#define vi vector<int>
#define vpii vector< pair<int,int> >
#define pii pair<int,int>
#define mp(x,y) make_pair(x,y)
#define all(x) (x).begin(),(x).end()
#define FOREACH(it,x) for (auto it = (x).begin(); it!=(x).end(); ++it) 
#define sz(x) (int)(x).size()
#define FOR(i,n) for (ll i = 0; i < ll(n); i++)
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
const double PI = std::atan(1.0)*4;

typedef long long ll;
typedef unsigned long long ull;
using namespace std;

int n;
double v,x;
vector<double> r,c;

int main(){
    READ(T);
	FOR(t,T){
		
		cin>>n>>v>>x;
		r = vector<double>(n);
		c = vector<double>(n);
		FOR(i,n){
			cin>>r[i]>>c[i];
		}
		double minc = 100, maxc = 0;
		FOR(i,n){
			gmax(maxc, c[i]);
			gmin(minc, c[i]);
		}
		double xsumc = x * v;

		if(x<minc || x>maxc){
			cout<<std::setprecision(9)<<"Case #"<<(t+1)<<": "<<"IMPOSSIBLE"<<endl; 
			continue;
		}

		if(n==1){
			double res = v / r[0];
			cout<<std::setprecision(20)<<"Case #"<<(t+1)<<": "<<res<<endl; 
			continue;
		}else if(n==2){
			if(c[0]==c[1]) r[0]+=r[1];
			if(c[0]>c[1]){
				swap(c[0], c[1]);
				swap(r[0],r[1]);
			}
			if(x==c[0]){
				double res = v / r[0];
				cout<<std::setprecision(20)<<"Case #"<<(t+1)<<": "<<res<<endl; 
				continue;
			}else if(x==c[1]){
				double res = v / r[1];
				cout<<std::setprecision(20)<<"Case #"<<(t+1)<<": "<<res<<endl; 
				continue;
			}else{
				double rat = (x-c[0])/(c[1]-c[0]);
				//cerr<<rat<<endl;
				double res = 0;
				gmax(res, (1-rat) * v / r[0]);
				gmax(res, rat * v / r[1]);
				cout<<std::setprecision(20)<<"Case #"<<(t+1)<<": "<<res<<endl; 
				continue;
			}
		}
		
		//cout<<"Case #"<<(t+1)<<": "<<"IMPOSSIBLE"<<endl; 
	}

    return 0;
}
