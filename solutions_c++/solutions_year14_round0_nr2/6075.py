#include <iostream>
#include <iomanip>
#include <fstream>
using namespace std;

int main()
{
	freopen("cca.in","r",stdin);
	freopen("cca.out","w",stdout);
	int T;
	cin>>T;
	for(int id=1;id<T+1;id++)
	{
		double c,f,x;
		cin>>c>>f>>x;
		double rate=2,sum=0;
		double total=0;
		if (x<=c) 
		{
			cout<<setiosflags(ios::fixed);
			cout.precision(7); 
			cout <<"Case #"<<id<<": "<<x/rate<<endl;
			continue;
		}
		total+=c/rate;
		sum += c;
		while ( (x-sum)*f >= rate*c )
		{
			sum -=c;
			rate += f;
			total+=c/rate;
			sum+=c;
		}
		total+=(x-sum)/rate;
		cout<<setiosflags(ios::fixed);
		cout.precision(7); 
		cout <<"Case #"<<id<<": "<<total<<endl;
	}
}