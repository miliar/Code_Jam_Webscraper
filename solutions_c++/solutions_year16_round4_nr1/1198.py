#include<stdio.h>

char ans[20];
char tmp[20];
int anscheck;
int n,m, P,R,S;

void test(void)
{
	int x=m,i,j;
	char temp[20];
	for(i=1;i<=m;i++)
		temp[i]=tmp[i];
	for(i=1;i<=n;i++)
	{
		for(j=1;j<=x/2;j++)
		{
			if(temp[2*j]==temp[2*j-1])
				return;
			if(temp[2*j]!='P' && temp[2*j-1]!='P')
				temp[j]='R';
			else if(temp[2*j]!='R' && temp[2*j-1]!='R')
				temp[j]='S';
			else if(temp[2*j]!='S' && temp[2*j-1]!='S')
				temp[j]='P';
		}
		x/=2;
	}
	anscheck=1;
	for(i=1;i<=m;i++)
		ans[i]=tmp[i];
	ans[m+1]=NULL;
}

void recall(int p,int r,int s,int lev)
{
	if(anscheck==1)
		return;
	if(lev==m+1)
	{
		test();
		return;
	}
	if(p!=P)
	{
		tmp[lev]='P';
		recall(p+1,r,s,lev+1);
	}
	if(r!=R)
	{
		tmp[lev]='R';
		recall(p,r+1,s,lev+1);
	}
	if(s!=S)
	{
		tmp[lev]='S';
		recall(p,r,s+1,lev+1);
	}
}



int main(void)
{
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	int t,k,x;
	scanf("%d",&t);
	for(k=1;k<=t;k++)
	{
		printf("Case #%d: ",k);
		scanf("%d %d %d %d",&n,&R,&P,&S);
		m=1;
		for(x=1;x<=n;x++)
			m*=2;
		anscheck=0;
		recall(0,0,0,1);
		if(anscheck==0)
			printf("IMPOSSIBLE");
		else
			printf("%s",&ans[1]);
		printf("\n");
	}
}