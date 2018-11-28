#include <iostream>
#include <iomanip>
#include <cstdio>
using namespace std;
int main()
{

	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t;
	cin>>t;
	for(int testCase = 1; testCase<=t;testCase++)
	{
		double c,f,x;
		cin>>c>>f>>x;
		double timePassed = 0;
		double currentRate = 2;
		double left = x;
		double best = 2000000000;
		for(int i=0; ;i++)
		{
			double time = left / currentRate;
			if(time + timePassed<best )
			{
				best = time+timePassed;
			}
			else
			{
				break;
			}

			timePassed += c / currentRate;
			currentRate += f;
		}
		cout<<"Case #"<<testCase<<": ";
		//cout<<setprecision(7)<<best<<endl;
		printf("%.8lf\n",best);

	}
	return 0;
}