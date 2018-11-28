#include <iostream>
#include <stdio.h>
using namespace std;

int main() {
	int t,i,j,k,l,m,n=0,p;
	int a[4][4],b[4][4];
	scanf("%d",&t);
	for(l=1;l<=t;l++)
	{
		n=0;
		scanf("%d",&k);
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				scanf("%d",&a[i][j]);
			}
			
		}
		scanf("%d",&m);
		for(i=0;i<4;i++)
		for(j=0;j<4;j++)
		scanf("%d",&b[i][j]);
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++){
			if(a[k-1][i]==b[m-1][j]){
			n++;
			p=a[k-1][i];
			}}
		}
		if(n==1)
		printf("Case #%d: %d\n",l,p);
		else if(n>1)
		printf("Case #%d: Bad magician!\n",l);
		else if(n==0)
		printf("Case #%d: Volunteer cheated!\n",l);
	}
	return 0;
}