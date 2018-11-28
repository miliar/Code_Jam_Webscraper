# include<iostream>
#include <iomanip>
using namespace std;
int main ()
{
	int t;double c,f,x;
	cin>>t;
	for(int i=0;i<t;i++)
	{
		cin>>c>>f>>x;
		double a1,a2=0.0,a3;double j=2.0;
		do
		{
			a1=x/j+a2;
			a2=a2+c/j;
			a3=x/(j+f);
			j+=f;
		}
		while(a2+a3<a1);
		std::cout << std::setprecision(7) << std::fixed;
		cout<<"Case #"<<i+1<<": "<<a1<<endl;
		
	}
	return 0;
}