#include<iostream>
#include<stdio.h>
#include<math.h>
using namespace std;
int main()
{
	freopen ("output.txt","w",stdout);
	freopen ("input.txt","r",stdin);
	long long T,t,r;
	cin>>T;
	for(int F=1;F<=T;F++)
	{
		cin>>r>>t;
		long long n=1;
		while(t>=2*n+2*r-1)
		{
			t-=2*n+2*r-1;
			n+=2;
		}
		//cout<<n-1<<endl;
		cout<<"Case #"<<F<<": "<<(n-1)/2<<endl;//<<long long(-r+sqrt(r*r+8*t))/4<<endl;
	}
}