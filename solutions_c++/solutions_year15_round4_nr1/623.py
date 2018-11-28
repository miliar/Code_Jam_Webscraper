#include<bits/stdc++.h>
#include<iostream>
using namespace std;
#define fre 	freopen("0.in","r",stdin),freopen("0.out","w",stdout)
#define abs(x) ((x)>0?(x):-(x))
#define MOD 1000000007
#define lld signed long long int
#define pp pop_back()
#define ps(x) push_back(x)
#define mpa make_pair
#define pii pair<int,int>
#define fi first
#define se second
#define scan(x) scanf("%d",&x)
#define print(x) printf("%d\n",x)
#define scanll(x) scanf("%lld",&x)
#define printll(x) printf("%lld\n",x)
#define boost ios_base::sync_with_stdio(0)
//vector<int> g[2*100000+5];int par[2*100000+5];
double V,X;
double v[6654],c[6464];
int main()
{
	fre;
	int N,T;
	cin >> T;
	for(int t=1;t<=T;++t)
	{
		cin>>N>>V>>X;
		for(int i=1;i<=N;++i)
		{
			cin>>v[i]>>c[i];
		}
		double time=0;
		if(N==1)
		{
			time = V/v[1];
			if(X!=c[1])
				time = -1;
		}
		else
			if(N==2 and c[1]==c[2])
		{
			v[1]+=v[2];
			time = V/v[1];
			if(X!=c[1])
				time = -1;
		}
		else
		{
			double t1 = (V/v[1])*(X-c[2])/(c[1]-c[2]);
			double t2 = (V/v[2])*(c[1]-X)/(c[1]-c[2]);
			time = max(t1,t2);
			if(t1<0 or t2<0)
				time=-1;
		}
		if(time<0)
		{
			printf("Case #%d: IMPOSSIBLE\n",t);
		}
		else
		{
			printf("Case #%d: %0.6f\n",t,time);
		}
	}
}
