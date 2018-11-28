#include<cstdio>
#include<cstring>
#include<algorithm>
#include<queue>
#include<vector>
#define maxn 100005
using namespace std;
int main()
{
	char a[2005];
	int vis[300];
	int ans[30];
	int T;
	freopen("E:A-large.in","r",stdin);
	freopen("E:outA.txt","w",stdout);
	scanf("%d",&T);
	char let[11][11]={"ZERO","ONE","TWO","THREE","FOUR","FIVE","SIX","SEVEN","EIGHT","NINE"};
	for(int c=1;c<=T;c++)
	{
		memset(ans,0,sizeof(ans));
	 printf("Case #%d: ",c);
	 scanf("%s",a);
	 int len=strlen(a);
	 memset(vis,0,sizeof(vis));
		for(int i=0;i<len;i++)
		{
			for(int j='A';j<='Z';j++)
			{
				if(a[i]==j)
				{
					vis[j]++;
				}
			}
		}
	 while(vis['Z'])
	 {
	 	ans[0]++;
		vis['Z']--;
		vis['E']--;
		vis['R']--;
		vis['O']--;
	 }
	 while(vis['X'])
	 {
	 	vis['X']--;
	 	ans[6]++;
		vis['I']--;
		vis['S']--;
	 }
	 while(vis['W'])
	 {
	 	ans[2]++;
	 	vis['W']--;
	 	vis['T']--;
	 	vis['O']--;
	 }
	 while(vis['G'])
	 {
	 	ans[8]++;
	 	vis['G']--;
	 	vis['E']--;
	 	vis['I']--;
	 	vis['H']--;
	 	vis['T']--;
	 }
	 while(vis['S'])
	 {
	 	ans[7]++;
	 	vis['S']--;
	 	vis['E']--;
	 	vis['V']--;
	 	vis['E']--;
	 	vis['N']--;
	 }
	 while(vis['U'])
	 {
	 	ans[4]++;
	 	vis['F']--;
	 	vis['O']--;
	 	vis['U']--;
	 	vis['R']--;
	 }
	 while(vis['V'])
	 {
		ans[5]++;
		vis['F']--;
		vis['I']--;
		vis['V']--;
		vis['E']--;
	 }
	 while(vis['O'])
	 {
	 	ans[1]++;
	 	vis['O']--;
	 	vis['N']--;
	 	vis['E']--;
	 }
	 ans[3]=vis['R'];
	 ans[9]=vis['I'];
	 for(int i=0;i<=9;i++)
	 {
	 	while(ans[i])
	 	{
	 		printf("%d",i);
	 		ans[i]--;
	 	}
	 	
	 }
	 printf("\n");
	 
	}

	
}
