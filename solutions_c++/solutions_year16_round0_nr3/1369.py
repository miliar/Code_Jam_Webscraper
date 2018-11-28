#include<iostream>
#include<cmath>
using namespace std;
int a[16] ;
long long int power[10];
long long int powera(long long int x,long long int y)
{
	long long int temp;
	if(y == 0)
	return 1;
	temp = powera(x,y/2);
	if(y%2 == 0)
	return temp*temp;
	else
	return x*temp*temp;
}
int main()
{
	int count = 0;
	int t,n,j;
	cin>>t>>n>>j;
	for(int i=2;i<=10;i++)
		power[i] = powera(i,16) + 1;
		
	cout<<"Case #1:"<<endl;
	for(int i = 32769;;i=i+2)
	{
		count++;
		int k = i , p=15;
		while(k!=0)
		{
			a[p--] = k%2;
			k = k/2;
		}
		for(int i=0;i<16;i++)
		cout<<a[i];
		for(int i=0;i<16;i++)
		cout<<a[i];
		cout<<" ";
		for(int i=2;i<=10;i++)
		cout<<power[i]<<" ";
		cout<<endl;
		if(count == 500)
		break;
	}
}
