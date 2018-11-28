#include<iostream>
#include<vector>
#include<fstream>
#define ll long long
using namespace std;

class Tracker
{
	vector<bool>has;
	int rem;
	
	public:
	Tracker()
	{
		has.resize(10,false);
		rem = 10;
	}
	
	void mark(ll n)
	{
		while(n)
		{
			int d = n%10;
			n/=10;
			if(!has[d])
			{
				has[d] = true;
				rem--;
			}
		}
	}
	
	bool done()
	{
		return (rem == 0);
	}
};

int main()
{
	int T;
	ifstream fin("A-large.in");
	ofstream fout("A-large.out");
	
	fin>>T;
	int c = 1;
	while(T--)
	{
		ll n;
		ll N;
		
		fin>>n;
		N=n;
		if(n==0)
		{
			fout<<"Case #"<<c<<":"<<" INSOMNIA"<<endl;
			c++;
			continue;
		}
		Tracker tracker;
		while(!tracker.done())
		{
			tracker.mark(N);
			
			if(tracker.done())
				break;
			N+=n;
		}
		fout<<"Case #"<<c<<":"<<" "<<N<<endl;
		c++;
	}
	return 0;
}
