#include <cstdio>
#include <cmath>
#include <cstring>
#include <ctime>
#include <iostream>
#include <algorithm>
#include <set>
#include <vector>
#include <sstream>
#include <typeinfo>
#include <fstream>
#include <deque>

using namespace std;
// #define INPUT_FILE

bool comp(const double &a, const double &b)
{
	return a>b;
}

int main(int argc, char const *argv[])
{
	#ifdef INPUT_FILE
	    freopen("D-large.in", "r", stdin);
	#endif
	int t;
	scanf("%d", &t);
	int n = t;
	while(t--)
	{
		int N;
		scanf("%d", &N);
		std::deque<double> Naomi(N);
		std::deque<double> Ken(N);
		for (int i = 0; i < N; ++i)
			scanf("%lf", &Naomi[i]);
		for (int i = 0; i < N; ++i)
			scanf("%lf", &Ken[i]);
		sort(Naomi.begin(), Naomi.end(),comp);
		sort(Ken.begin(), Ken.end(),comp);
		deque<double> Nwar(Naomi.begin(), Naomi.end());
		deque<double> Kwar(Ken.begin(), Ken.end());
		int war = 0;
		for (int i = 0; i < N; ++i)
		{
			if(Nwar.front() > Kwar.front())
			{
				war++;
				Nwar.pop_front();
				Kwar.pop_back();
			}
			else
			{
				bool flag = false;
				for (int j = 0; j < Kwar.size(); ++j)
				{
					if(Kwar[j] < Nwar.front())
					{
						Kwar.erase(Kwar.begin() + j-1);
						flag = true;
						break;
					}
				}
				if(!flag)
					Kwar.pop_back();
				Nwar.pop_front();
			}
		}
		int dwar = 0;
		for (int i = 0; i < N; ++i)
		{
			if(Naomi.back() > Ken.back())
			{
				dwar++;
				Naomi.pop_back();
				Ken.pop_back();
			}
			else
			{
				Ken.pop_front();
				Naomi.pop_back();
			}
		}
		printf("Case #%d: %d %d\n", n-t, dwar, war);
	}
	return 0;
}
