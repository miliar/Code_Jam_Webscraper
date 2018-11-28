#include<iostream>

using namespace std;

int main()
{
	int t;
	cin>>t;
	for(int i=0;i<t;i++)
	{
		double c,f,x;
		cin>>c>>f>>x;
		double coki=0;
		double rate=2;
		double time=0;
		while(coki<x)
		{
			double tem1=(c-coki)/rate;
			double tem2=x/(rate+f);
			double t=(x-coki)/rate;
			if(t<(tem1+tem2))
			{
				time+=t;
				break;
			}
			else
			{
				time+=tem1;
				coki=0;
				rate+=f;
			}
		}
		cout<<"Case #"<<i+1<<": ";
		cout << std::fixed;
   		cout.precision(7);
   		cout<<time<<endl;
	}
	return 0;
}
