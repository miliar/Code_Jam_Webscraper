#include<iostream>
#include<conio.h>
#include<math.h>
using namespace std;
long long int convert(int a[],int k)
{
	long long int res=0;
	for(int i=0;i<16;i++)
	{
		if(a[i]==1)
		res+=(pow(k,i));
	}
	return res;
}
long long int check_divisor(long long int a)
{
	long long int limit=sqrt(a);
	if(a==2)
	return -1;
	for(int i=2;i<=limit;i++)
	{
		if(a%i==0)
		return i;
	}
	return -1;
}
int main()
{
	int t;
	cin>>t;
	cout<<"Case #1:"<<endl;
	int N,J;
	cin>>N;
	cin>>J;
// long long int a=32768;
	long long int n=0;
	long long int test;
	int a[16]={0};
	a[15]=1;
	a[0]=1;
	int divisor_array[9];
	int j=1;
	int i=0;
	while(i<J)
	{
		//cout<<"Count i "<<i<<" "<<endl;
		j=1;
		test=n;
		n++;
		while(test!=0)
		{
			a[j]=test%2;
			test/=2;
			j++;
		}
	
	
	int flag=0;
	for(int k=2;k<=10;k++)
	{
		long long int divisor;
		long long int converted_no= convert(a,k);
		//cout<<"Divisor No "<<converted_no<<endl;
		divisor=check_divisor(converted_no);
		if(divisor>=2)
		{
			  divisor_array[k-2]=divisor;
		}
		else
			flag=1;
	}
	if(flag==0)
 	{
		for(int l=15;l>=0;l--)
			cout<<a[l];
		for(int k=0;k<9;k++){
  				cout<<" "<<divisor_array[k];
 			}
 			cout<<endl;
 			i++;
	}
 	flag=0;

	}
	getch();
}
