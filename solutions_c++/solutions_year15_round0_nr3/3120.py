// Jai sai ram
// Google Code Jam 2015
// Prob B
#include<stdio.h>
#include<algorithm>
#include<algorithm>
#include<string>
#include<iostream>
using namespace std;
#define ll long long
#define ull unsigned long long
#define inp(a) fscanf(fp1,"%lld",&a);
#define outp(a) fprintf(fp2,"%lld\n",a);
int a[100010];
int pre[100010];
int suf[100010];
int main()
{
	FILE *fp1,*fp2;
	fp1=fopen("INPUT2.in","r");
	fp2=fopen("OUTPUT2.txt","w");
	if(!fp2 || !fp2)
		return 0;
	int tc;fscanf(fp1,"%d",&tc);
	int conv[5][5];
		conv[4][4]=-1;
		conv[1][4]=4;
		conv[2][4]=-3;
		conv[3][4]=2;
		conv[4][1]=4;
		conv[1][1]=1;
		conv[2][1]=2;
		conv[3][1]=3;
		conv[4][2]=3;
		conv[1][2]=2;
		conv[2][2]=-1;
		conv[3][2]=-4;
		conv[4][3]=-2;
		conv[1][3]=3;
		conv[2][3]=4;
		conv[3][3]=-1;
		conv[0][0]=conv[0][1]=conv[0][2]=conv[0][3]=conv[0][4]=1;
		conv[1][0]=conv[2][0]=conv[3][0]=conv[4][0]=1;
	for(int i=1;i<=tc;i++)
	{
		ull l,x;
		fscanf(fp1,"%llu%llu",&l,&x);
	//	printf("heallo1\n");
		if(l*x>10000)
		{
			if(x>100)
			{
				if(!(x%2))
					x=100;
				else
					x=101;
			}
		}
		char st[10001];
		fscanf(fp1,"%s",st);
	//	printf("heallo2\n");
		for(ll j=0;j<x;j++)
		{
			for(ll k=0;k<l;k++)
			{
				if(st[k]=='i')
					a[j*l+k]=2;
				else if(st[k]=='j')
					a[j*l+k]=3;
				else
					a[j*l+k]=4;
			}
		}
	//	printf("hello3\n");
		pre[0]=a[0];
		for(ll j=1;j<(x*l);j++)
		{
			if(pre[j-1]>0)
				pre[j]=conv[pre[j-1]][a[j]];
			else
				pre[j]=-1*conv[-pre[j-1]][a[j]];
		}
		suf[x*l-1]=a[x*l-1];
	//	printf("hello5\n");
		for(ll j=x*l-2;j>=0;j--)
		{
	//		printf("= %d %d \n",j,j>=0);
			if(suf[j+1]>0)
				suf[j]=conv[a[j]][suf[j+1]];
			else
				suf[j]=-1*conv[a[j]][-suf[j+1]];
		}
		int flag=0;
	//	printf("hello4\n");
	//	for(ll j=0;j<x*l;j++)
	//		printf("%d %d\n",pre[j],suf[j]);
		for(ll j=0;j<x*l;j++)
		{
			for(ll k=j+2;k<(x*l);k++)
			{
				if(pre[j]==2 && suf[k]==4 && pre[k-1]==4)
				{
					flag=1;
					goto exit1;
				}
			}
		}
		exit1:;
		if(flag)
			fprintf(fp2,"Case #%d: YES\n",i);
		else
			fprintf(fp2,"Case #%d: NO\n",i);
	}
	return 0;
}
