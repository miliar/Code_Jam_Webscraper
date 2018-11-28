#include <cstdio>
#include <cstring>
#include <iostream>
using namespace std;
int T,N;
char str[101][102];
char lstr[101][102];
int repeat[101][102];
int rep[102];
inline int abs(int x)
{
	return x>0?x:-x;
}
int main()
{
	scanf("%d",&T);
	for (int TT=1;TT<=T;TT++)
	{
		scanf("%d",&N);
		memset(lstr,0,sizeof(lstr));
		for (int i=1;i<=N;i++)
		{
			scanf("%s",str[i]);
			int k=0;
			for (int j=0;str[i][j];j++)
				if (str[i][j]!=str[i][j+1])
					lstr[i][k++]=str[i][j];
			// printf("%s\n",lstr[i]);
		}
		int ans_exist=1;
		for (int i=1;i<N;i++)
			ans_exist&=strcmp(lstr[i],lstr[i+1])==0;
		printf("Case #%d: ",TT);
		if (ans_exist)
		{
			int len=strlen(lstr[1]);
			memset(repeat,0,sizeof(repeat));
			memset(rep,0,sizeof(rep));
			for (int i=1;i<=N;i++)
			{
				int k=0,sum=0;
				for (int j=0;str[i][j];j++)
				{
					repeat[i][k]++;
					if (str[i][j]!=str[i][j+1])
					{
						rep[k]+=repeat[i][k];
						k++;
					}
				}
			}
			for (int i=0;i<len;i++)
				rep[i]/=N;
			int ans=0,ans1,ans2;
			for (int i=0;i<len;i++)
			{
				ans1=ans2=0;
				for (int j=1;j<=N;j++)
				{
					ans1+=abs(rep[i]-repeat[j][i]);
					ans2+=abs(rep[i]-repeat[j][i]+1);
				}
				ans+=min(ans1,ans2);
				// printf("rep=%4d,ans1=%4d,ans2=%4d\n",rep[i],ans1,ans2);
			}
			printf("%d\n",ans);
		}
		else
			printf("Fegla Won\n");
	}
	return 0;
}