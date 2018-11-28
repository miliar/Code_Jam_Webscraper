#include<stdlib.h>
#include<stdio.h>
#include<iostream>
using namespace std;
int arr[10][10];
int ro,co;
int check()
{
	int i,j,cnt,tot=0,temp=0;
	for(i=0;i<ro;i++)
	{
		cnt=0;
		for(j=0;j<co;j++)
		{
			if(arr[i][j]==1)
			cnt++;
		}
		if(cnt==co)
		{
			tot++;
			for(j=0;j<co;j++)
			arr[i][j]=0;		
		}
	}
	for(j=0;j<co;j++)
	{
		cnt=0;
		for(i=0;i<ro;i++)
		{
			if(arr[i][j]==1)
			{cnt++;}
			if(arr[i][j]==0)
			{cnt++;}
		}
		if(cnt==ro)
		{
			tot++;
			for(i=0;i<ro;i++)
			arr[i][j]=0;		
		}
	}
	for(j=0;j<co;j++)
	for(i=0;i<ro;i++)
	if(arr[i][j]==1)
	return 0;
	for(j=0;j<co;j++)
	for(i=0;i<ro;i++)
	if(arr[i][j]==2)
	temp++;
	if(temp==(ro*co))
	return 1;
	return tot;
}
int intch(char ch)
{
	if((int)ch>=48 && (int)ch<=57)
	return ((int)ch-48);
}
int main(void)
{
	int t,test,num;
	FILE *fp;
	FILE *rf;
	char ch,c[6];
	fp=fopen("B-small-attempt3.in","r");
	fscanf(fp,"%d",&t);
	int rea[t];
	for(test=0;test<t;test++)
	{
		fscanf(fp,"%d",&ro);
		fscanf(fp,"%d",&co);
		for(int i=0;i<ro;i++)
		for(int j=0;j<co;j++)
		{
			ch=getc(fp);
			ch=getc(fp);
			arr[i][j]=intch(ch);
		}
		rea[test]=check();
	}
	rf=fopen("ANS2.in","w+");
	for(test=0;test<t;test++)
	{
		fprintf(rf,"Case #%d: ",test+1);
		if(rea[test]!=0)
		fprintf(rf,"YES\n");
		else	
		fprintf(rf,"NO\n");
	}
}
