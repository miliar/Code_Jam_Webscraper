#include <iostream>
#include <iomanip>
using namespace std;

int main()
{
	int testCases;
	double C,F,X;
	cin>>testCases;int n=testCases;
	while(testCases--)
	{
		cin>>C>>F>>X;
		double t=0.0000000;
		double r=2.0;
		while(1)
		{
			if((C/r+X/(r+F)) > X/r)
			{
				t+=X/r;
				break;
			}
			else
			{
				t+= C/r;
				r+=F;
			}
		}
		//cout<<setprecision(7)<<fixed<<"\n";
		cout<<"Case #"<<setprecision(7)<<fixed<<(n-testCases)<<":"<<" "<<t<<endl;
	}
	return 0;
}