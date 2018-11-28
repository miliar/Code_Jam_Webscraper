#include <cstdio>
#include <iostream>
#include <map>
#include <vector>
#include <string>
#include <set>
#include <queue>
#include <list>
using namespace std;

#define MOD 1000002013

int main()
{
	int t;
	cin >> t;
	for(int i=1;i<=t;i++)
	{
		int n,m;
		cin >> n >> m;
		
		//<station, delta>
		long long real_cost = 0;
		map<int, long long> data;
		while(m--)
		{
			long long o,e,p;
			cin >> o >> e >> p;
			
			if(e>o)
			{
				long long stations = e-o;
				long long cost = p * (stations * n - ((stations)*(stations-1))/2);
				//printf("cost of this = %lld\n", cost);
				real_cost += cost;
				real_cost %= MOD;
			}
			data[o] += p;
			data[e] -= p;
		}
		
		long long min_cost = 0;
		
		while(data.size())
		{
			long long current = 0;
			long long carry = 0;
			for(auto it = data.begin(); it!=data.end(); it++)
			{
				//printf("ST %d, delta=%lld\n", it->first, it->second);
				if(current==0)
				{
					carry = it->second;
					//printf("Starting from %d, carrying %lld people\n", it->first, carry);
				}
				current += it->second;
				if(current==0)
				{
					//printf("Finishing at %d, carried %lld people\n", it->first, carry);
					long long stations = it->first - data.begin()->first;
					long long cost = carry * (stations * n - ((stations)*(stations-1))/2);
					//printf("It costed %lld\n", cost);
					min_cost += cost;
					min_cost %= MOD;
					
					if(it->second==carry)
					{
						data.erase(it);
					}
					else
					{
						it->second += carry;
					}
					
					auto itf = data.begin();
					if(itf->second==carry)
					{
						//printf("finished start\n");
						data.erase(data.begin());
					}
					else
					{
						//printf("delted start\n");
						data.begin()->second -= carry;
					}
					break;
				}
				else if(current<carry)
				{
					carry = current;
					//printf("Carrying only %lld people from station %d\n", carry, it->first);
				}
				//printf("%lld after station %d\n", current, it->first);
			}
		}
		
		printf("Case #%d: %lld\n", i, real_cost-min_cost);
	}
}
