#include<iostream>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cmath>
using namespace std;
#define rep2(x,from,to) for(int x=(from);(x)<(to);(x)++)
#define rep(x,to) rep2(x,0,to)

int T;
int d;
int p[3004];
int ans;
int koho;
int dai;
int main()
{
	FILE *fp=fopen("B-large.in","r");
	FILE *fpp=fopen("outbbbb.txt","w");
	fscanf(fp,"%d",&T);
	rep(kkk,T)
	{
		ans=-1;
		dai=-1;
		fscanf(fp,"%d",&d);
		rep(i,d)
		{
			fscanf(fp,"%d",&p[i]);
			dai=max(dai,p[i]);
		}
		rep2(i,1,dai+1)
		{
			koho=i;
			rep(j,d)
			{
				if(p[j]%i==0)
				{
					koho+=(p[j]/i-1);
				}
				else
				{
					koho+=(p[j]/i);
				}
			}
			if(ans==-1)ans=koho;
			else ans=min(ans,koho);
		}
		fprintf(fpp,"Case #%d: %d\n",kkk+1,ans);
	}
	fclose(fp);
	fclose(fpp);
	return 0;
}