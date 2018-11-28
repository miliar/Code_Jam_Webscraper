#include<iostream>
#include<stdio.h>
#include<iomanip>
using namespace std;
int main()
{
	freopen("test.txt","w",stdout);
	cout<<fixed<<setprecision(10);
	long double c,f,x;
	int t;cin>>t;
	int ii,i,j,k;
	for(ii=1;ii<=t;ii++)
	{
		cin>>c>>f>>x;
		cout<<"Case #"<<ii<<": ";
		long double t=0;//t+=(x/2);
		//cout<<t;
		double v=2;
		while(x*f>c*(v+f))
		{
			t+=(c/v);v+=f;
			//cout<<"Y "<<t<<" "<<v<<endl;
		}
		t+=(x/v);
		cout<<t<<endl;
	}
}
