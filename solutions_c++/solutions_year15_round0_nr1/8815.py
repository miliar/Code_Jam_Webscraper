#include<bits/stdc++.h>
#define chtoi(a) ((int)a-'0')
using namespace std;
int main()
{
	freopen("E://A-large.in","r",stdin);
	freopen("E://t1.txt","w",stdout);
	int cnt=0,sum=0;
	int t,max,x=0;
	char S[1005];
	scanf("%d",&t);
	while(t--)
	{
		scanf("%d %s",&max,S);
		cnt=sum=0;
		for(int i=0;i<max+1;i++)
		{
			if(sum<=i)
			{
				cnt+=(i-sum);
				sum+=(i-sum);
			}
			sum+=chtoi(S[i]);
		}
		x++;
		printf("Case #%d: %d\n",x,cnt);
	}
	return 0;
}
