#include<iostream>
#include<vector>
#include<set>
using namespace std;
int main()
{
	int t;
	cin>>t;
	double c,f,x;
	for(int cs = 1; cs <=t ;cs++)
	{
		cin>>c>>f>>x;
		double sum=0.0;
		double rate = 2;
		while(true)
		{
			if((x/rate) > ( (c/rate) + (x/(rate+f)) ) )
			{
				sum += (c/rate);
				rate += f;
			}
			else
			{
				sum += (x/rate);
				break;
			}
		}
		printf("Case #%d: %.7f",cs,sum);
		cout<<endl;
		//cout<<"Case #"<<cs<<": "<<<<endl;
	}
	return 0;
}