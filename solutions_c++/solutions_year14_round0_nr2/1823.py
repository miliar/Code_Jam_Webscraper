#include <iostream>
#include <fstream>
#include <iomanip>
using namespace std;

int main(void)
{
	int test,count=0,farm=0;
	double c,f,x;
	double best,value,current;
	//ofstream cout("ansB.out");
	//ifstream cin("B-large.in");
	cin>>test;
	while(count++<test)
	{
		cin>>c>>f>>x;
		best=x/2;
		current=0;
		value=0;
		farm=0;
		while(true)
		{
			if(current>=best)
				break;
			value=current+x/(2+farm*f);
			if(value<best)
				best=value;
			current+=c/(2+farm*f);
			farm++;
		}
		cout<<fixed<<setprecision(7);
		cout<<"Case #"<<count<<": "<<best<<endl;
	}
	return 0;
}