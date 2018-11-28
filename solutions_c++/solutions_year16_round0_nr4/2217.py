#include<bits/stdc++.h>
using namespace std;

typedef unsigned long long ll;
int T,n,m,c,s,k;
ll z[111];

int main()
{
	freopen("D.in","r",stdin);
	freopen("D.out","w",stdout);
	
	int p=0;
	scanf("%d",&T);
	for(;T;T--)	
	{
		printf("Case #%d:",++p);
		
		scanf("%d%d%d",&k,&c,&s);
		for(int i=1;i<=k;i++)		
		{
			ll t=i;
			for(int j=1;j<=c-1;j++)t=(t-1)*k+i;
			
			cout<< " " << t;
		}
		cout<<endl;
		
	}
	
	return 0;
}
