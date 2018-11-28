#include<bits/stdc++.h>
#define ll long long
using namespace std;
int mark[10];
void solve(ll n)
{
	while(n)
	{
		mark[n%10]=1;
		n=n/10;
	}
}
int main()
{
	int t;
	scanf("%d",&t);
	for(int c=1;c<=t;c++)
	{
		int n;
		scanf("%d",&n);
		printf("Case #%d: ",c);
		if(n==0)
		{
			cout<<"INSOMNIA\n";
			continue;
		}
		for(int i=0;i<10;i++) mark[i]=0;
		ll s=n;
		for(int i=2;;i++)
		{	
			solve(s);
			int f=0;
			for(int j=0;j<10;j++) if(mark[j]==0) f=1;
			if(f==0) break;
			s=1ll*i*n;
		}
		cout<<s<<endl;
	}
return 0;
}
