#include<iostream>
#include<cmath>
#include<string>
using namespace std;

int main()
{
	long long int t,T,r,n,j,a,temp,sum,x,y,b,temp1;
	int i,z;
	cin>>T;
	string s;
	for(t=1;t<=T;t++)
	{
		sum=0;
		a=1;
		cin>>n>>j;
		for(i=0;i<n-1;i++)
		{
			sum+=a;
			for(x=0;x<=i;i++)
				a*=2;
			
		}
		a=1;
		for(i=0;i<n-1;i++)
			a*=2;
		int bin[a][n];
		i=1;
		for(x=sum;x>=a+1;x=x-2)
		{	
			z=0;
			temp1=x;
			while(temp1!=0)
			{
				r=a%2;
				bin[i][z]=r;
				temp1=temp1/10;
				z++;
			}
			for(z=0;z<n;z++)
			cout<<bin[i][z];
			i++;
		}
		
	}	
}