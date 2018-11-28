#include<iostream> 
#include<string> 
#include<queue> 
#include<algorithm> 
#include<cstdio> 
#include<vector> 
#include<queue> 
#include<climits> 
#include<cstring> 
#include<ctime>
#include<cstdlib>
using namespace std; 

int maxed,Case;
char str[1005];
int num[1005];

int main()
{
	freopen("d://A-large.in","r",stdin);
	freopen("d://output.txt","w",stdout);
	scanf("%d",&Case);
	for(int K=1;K<=Case;K++)
	{
		scanf("%d",&maxed);
		scanf("%s",str);
		for(int i=0;i<=maxed;i++)
		{
			num[i]=str[i]-'0';
		}
		int ans=0;
		int tot=0;
		for(int i=0;i<=maxed;i++)
		{
			if(tot<i) { ans+=(i-tot);tot=i;}
			tot+=num[i];
		}
		printf("Case #%d: %d\n",K,ans);
	}
}

