#include <iostream>
#include <string>
#include<math.h>
#include<iomanip>
#include<vector>
#include<set>
#include<algorithm>
using namespace std;
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int t;
	
	cin>>t;
	double c,f,x;
	for(int i=0;i<t;i++)
	{
		cin>>c>>f>>x;
		double rate=2;
		double seconds=0;
		double cookies=0;

		while(true)
		{
			cookies+=min(x,c);
			seconds+=min(x,c)/rate;
			if(cookies==x)
				break;
			if( (x-cookies)/rate > x/(rate+f)  )
			{
				rate+=f;
				cookies=0;
			}
			else
			{
				cookies+=(x-c);
				seconds+=(x-c)/rate;
				break;
			}
		}
		cout<<"Case #"<<i+1<<": "<<setprecision(10)<<seconds<<endl;

	}
	return 0;
}
