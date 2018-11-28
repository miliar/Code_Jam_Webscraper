#include<iostream>
#include<cstdlib>
#include<cstring>
#include<cstdio>
#include<cmath>
#include<algorithm>
#include<cassert>
using namespace std;
#define rep(i,n) for(int i=1;i<=(n);++i)
#define rep2(i,a,b) for(int i=(a);i<=(b);++i)
int nx,ny;
		//i,2,3,s,last2/3
long long tdp[110][13][2];

int gcd(int ia,int ib)
{
	int ir=ia%ib;
	while(ir)
	{
		ia=ib;ib=ir;ir=ia%ib;
	}
	return ib;
}
void task()
{
	scanf("%d%d",&nx,&ny);
	memset(tdp,0,sizeof tdp);
	tdp[0][1][0]=1;
	int tmul;
	long long tot=0;
	#define tranto(mul,to) to=(to+mul*tdp[i][irep][ilast])%1000000007
	rep2(i,0,nx)
	{
		rep(irep,12)
		{
			rep2(ilast,0,1)
			{
				if(!tdp[i][irep][ilast])continue;
				//cout<<i<<","<<irep<<","<<ilast<<":"<<tdp[i][irep][ilast]<<endl;
				//switch 33
				if(i==0||ilast==0)
				{
					tranto(1,tdp[i+2][irep][1]);
				}
				//switch 112 -> i3=1
				if((i==0||ilast==1)&&ny%4==0)
				{
					int tn=4;
					int tg=gcd(irep,tn);
					tranto(tg,tdp[i+3][irep*tn/tg][0]);
				}
				//switch 12 -> i2=1
				if((i==0||ilast==1)&&ny%6==0)
				{
					int tn=6;
					int tg=gcd(irep,tn);
					tranto(tg,tdp[i+2][irep*tn/tg][0]);
				}
				//switch 22 -> is=1
				if((i==0||ilast==1)&&ny%3==0)
				{
					int tn=3;
					int tg=gcd(irep,tn);
					tranto(tg,tdp[i+2][irep*tn/tg][0]);
				}
				//switch 2
				if(i==0||ilast==1)
				{
					tranto(1,tdp[i+1][irep][0]);
				}
				if(i==nx)
				tranto(1,tot);
			}
		}
	}
	printf("%lld\n",tot);
}
int main()
{
	freopen("in","r",stdin);
	freopen("out","w",stdout);
	
	int nt;scanf("%d",&nt);
	rep(it,nt){printf("Case #%d: ",it);task();}
}
