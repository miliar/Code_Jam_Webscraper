#include <cstdio>
#include <cstring>
#include <iostream>
using namespace std;
int n,r,p,s;
char str[1000000];
int f(int x)
{
	int ans=1;
	for(int i=1;i<=x;i++)
		ans*=2;
	return ans;
}
void fun()
{
	for(int sb=1;sb<=n;sb++)
	{
		int p=f(sb);
		int len=f(n);
		for(int j=1;j<=len;j+=p)
		{

			int ok1=0;
			int pp=0;
			while(pp<=p/2)
			{
				//cerr <<"j = "<< j <<", pp = "<< pp << endl;
				if(str[j+pp]<str[j+p/2+pp]){ok1=1;break;}
				if(str[j+pp]>str[j+p/2+pp]){ok1=0;break;}
				pp++;
			}
			if(!ok1)
			{
				for(int l=0;l<p/2;l++)
				{
					swap(str[j+l],str[j+l+p/2]);
				}
			}
		}
	}

	//printf("str = %s\n", str);
}
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("sample.out","w",stdout);
	int t;
	scanf("%d",&t);
	int cccc=0;
	while(t--)
	{
		cccc++;
		scanf("%d%d%d%d",&n,&r,&p,&s);
		memset(str,0,sizeof(str));
		int ok=0;
			str[1]='R';

			for(int i=0;i<n;i++)
			{
				for(int j=f(i);j>=1;j--)
				{
					if(str[j]=='R'){str[2*j-1]='R';str[2*j]='S';}
					else if(str[j]=='S'){str[2*j-1]='P';str[2*j]='S';}
					else if(str[j]=='P'){str[2*j-1]='P';str[2*j]='R';}
				}
				
			}
			int cntr=0,cntp=0,cnts=0;
			for(int i=1;i<=f(n);i++)
			{
				if(str[i]=='R')cntr++;
				if(str[i]=='P')cntp++;
				if(str[i]=='S')cnts++;
			}
			fun();
			if(cntr==r&&cntp==p&&cnts==s){
				printf("Case #%d: %s\n",cccc,str+1);
				ok=1;
			}
			if(ok)continue;
			str[1]='P';
			for(int i=0;i<n;i++)
			{
				for(int j=f(i);j>=1;j--)
				{
					if(str[j]=='R'){str[2*j-1]='R';str[2*j]='S';}
					else if(str[j]=='S'){str[2*j-1]='P';str[2*j]='S';}
					else if(str[j]=='P'){str[2*j-1]='P';str[2*j]='R';}
				}
			}
			cntr=0,cntp=0,cnts=0;
			for(int i=1;i<=f(n);i++)
			{
				if(str[i]=='R')cntr++;
				if(str[i]=='P')cntp++;
				if(str[i]=='S')cnts++;
			}
			fun();
			if(cntr==r&&cntp==p&&cnts==s){
				printf("Case #%d: %s\n",cccc,str+1);
				ok=1;
			}
			if(ok)continue;
			str[1]='S';
		
		for(int i=0;i<n;i++)
			{
				for(int j=f(i);j>=1;j--)
				{
					if(str[j]=='R'){str[2*j-1]='R';str[2*j]='S';}
					else if(str[j]=='S'){str[2*j-1]='P';str[2*j]='S';}
					else if(str[j]=='P'){str[2*j-1]='P';str[2*j]='R';}
				}
			}
			cntr=0,cntp=0,cnts=0;
			for(int i=1;i<=f(n);i++)
			{
				if(str[i]=='R')cntr++;
				if(str[i]=='P')cntp++;
				if(str[i]=='S')cnts++;
			}
			fun();
			if(cntr==r&&cntp==p&&cnts==s){
				printf("Case #%d: %s\n",cccc,str+1);
				ok=1;
			}
			if(!ok)printf("Case #%d: IMPOSSIBLE\n",cccc);
	}
	return 0;
}