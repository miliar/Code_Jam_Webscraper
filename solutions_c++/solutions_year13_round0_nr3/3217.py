#include<iostream>
#include<stdio.h>
using namespace std;
int main()
{
long long int ans_arr[21]={1,4,9,121,484,10201,12321,14641,40804,44944,1002001,1234321,4008004,100020001,102030201,104060401,121242121,123454321,125686521,400080004,404090404};
int i,j;
long long int a,b;
int t,k,counter;
cin>>t;
for(k=1;k<=t;k++)
{
	cin>>a>>b;
	counter=0;
	for(i=0;i<21;i++)
	{
	if(ans_arr[i]>=a && ans_arr[i]<=b)
	counter++;
	}
	
	cout<<"Case #"<<k<<": "<<counter<<endl;
}
return 0;
}
