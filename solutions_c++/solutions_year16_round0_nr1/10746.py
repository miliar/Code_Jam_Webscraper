/*
kavya_D*/

#include<iostream>
#include<stdlib.h>
#include<fstream>
using namespace std;

int a[10]={0,0,0,0,0,0,0,0,0,0};
int T,n,N,x,sum=0,j,temp;
int flag=0;
void Sum()
{	sum=0;
	for(int k=0;k<10;k++)
		sum+=a[k];
	if(sum==10)
		flag=1;
}

void cal(int n)
{
	if(sum>10)
		return;
	while(n!=0 && sum<11)
	{
		x=n%10;
		a[x]=1;
		n=n/10;
	}
}

int main()
{
   ifstream f_in;
   ofstream f_out;
   f_in.open("A-large.in",ios::in);
   f_out.open("ex.out",ios::out);
   f_in>>T;
	for(int i=1;i<=T;i++)
	{
		sum=0; flag=0; j=2;
		for(int y=0;y<10;y++)
			a[y]=0;
		f_in>>N;
		if(N==0)
			goto ert;
		temp=N;
		while(flag==0)
		{
			cal(temp);
			Sum();
			temp=N*j;	j++;
		}
	
ert:
		if(sum==10)
		{
			f_out<<"Case #"<<i<<": "<<(temp-N)<<endl;
		}
		else
			f_out<<"Case #"<<i<<": INSOMNIA"<<endl;

	}
	f_in.close();
	f_out.close();
	return 0;
}
