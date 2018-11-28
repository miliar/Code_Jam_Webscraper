#include<iostream>
#include<cmath>
#include<fstream>
#include<cstdio>
using namespace std;
ofstream outfile;
int isHW(int x)
{
	int is=0,a,b,num;
	if(x<10) return 1;
	while(x>9)
	{
		a=x%10;
		b=x;
		num=1;
		while(b>9)
		{
			b/=10;
			num*=10;
		}
		if(a!=b) return 0;
		x-=b*num;
		x/=10;
	}
	return 1;
}
int main()
{
	freopen("C-small-attempt1.in","r",stdin);
	outfile.open("output.txt");
	int t,i,j,k,num,a,b;
	cin>>t;
	for(i=0;i<t;i++)
	{
		num=0;
		cin>>a>>b;
		j=(int)sqrt(a);
		if(j*j<a) j++;
		k=(int)sqrt(b);
		while(j<=k)
		{
			if(isHW(j)&&isHW(j*j)) num++;
			j++;
		}
		outfile<<"Case #"<<i+1<<": "<<num<<endl;
	}
	return 0;
}