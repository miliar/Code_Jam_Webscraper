#include<iostream>
#include<fstream>
#include<stdlib.h>
#include<cstring>
#include<math.h>
using namespace std;

ofstream op;

int ispalin(long i)
{
	long rev=0;
	long n=i;
	while(n>0)
	{
		rev=rev*10+n%10;
		n=n/10;
	}
	if(rev==i)
		return 1;
	return 0;
}
int main()
{
	ifstream ip;
	ofstream op;
	unsigned long i,j,k,l;
	long T,A,B;
	int min;
	int flag=0;
	long *nums=new long[50];
	//int **p,**q;
	int max;
	op.open("output.txt");	
	ip.open("C-large-1.in");
	ip>>T;
	flag=0;
	i=k=1;
	j=3;
	for(i=1;i<=100000000000000;)
	{
			//if(k==111111)
				//cout<<i<<"\n";
			if(ispalin(i)==1 && ispalin(k)==1)
				{nums[flag++]=i;} //cout<<k<<" "<<i<<"\n";}
			i=i+j;
			k++;
			j+=2;
	}
	cout<<flag<<"\n";
	for(l=0;l<T;l++)
	{
		ip>>A>>B;
		//cout<<B<<"\n";
		for(i=0;i<flag;i++)
		{
			if(nums[i]>=A)
				break;
		}
		for(j=flag-1;j>=0;j--)
		{
			if(nums[j]<=B)
				break;
		}
		//cout<<i<<" "<<j<<"\n";
		//cout<<i<<"\n";
		//cout<<flag<<"\n";
		op<<"Case #"<<l+1<<": "<<j-i+1<<"\n";
	}
	ip.close();
	op.close();
	return 0;
	
}
