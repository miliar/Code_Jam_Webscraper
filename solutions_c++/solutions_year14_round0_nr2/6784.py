#include <iostream>
#include <iomanip>

using namespace std;

int main()
{
	int t;
	cin>>t;
	for(int m=0;m<t;m++)
	{
		double c,f,x;
		cin>>c>>f>>x;
		cout<<setprecision(15);
		double t=0.;
		for(int n=0;;n++)
		{
			if((x-c)/(n*f+2)>x/((n+1)*f+2))
			{
				t+=c/(n*f+2);
			}
			else
			{
				t+=x/(n*f+2);
				break;
			}
		}
		cout<<"Case #"<<m+1<<": "<<t<<endl;
	}
}
