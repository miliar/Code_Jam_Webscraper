#include<bits/stdc++.h>
using namespace std;

#define MAX 1000000
#define MOD 1000000007
#define F first
#define S second
#define PB push_back
#define MP make_pair
#define V vector
#define I int
#define D double
#define B bool
#define pii pair<int,int>
#define LL long long

#define in(x) scanf("%d",&x)
#define in2(x,y) scanf("%d%d",&x,&y)
#define lin(x) scanf("%lld",&x)
#define lin2(x,y) scanf("%lld%lld",&x,&y)
#define FOR(i,a,b) for(i=a;i<b;i++)

/*
I p[MAX]={1,1,0};
I prime[MAX/10]={2};
void sieve()
{
	I i,j,k=1;
	for(i=3;i*i<=MAX;i+=2)
	{
		if(p[i])
			continue;
		for(j=i*i;j<MAX;j+=2*i)
			p[j]=1;
	}
	FOR(i,3,MAX)
	{
		if(!p[i])
			p[k++]=i;
	}
	return;
}

I gcd(I a,I b)
{
	if(!b)
		return a;
	return gcd(b,a%b);
}

LL power(LL a,LL b,LL m){
	if(!b)
		return 1;
	LL h=power(a,b/2,m)%m;
	if(b&1)
		return (((h*h)%m)*a)%m;
	else
		return (h*h)%m;
}
*/

I main()
{
	I t,i,j,k;
	cin>>t;
	FOR(k,1,t+1){
		I n;cin>>n;
		string s;cin>>s;
		j=0;
		I c=0;
		FOR(i,0,s.length()){
			if(i-j>0){
				c+=(i-j);
				j+=(i-j);
			}
			j+=(s[i]-'0');
		}
		cout<<"Case #"<<k<<": "<<c<<endl;
	}
	return 0;
}
