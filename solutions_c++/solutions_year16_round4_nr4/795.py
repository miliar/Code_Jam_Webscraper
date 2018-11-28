#include <stdio.h>
#include <algorithm>

FILE* in=fopen("D-small-attempt0.in","r");
FILE* out=fopen("out.txt","w");

int ans,n,pos[16][16];

int check()
{
	int bin[16]={},one[16]={};
	int i,t,j;
	for(i=0;i<n;i++)
	{
		t=1;
		for(j=0;j<n;j++)
		{
			bin[i]+=pos[i][j]*t;
			one[i]+=pos[i][j];
			t*=2;
		}
	}
	for(i=0;i<n;i++)
	{
		int cnt=0;
		for(j=0;j<n;j++)
		{
			if(bin[i]==bin[j]) cnt++;
			else if(bin[i]&bin[j]) return 0;
		}
		if(cnt!=one[i]) return 0;
	}
	return 1;
}

void DFS(int y,int x,int ch)
{
	if(y==n)
	{
		if(check() && ch<ans) ans=ch;
		return; 
	}
	if(x==n)
	{
		DFS(y+1,0,ch);
		return;
	}
	
	if(pos[y][x]==0)
	{
		pos[y][x]=1;
		DFS(y,x+1,ch+1);
		pos[y][x]=0;
	}
	DFS(y,x+1,ch);
}

void solve()
{
	int i,j;
	fscanf(in,"%d",&n);
	for(i=0;i<n;i++) for(j=0;j<n;j++)
		fscanf(in,"%1d",pos[i]+j);
	
	ans=n*n;
	DFS(0,0,0);
	
	fprintf(out,"%d\n",ans);
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
