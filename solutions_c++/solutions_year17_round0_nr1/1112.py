#include <bits/stdc++.h>

#define INF 2123123123

using namespace std;

int t,k,cnt,l,dp[1005][1005],flipped[1005];
char state[1005];
bool can;

int main()
{
	scanf("%d",&t);
	for(int p=1;p<=t;p++)
	{
		scanf("%s",state);
		scanf("%d",&k);
		cnt=0;
		l = strlen(state);
	//	printf("length %d, state %s",l,state);
		for(int i=0;i<=l-k;i++)
		{
			if(state[i] == '-')
			{
				cnt++;
				for(int j=i;j<i+k;j++)
					if(state[j]=='-')
						state[j]='+';
					else state[j] ='-';
			}
		}
		can=true;
		for(int i=0;i<l;i++)
		{
			if(state[i] == '-')
			{
				can=false;
			}
		}
		printf("Case #%d: ",p);
		if(can)
			printf("%d",cnt);
		else printf("IMPOSSIBLE");
		printf("\n");
	}
	return 0;
}
