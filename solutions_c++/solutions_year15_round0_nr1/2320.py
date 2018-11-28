#include<iostream>
#include<cstdlib>
#include<cstring>
#include<cstdio>
#include<algorithm>
using namespace std;

char d[1010];
int main()
{
//	freopen("a.in","r",stdin);
//	freopen("a.out","w",stdout);
	int T,n ;
	scanf("%d",&T);
	for(int tcase=1;tcase<=T;tcase++)
	{
		scanf("%d %s\n",&n,d);
		int sum=d[0]-'0',ans=0;
		for(int i=1;i<=n;i++)
		{
			d[i]-='0';
			if(sum<i){ans+=i-sum;sum=i;} 
			sum+=d[i];
		}
		printf("Case #%d: %d\n",tcase,ans);
	}
	return 0;
}

