#include <stdio.h>
#include<string.h>
#include <deque>
int main()
{
	using namespace std;
	freopen( "A-large.in", "r", stdin );
	freopen( "output.txt", "w", stdout );
	int n,t,i,sum,lol,len,rsv[10];
	char a[2001];
//	bool rsv;
	scanf("%d",&t);
	for(lol=1;lol<=t;lol++)
	{
		scanf(" %s",&a[0]);
		n=strlen(a);
		for(i=0;i<10;i++)
		rsv[i]=0;
		for(i=0;i<n;i++)
		{
			if(a[i]=='X')rsv[6]++;
			if(a[i]=='Z')rsv[0]++;
			if(a[i]=='U')rsv[4]++;
			if(a[i]=='W')rsv[2]++;
			if(a[i]=='G')rsv[8]++;
			if(a[i]=='H')rsv[3]++;
			if(a[i]=='O')rsv[1]++;
			if(a[i]=='F')rsv[5]++;
			if(a[i]=='S')rsv[7]++;
			if(a[i]=='I')rsv[9]++;
		}
		rsv[3]-=rsv[8];if(rsv[3]<0)rsv[3]=0;
		rsv[1]-=(rsv[0]+rsv[2]+rsv[4]);if(rsv[1]<0)rsv[1]=0;
		rsv[5]-=rsv[4];if(rsv[5]<0)rsv[5]=0;
		rsv[7]-=rsv[6];if(rsv[7]<0)rsv[7]=0;
		rsv[9]-=(rsv[5]+rsv[6]+rsv[8]);	if(rsv[9]<0)rsv[9]=0;
		printf("Case #%d: ",lol);
		for(i=0;i<10;i++)
		{
			while(rsv[i]>0)
			{
				printf("%d",i);rsv[i]--;
			}
		}
		printf("\n");
	}
	return 0;
}
		
