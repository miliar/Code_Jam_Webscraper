#include<iostream>
#include<stdio.h>
#include<algorithm>

using namespace std;

int main()
{
	int T;
	scanf("%d",&T);
	int N,M;
	bool ok;
	int *mR,*mC;
	int **n;
	int i,j,max;
	for(int c=1;c<=T;c++)
	{
		ok=true;
		scanf("%d",&N);
		scanf("%d",&M);
		n=new int*[N];
		mR=new int[N];
		mC=new int[M];
		for(i=0;i<N;i++)
		{
			n[i]=new int[M];
			for(j=0;j<M;j++)
				scanf("%d",&n[i][j]);
		}
		for(j=0;j<M;j++)
		{
			max=0;
			for(i=0;i<N;i++) if(n[i][j]>max) max=n[i][j];
			mC[j]=max;
		}
		for(i=0;i<N;i++)
		{
			max=0;
			for(j=0;j<M;j++) if(n[i][j]>max) max=n[i][j];
			mR[i]=max;
		}
		for(i=0;i<N;i++)
			for(j=0;j<M;j++)
				if(n[i][j]!=mR[i]&&n[i][j]!=mC[j]) ok=false;
		if(ok)
			printf("Case #%d: YES\n",c);
		else
			printf("Case #%d: NO\n",c);
	}
	return 0;
}
