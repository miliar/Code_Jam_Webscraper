#include<bits/stdc++.h>
using namespace std;

//#pragma comment (linker, "/STACK:256000000")

typedef long long ll ;
typedef vector<ll> VI ;
typedef pair<ll,ll>  PP;
typedef vector<PP>  VPP ;

#define endl '\n'
#define  MP make_pair
#define PB push_back
#define F first
#define S second
#define sz(x) ((int)(x).size())
#define forn(i,n) for(int i=0;i<n;i++)
#define fileio 
#define boost  ios_base::sync_with_stdio(false);cin.tie(0);
#define trace1(x)                cerr << #x << ": " << x << endl;
#define trace2(x, y)             cerr << #x << ": " << x << " | " << #y << ": " << y << endl;
#define trace3(x, y, z)          cerr << #x << ": " << x << " | " << #y << ": " << y << " | " << #z << ": " << z << endl;

ll mod = 1e9 + 7 ;
ll powmod(ll a,ll b) {ll res=1;a%=mod;for(;b;b>>=1){if(b&1)res=res*a%mod;a=a*a%mod;}return res;}
ll gcd(ll a , ll b){return b==0?a:gcd(b,a%b); }

/*---------------------------------------------------------------------------------------------------------------------------------------------------------------*/
/*                                                              SNIPPETS DONE
/*---------------------------------------------------------------------------------------------------------------------------------------------------------------*/


double V,X;
double v[6700],c[6700];
int main()
{
	freopen("in.txt","r",stdin); freopen("out.txt","w",stdout);
	
	int N,T;
	cin >> T;
	double t1 , t2 ;
	int t;
	
	for(t=1;t<=T;++t)
	{
		cin>>N>>V>>X;
		for(int i=1;i<=N;++i)
		{
			cin>>v[i]>>c[i];
		}
		double tim=0;
		if(N==1)
		{
			tim = V/v[1];
			if(X!=c[1])
				tim = -1;
		}
		else
			if(N==2 and c[1]==c[2])
		{
			v[1]+=v[2];
			tim = V/v[1];
			if(X!=c[1])
				tim = -1;
		}
		else
		{
			 t1 = (V/v[1])*(X-c[2])/(c[1]-c[2]);
			 t2 = (V/v[2])*(c[1]-X)/(c[1]-c[2]);
			tim = max(t1,t2);
			if(t1<0 or t2<0)
				tim=-1;
		}
		//cout << tim <<endl;
		
		if(tim<0)
		{
			printf("Case #%d: IMPOSSIBLE\n",t);
		}
		else
		{
			printf("Case #%d: %0.8f\n",t,tim);
		}
	}
}

