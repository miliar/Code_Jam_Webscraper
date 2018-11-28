#include<cstdio>
#include<cstdlib>
#include<iostream>
#include<algorithm>
#include<cmath>
#include<cstring>
using namespace std;

int b[5],a[5][5];
int xzq,q,i,j,t,tt,l,k;
bool p[5];

int main()
{
	scanf("%d",&t);
	for(tt=1;tt<=t;tt++){
		scanf("%d",&l);
		for(i=1;i<=4;i++)
			for(j=1;j<=4;j++){
				scanf("%d",&a[i][j]);
			}
		for(i=1;i<=4;i++)b[i]=a[l][i];
		scanf("%d",&k);
		for(i=1;i<=4;i++)
			for(j=1;j<=4;j++){
				scanf("%d",&a[i][j]);
			}
		xzq=0;
		q=0;
		p[1]=false; p[2]=false; p[3]=false; p[4]=false;
		for(i=1;i<=4;i++){
			for(j=1;j<=4;j++){
				if(a[k][i]==b[j]&&p[j]==false){
					xzq=b[j];
					q++;
					p[j]=true;
				}
			}
		}
		printf("Case #%d: ",tt);
		if(q==1)printf("%d\n",xzq);
		if(q==0)printf("Volunteer cheated!\n");
		if(q>1)printf("Bad Magician!\n");
	}
	
}