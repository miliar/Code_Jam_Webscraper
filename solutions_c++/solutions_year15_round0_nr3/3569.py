#include<bits/stdc++.h>
#include "iostream"
// coded by coolboy95
using namespace std;
int 
yolo,
i,j,
dyna_pro[100001][5],s,answer2,t,fluuu,
matrix_babu[10][10],l,x,array[100001];
	char stringggg[100001];
int main()
{
	scanf("%d",&t);
	for(yolo=1;yolo<=t;yolo++)
	{
		scanf("%d%d",&l,&x);
		scanf("%s",stringggg);
		for(i=0;i<x;i++)
			for(j=0;j<l;j++)
			{
				if(stringggg[j]=='i')
					array[i*l+j]=2;	else if(stringggg[j]=='j')
					array[i*l+j]=3;
			   	else if(stringggg[j]=='k')
					array[i*l+j]=4;
			}
		
		matrix_babu[1][1]=1; 
		matrix_babu[1][2]=2; 
		matrix_babu[1][3]=3;
		matrix_babu[1][4]=4;
		matrix_babu[2][1]=2; 
		matrix_babu[2][2]=-1; 
		matrix_babu[2][3]=4;
		matrix_babu[2][4]=-3;
		matrix_babu[3][1]=3;
		matrix_babu[3][2]=-4;
		matrix_babu[3][3]=-1; 
		matrix_babu[3][4]=2;
		matrix_babu[4][1]=4; 
		matrix_babu[4][2]=3;
		matrix_babu[4][3]=-2; 
		matrix_babu[4][4]=-1;
		l=l*x;
		
		memset(dyna_pro,0,sizeof(dyna_pro));
		answer2=array[0];
		if(answer2==2)
			dyna_pro[0][2]=1;   
		for(i=1;i<l;i++)
		{
			if(answer2>0)
				answer2=matrix_babu[answer2][array[i]];
			else 
				answer2=-1*matrix_babu[abs(answer2)][array[i]];
			if(answer2==2)
				dyna_pro[i][2]=1;
		}
		answer2=1;
		for(i=0;i<l;i++)
		{
			if(dyna_pro[i][2]==1)
			{		answer2=1;
				for(j=i+1;j<l;j++)
				{
					if(answer2>0)
						answer2=matrix_babu[answer2][array[j]];
					else 
						answer2=-1*matrix_babu[-1*answer2][array[j]];
					if(answer2==3)
						dyna_pro[j][3]=1;		}
			}
		}
		answer2=1;	fluuu=0;
		for(i=0;i<l;i++)
		{if(dyna_pro[i][3]==1)
			{
				answer2=1;
				for(j=i+1;j<l;j++)
				{
					if(answer2>0)	answer2=matrix_babu[answer2][array[j]];
					else answer2=-1*matrix_babu[-1*answer2][array[j]];
				}
				if(answer2==4)
			   	{fluuu=1;
					break;		}
			}
 }
	           	if(fluuu==1)
			printf("Case #%d: YES\n",yolo);
	                       	else
			printf("Case #%d: NO\n",yolo);
	}
}