#include<iostream>

using namespace std;

void doit(int casenum)
{
	double C,F,X;
	cin>>C>>F>>X;
	double t=0;
	int n=0;
	double cookie_to_do = X;
	while(true)
	{
		double time_remain = cookie_to_do/(n*F+2);
		double one_farm_time_cost = C/(n*F+2);
		double plus_one_time_remain = one_farm_time_cost+ (cookie_to_do)/((n+1)*F+2);
		if(time_remain>=plus_one_time_remain)
		{
			++n;
			t+=one_farm_time_cost;
			
		}else
		{
			cout<<"Case #"<<casenum<<": "<<t+time_remain<<endl;
			break;
		}
	}
}

int main()
{
	int t;
	std::cout.precision(10);
	freopen ("myfile.txt","w",stdout);

	cin>>t;
	for(int i=1;i<=t;++i)
	{
		doit(i);
	}
	return 0;
}