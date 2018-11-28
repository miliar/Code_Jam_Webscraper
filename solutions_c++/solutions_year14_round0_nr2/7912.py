#include <iostream>
#include<fstream>
#include<iomanip>
using namespace std;

int main()
{
	ifstream fin;
	ofstream fout;
	fout.open("Cookie_Answer.in");
	fin.open("B-large.in");
	long q,test;
	long double farm_cost,cookies_per,min_cookie,rate,time;
	long double temp,temp1;
	fin>>test;
	fout << setiosflags(ios::fixed | ios::showpoint)<< setprecision(7);
	for(q=0;q<test;q++)
	{
		fin>>farm_cost;
		fin>>cookies_per;
		fin>>min_cookie;
		rate = 2.0;
		time = 0.0;
		while(true)
		{
			temp = min_cookie/rate;
			temp1 = (farm_cost/rate) + (min_cookie/(rate + cookies_per));
			if(temp<=temp1)
				break;
			time = time + farm_cost/rate;
			rate = rate + cookies_per;
		}
		time = time + min_cookie/rate;
		fout<<"Case #"<<q+1<<": "<<time<<"\n";
	}
	fin.close();
	fout.close();
	return 0;
}
