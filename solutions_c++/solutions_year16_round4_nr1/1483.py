#include <stdio.h>

FILE* in=fopen("A-small-attempt1.in","r");
FILE* out=fopen("out.txt","w");

int tor[8];
int flag;

int check(int n)
{
	if(flag) return 1;
	int cur[8],next[8];
	int i;
	for(i=0;i<n;i++) cur[i]=tor[i];
	while(n>1)
	{
		for(i=0;i<n/2;i++)
		{
			if(cur[2*i]==cur[2*i+1]) return 0;
			else cur[i]=(5-(cur[2*i]+cur[2*i+1]))%3;
		}
		n/=2;
	}
	return flag=1;
}

void f(int r,int p,int s,int k,int n)
{
	if(flag) return;
	if(k==n)
	{
		check(n);
		return;
	}
	if(flag) return;
	if(p)
	{
		tor[k]=1;
		f(r,p-1,s,k+1,n);
	}
	if(flag) return;
	if(r)
	{
		tor[k]=0;
		f(r-1,p,s,k+1,n);
	}
	if(flag) return;
	if(s)
	{
		tor[k]=2;
		f(r,p,s-1,k+1,n);
	}
}

void print(int n)
{
	int i;
	for(i=0;i<n;i++) fprintf(out,"%c",tor[i]==0?'R':tor[i]==1?'P':'S');
	fprintf(out,"\n");
}

void solve()
{
	int n,r,p,s;
	fscanf(in,"%d %d %d %d",&n,&r,&p,&s);
	
	flag=0;
	f(r,p,s,0,1<<n);
	if(flag) print(1<<n);
	else fprintf(out,"IMPOSSIBLE\n");
}

int main()
{
	int i,t;
	fscanf(in,"%d",&t);
	for(i=1;i<=t;i++)
	{
		fprintf(out,"Case #%d: ",i);
		solve();
	}
	return 0;
}
