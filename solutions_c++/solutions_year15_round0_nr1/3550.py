#include<iostream>
#include<cstdio>
#include<cstring>
#include<cstdlib>
using namespace std;
#define rep2(x,from,to) for(int x=(from);(x)<(to);(x)++)
#define rep(x,to) rep2(x,0,to)
int n;
int t;
char s[1003];
int ans;
int hito;
int ppp;
int main()
{
	FILE *fp=fopen("c.txt","w");
	FILE *fpp=fopen("A-large.in","r");
	fscanf(fpp,"%d",&n);
	rep(i,n)
	{
		ans=0;
		hito=0;
		fscanf(fpp,"%d %s",&t,s);
		rep(j,t+1)
		{
			if(s[j]!='0')
			{
				if(hito<j)
				{
					ans+=(j-hito);
					hito=j;
				}
				ppp=(int)(s[j]-'0');
				hito+=ppp;
			}
		}
		fprintf(fp,"Case #%d: %d\n",i+1,ans);
	}
	return 0;
}