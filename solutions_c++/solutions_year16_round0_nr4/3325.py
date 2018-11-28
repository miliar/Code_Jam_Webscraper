#include <bits/stdc++.h>
using namespace std;

#define FOR(i,j,n) for(i=j;i<n;i++)
#define si(i) scanf("%d",&i)
#define sli(i) scanf("%ld",&i)
#define slli(i) scanf("%lld",&i)
#define sc(i) scanf("%c",&i)
#define ss(i) scanf("%s",i);

#define pi(i) printf("%d\n",i)
#define pli(i) printf("%ld\n",i)
#define plli(i) printf("%lld\n",i)
#define pc(i) printf("%c\n",i)
#define ps(i) printf("%s\n",i);

typedef long long int lli;

void solve()
{
	//print the answer and nothing less or more. 
	lli k,c,s;
	slli(k);
	slli(c);
	slli(s);	
	lli power=1,i;
	FOR(i,0,c-1)
	{
		power=power*k;
	}
	for(i=1;i<=(power*k);i=i+power)
	{
		printf("%lld ",i);
	}

}

int main()
{
	lli i,t;
	cin>>t;
	for(i=1;i<=t;i++)
	{
		cout<<"Case #"<<i<<": ";
		solve();
		cout<<endl; 	
	}
	   
    return 0;
}