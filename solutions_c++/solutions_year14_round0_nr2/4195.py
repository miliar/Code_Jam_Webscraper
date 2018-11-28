#include<bits/stdc++.h>

using namespace std;
#define CLR(a,val) memset(a, val, sizeof(a))
#define SZ(V) (LL)V.size()
#define ALL(V) V.begin(),V.end()
#define RALL(V) V.rbegin(),V.rend()
#define FORN(i, n) for(LL i = 0; i < n; i++)
#define FORAB(i, a, b) for(LL i = a; i <= b; i++)
#define MOD 1000000007LL
#define PB push_back
#define MP make_pair
#define F first
#define S second

typedef long long LL;
typedef pair<LL,LL> pll;


int main()
{
	LL test;
	cin >> test;
	FORAB(tc,1LL,test){
		double c,f,x;
		cin >> c >> f >> x;
		double t=0.0,ct=0.0,result=x/(2.0+ct);
		while(true){
			t+=c/(2.0+ct);
			ct+=f;
			double ans= t + x/(2.0+ct);
			if(ans>result) break;
			result=ans;
		}
		printf("Case #%lld: %.7lf\n",tc,result );
	}
	return 0;
}