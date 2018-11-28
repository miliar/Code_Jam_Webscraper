#include<bits/stdc++.h>
using namespace std;
#define maxi 1005

int main() {
	int t,n,k,ans;
	char a[maxi];
	scanf("%d",&t);
	for(int j=1;j<=t;j++)
	{
		scanf("%d %s",&n,a);
		ans=0;
		k=(a[0]-'0');
		for(int i=1;i<=n;i++)
		{
			if((a[i]-'0')!=0)
			{
				if(k<i)
				{
					ans+=(i-k);
					k+=ans;
				}
			}
			k+=(a[i]-'0');
		}
		printf("Case #%d: %d\n",j,ans);
	}
 return 0;
}

