#include<iostream>
#include<math.h>
#include<stdio.h>
using namespace std;
int main()
{
	freopen("test.txt","w",stdout);
	int c;
	long long int r,t,temp,temp2;
	cin>>c;
	int i,j,k;
	for(i=1;i<=c;i++)
	{
		cin>>r>>t;
		temp=sqrt((2*r-1)*(2*r-1)+(8*t));
		temp2=(-(2*r-1)+temp)/4;
		cout<<"Case #"<<i<<": "<<temp2<<endl;
	}
}
