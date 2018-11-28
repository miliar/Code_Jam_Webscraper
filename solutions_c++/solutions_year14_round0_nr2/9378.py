#include <iostream>
#include <vector>
using namespace std;


class Cookies
{
	public:

	

	void load()
	{
		times.clear();
		farms_cost.clear();
		num_farms = 0;
		time = 0;
		rate = 2;
		cin>>farm_cost;
		cin>>farm_rate;
		cin>>goal;		
	}	

	double farm_cost;
	double rate;

	void find_times()
	{
		if(times.size() == 0 )
		{
			times.push_back(goal/rate);
			farms_cost.push_back(0);
		}
		else
		{
			farms_cost.push_back(farms_cost[farms_cost.size() -1 ] + farm_cost / rate);
			rate+=farm_rate;
			times.push_back(farms_cost[farms_cost.size()-1] + goal/rate);
		}
	}

	bool solved()
	{
		if(times.size() < 2)
			return false;
		else
			return times[times.size() -1] > times[times.size() -2];
	}

	double answer()
	{
		return times[times.size() -2];
	}

	void print_tables()
	{
		for( int i= 0; i < times.size(); i++)
			cout<<i<<" : "<<times[i]<<"\t"<<farms_cost[i]<<endl;
	}

	double goal;
	double time;
	int num_farms;
	double farm_rate;


	vector<double> times;
	vector<double> farms_cost;

};


int main ()
{
	Cookies prob;
	int icase = 0;
	int ncase;
	cout.setf(ios::fixed);
	cout.setf(ios::showpoint);
	cout.precision(7);
	cin>>ncase;
	for(icase;icase<ncase;icase++)
	{
		prob.load();
		while (!prob.solved())
		{
			prob.find_times();			
		}
		cout<<"Case #"<<icase<<": "<<prob.answer()<<endl;
	}
}
