#include <iostream>
#include <fstream>
#include <cstdlib>
#include <vector>
#include <iomanip>

using namespace std;

typedef long double ld;

ld minimize_time(ld init_rate, ld cookies_needed, ld current_cookies, ld farm_cost, ld farm_production)
{
	if(current_cookies >= cookies_needed || max(farm_cost-current_cookies, 0.0L) >= max(cookies_needed-current_cookies, 0.0L))
	{
		return max((cookies_needed-current_cookies)/init_rate,0.0L);
	}
	else
	{
		ld time_to_build = max(0.0L, (farm_cost-current_cookies)/init_rate);
		if(time_to_build + (cookies_needed-(current_cookies-farm_cost)-time_to_build*init_rate)/(init_rate+farm_production) < (cookies_needed-current_cookies)/init_rate)
		{
			return time_to_build + minimize_time(init_rate+farm_production, cookies_needed, current_cookies+time_to_build*init_rate-farm_cost, farm_cost, farm_production);
		}
		else
		{
			return max((cookies_needed-current_cookies)/init_rate,0.0L);
		}
	}

}

int main()
{
	ifstream fin("cookieclicker.in");
	int T;
	fin>>T;

	ofstream fout("cookieclicker.out");

	for(int i=0;i<T;i++)
	{
		fout<<"Case #"<<(i+1)<<": ";
		ld C,F,X;
		fin>>C>>F>>X;
		fout<<setprecision(20)<<minimize_time(2.0L,X,0.0L,C,F)<<endl;
	}

	return 0;
}
