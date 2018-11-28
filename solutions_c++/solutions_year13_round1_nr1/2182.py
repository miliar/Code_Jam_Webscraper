#include<iostream>
#include<cstdio>
#include<cmath>
#include<vector>
#include<algorithm>
#include<fstream>
#define ll long long
#define ld long double
ll r,t;
ll k; 
long double x;
using namespace std;
//fstream fin("i.in",ios::in);
int call()
{
	x=0;k=0;r=0;t=0;
	cin>>r>>t;
	x=(ld)((ld)((ld)sqrt((4*(ld)pow(r,2)-4*r+1+8*t))-(2*r-1))/4);
	//cerr<<x;
	k=(ll) x;
	cout<<k;
	return 0;
}
int main()
{

	int n; 
	cin>>n;
	for(int i=0;i<n;i++)
	{
		cout<<"Case #"<<i+1<<": "; call();
		cout<<endl;
	}
	return 0;
}
