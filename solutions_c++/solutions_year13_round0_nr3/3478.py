#include<iostream>
#include<cstdlib>
#include<cstdio>
#include<string.h>
#include<cmath>
using namespace std;
#define N 1200

int Q[N];
void getFlag()
{
	Q[0]=0;
	Q[++Q[0]]=0;
	Q[++Q[0]]=1;
	Q[++Q[0]]=4;
	Q[++Q[0]]=9;
	Q[++Q[0]]=121;
	Q[++Q[0]]=484;
}
int main(void)
{
	int T,cse=0,A,B,cnt;
	freopen("data.in","r",stdin);
	freopen("data.out","w",stdout);
	getFlag();

	scanf("%d",&T);
	while(T--)
	{
		scanf("%d%d",&A,&B);
		printf("Case #%d: ",++cse);
		cnt=0;

		for(int i=1;i<=Q[0];i++)
			if(Q[i]>=A && Q[i]<=B)
				cnt++;
		printf("%d\n",cnt);
	}

	return 0;
}
/*

*/