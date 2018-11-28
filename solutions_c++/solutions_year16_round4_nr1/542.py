#include<cstdio>
#include<cstring>
#include<string>
#include<algorithm>
using namespace std;
char ans[10001],anst[10001];
void f(char c,int n,char* stt)
{
	if(n==0)
	{
		stt[0]=c;
		stt[1]=0;
		return;
	}
	char sl[10001],sr[10001];
	if(c=='P')
	{
		f('P',n-1,sl);
		f('R',n-1,sr);
	}
	else if(c=='R')
	{
		f('R',n-1,sl);
		f('S',n-1,sr);
	}
	else
	{
		f('S',n-1,sl);
		f('P',n-1,sr);
	}
	sl[1<<(n-1)]=0;
	sr[1<<(n-1)]=0;
	if(strcmp(sl,sr)<0)
	{
		memcpy(stt,sl,1<<(n-1));
		memcpy(stt+(1<<(n-1)),sr,1<<(n-1));
	}
	else
	{
		memcpy(stt,sr,1<<(n-1));
		memcpy(stt+(1<<(n-1)),sl,1<<(n-1));
	}
	stt[1<<n]=0;
	return;
}
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int cas=0,T,n,r,p,s;
	scanf("%d",&T);
	while(T--)
	{
		scanf("%d%d%d%d",&n,&r,&p,&s);
		
		ans[0]=120;
		ans[1]=0;
		f('P',n,anst);
		if(count(anst,anst+(1<<n),'R')==r&&count(anst,anst+(1<<n),'S')==s&&count(anst,anst+(1<<n),'P')==p
		&&strcmp(anst,ans)<0)
		{
			strcpy(ans,anst);
		}
		f('R',n,anst);
		if(count(anst,anst+(1<<n),'R')==r&&count(anst,anst+(1<<n),'S')==s&&count(anst,anst+(1<<n),'P')==p
		&&strcmp(anst,ans)<0)
		{
			strcpy(ans,anst);
		}
		f('S',n,anst);
		if(count(anst,anst+(1<<n),'R')==r&&count(anst,anst+(1<<n),'S')==s&&count(anst,anst+(1<<n),'P')==p
		&&strcmp(anst,ans)<0)
		{
			strcpy(ans,anst);
		}
		printf("Case #%d: ",++cas);
		if(ans[0]==120)
		{
			puts("IMPOSSIBLE");
		}
		else
		{
			puts(ans);
		}
	}
	return 0;
}
/*
4
1 1 1 0
1 2 0 0
2 1 1 2
2 2 0 2
*/

