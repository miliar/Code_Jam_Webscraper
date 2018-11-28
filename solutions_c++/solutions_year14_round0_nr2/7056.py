#include<cstdio>
#include<iostream>
#include<algorithm>
#include<cmath>
#include<cstdlib>
#include<queue>
#include<map>
#include<set>
#include<string>
#include<sstream>
#include<climits>
#include<vector>
#include<cstring>
#include<stack>

using namespace std;

#define all(c) (c).begin(),(c).end()
#define vi vector<int>
#define vvii vector< vi >
#define REP(i,s,n)  for (int i=(s),_n=(n);i<=_n;i++)
#define FOR(i,s,n)  for (int i=(s),_n=(n);i<_n;i++)
#define REPD(i,e,s)  for (int i=(e),_s=(s);i>=_s;i--)
#define tr(container, it) \
	for (typeof(container.begin()) it=container.begin(); it!=container.end();it++)
#define ALL(x) x.begin(),x.end()
#define debug(args...)	{dbg,args; cerr<<endl;}
#define PB push_back
#define MP make_pair
#define EPS 1e-8
#define INF (int)(1e9)
typedef long long LL;

struct debugger {
	template<typename T> debugger& operator , (const T& v) {	
		cerr<<v<<" ";	
		return *this;	
	}
} dbg;


int main() {
	int T,ind=1;
	cin >> T;
	while(T--)
	{
		double C , F , X;
		double rate=2.0,time=0;
		cin >> C >> F >> X;
		while((X*10000000)/(rate) > (C*10000000/(rate))+(X*10000000/(rate+F)))
		{
			time+=(C*10000000.0/rate);
			rate+=F*1.0;
		}
		time+=(X*10000000.0)/(rate);
		printf("Case #%d: %.7lf\n",ind,time/10000000);


		ind++;

	}
	return 0;
}

