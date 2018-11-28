#include<iostream>
#include<cstdio>
#include<fstream>
#include<cstring>
#include<algorithm>
#include<cstdlib>
#define MAXL 103
using namespace std;

char s[MAXL];
int state[MAXL];
int T;

void solve()
{
	scanf("%d",&T);
	int ca=0;
	
	while(T--)
	{
		ca++;
		printf("Case #%d: ",ca);
		
		scanf("%s",s);
		int len=strlen(s);
		
		for(int i=0;i<len;i++)
		{
			if(s[i]=='+')state[i+1]=1;
			else state[i+1]=0;
		}
		
		int now=len,ans=0;
		
		while(now>0)
		{
		    while(now>0 && state[now]==1)now--;
		    if(now>0)
		    {
		    	ans++;
		    	for(int i=1;i<=now;i++)
		    		state[i]=1-state[i];
		    }
		    else break;
		}
		
		printf("%d\n",ans);
	}
}
		
int main()
{
	//freopen("Revenge of the Pancakes.in","r",stdin);
	//freopen("Revenge of the Pancakes.out","w",stdout);
	
	solve();
	
	return 0;
}
