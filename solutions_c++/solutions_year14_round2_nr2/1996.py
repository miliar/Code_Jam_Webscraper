//#include<iostream>
#include<vector>
#include<fstream>
#include<cmath>
using namespace std;
int t;
ifstream cin("B-small-attempt0.in");
ofstream cout("B-small-attempt0.out");
int main()
{
	cin>>t;
	for(int ii=0;ii<t;ii++)
	{
		int sum=0;
		int a,b,k;
		cin>>a>>b>>k;
		for(int i=0;i<a;i++)
		for(int j=0;j<b;j++)
		if((i&j)<k)
		sum++;
		cout<<"Case #"<<ii+1<<": "<<sum<<endl;
	}
	//cin>>t;
}
