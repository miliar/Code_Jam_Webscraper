#include<iostream>
#include<stdio.h>
using namespace std;
int main()
{
	int t,m;
	scanf("%d",&t);
	for(m=1;m<=t;++m)
	{
		int c1,c2,a[5][5],i,j,b[5][5],ctr=0,flag=1;
		scanf("%d",&c1);
		for(i=1;i<=4;i++)
		{
		for(j=1;j<=4;j++)
		{
			cin>>a[i][j];
		}}
		scanf("%d",&c2);
		for(i=1;i<=4;i++)
		{
		for(j=1;j<=4;j++)
		{
			cin>>b[i][j];
		}}
		int k=0;
		for(i=1;i<=4;i++)
		{for(j=1;j<=4;j++)
		{
			if(a[c1][i]==b[c2][j])
			{
			   ctr++;
			   //cout<<"ctr-"<<ctr<<endl;
			   k=b[c2][j];
			   //cout<<"k-"<<k<<endl;
		    }
		    //if(ctr==0)
		    //flag==0;
		}}
		if(ctr==1)
		printf("Case #%d: %d\n",m,k);
		else if(ctr>1)
		printf("Case #%d: Bad magician!\n",m);
		if(ctr==0)
		printf("Case #%d: Volunteer cheated!\n",m);
	}
	return 0;
}
