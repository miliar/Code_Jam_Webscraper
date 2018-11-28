#include<iostream>

using namespace std;

int main()
{
	int t;
	cin>>t;
	for(int p=0;p<t;p++)
	{
		double c,f,x;
		cin>>c>>f>>x;
		double cookie=0;
		double r=2;
		double time=0;
		while(cookie<x)
		{
			double temp1=(c-cookie)/r;
			double temp2=x/(r+f);
			double temp3=(x-cookie)/r;
			if(temp3<(temp1+temp2))
			{
				time+=temp3;
				break;
			}
			else
			{
				time+=temp1;
				cookie=0;
				r+=f;
			}
		}
		cout<<"Case #"<<p+1<<": ";
		cout << std::fixed;
   		cout.precision(7);
   		cout<<time<<endl;
	}
	return 0;
}