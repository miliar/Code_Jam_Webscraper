#include<iostream>
using namespace std;
#include<unistd.h>
#include<stdio.h>
#include<stdlib.h>
int main()
{
	int ncase=0,k;
	char ch;
	FILE * fp;

	fp=fopen("large.in","r");
	fscanf(fp,"%d",&ncase);
	for(k=1;k<=ncase;k++)
	{
		int tic[4][4]={{0}};
		int i,j;	
		int d1=0,d2=0,r[4]={0,0,0,0},c[4]={0,0,0,0},nc=0,flag=0;
		ch=fgetc(fp);
		for(i=0;i<4;i++)
		for(j=0;j<5;j++)
		{
			ch=fgetc(fp);	
	
			if(ch=='\n');
			if(ch=='X')tic[i][j]=1;
			if(ch=='O')tic[i][j]=5;
			if(ch=='T')tic[i][j]=25;
			if(ch=='.')tic[i][j]=125;
		}
		for(i=0;i<4;i++)r[i]=(tic[i][0]+tic[i][1]+tic[i][2]+tic[i][3]);
		for(i=0;i<4;i++)c[i]=(tic[0][i]+tic[1][i]+tic[2][i]+tic[3][i]);
		for(i=0;i<4;i++){d1+=tic[i][i];d2+=tic[i][3-i];}
		
		for(i=0;i<4;i++)
		{
			if(r[i]==4||r[i]==28||c[i]==4||c[i]==28)flag=1;
			if(r[i]==20||r[i]==40||c[i]==20||c[i]==40)flag=2;
			if(r[i]>=125||c[i]>=125)nc=1;
		}
		if(d1==4||d1==28||d2==4||d2==28)flag=1;
		if(d1==20||d1==40||d2==20||d2==40)flag=2;
		if(flag==1){cout<<"Case #"<<k<<": X won\n";}
		else if(flag==2){cout<<"Case #"<<k<<": O won\n";}
		else if(nc==1){cout<<"Case #"<<k<<": Game has not completed\n";}
		else {cout<<"Case #"<<k<<": Draw\n";}
	
	}
	return 0;		
		
}
