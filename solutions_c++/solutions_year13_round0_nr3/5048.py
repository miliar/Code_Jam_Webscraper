#include<iostream>
#include<stdio.h>
#include<fstream>
#include<vector>
using namespace std;
int main()
{
	int i,j,t,k,n,a,b;
	cin>>t;
	int arr[5];
	arr[0]=1;
	arr[1]=4;
	arr[2]=9;
	arr[3]=121;
	arr[4]=484;
	for(k=1;k<=t;k++)
	{
		n=0;
		cin>>a>>b;
		for(i=0;i<5;i++)
		{
			j=arr[i];
			if(j>=a&&j<=b)
				n++;
		}
		cout<<"Case #"<<k<<": "<<n<<endl;
	}
	return 0;
}