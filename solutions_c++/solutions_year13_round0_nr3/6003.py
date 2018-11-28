#include<iostream>
using namespace std;
#include<math.h>
#include<stdio.h>

int palin(int i)
{
	int r=0,ir=0,io=i;
	while(i>0)
	{
		r=i%10;
		ir=ir*10+r;
		i=i/10;
	}
	if((io-ir)==0)return 1;
	else return 0;
}

int main(int argc,char **argv)
{
	int t;
	int a,b;
	FILE * fp=fopen(argv[1],"r");
	fscanf(fp,"%d",&t);
	char ch=fgetc(fp);

	for(int k=1;k<=t;k++)
	{
		fscanf(fp,"%d",&a);
		ch=fgetc(fp);
		fscanf(fp,"%d",&b);
		ch=fgetc(fp);
		int cnt=0;
		for(int i=a;i<=b;i++)
		{		
			int x=sqrt(i);
			if((x*x)==i)if(palin(i))if(palin(x))cnt++;
		}		
		cout<<"Case #"<<k<<": "<<cnt<<endl;
	}
}
