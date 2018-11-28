/*
 E-Mail : makiolo@gmail.com
 Twitter: @makiolo

 Yeah Nigga
 */

#define EXERCISE "B"
//#define SHOW_IN_SCREEN
//#define WORK_WITH_SMALL
//#define USE_EXAMPLE
#define FILENAME(file_name) EXERCISE ## "-" ## file_name

#include <cstring>
#include <string.h>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <list>
#include <assert.h>

typedef double Real;

template <typename T>
void get_from_cin(T& output)
{
	std::string buffer;
	std::cin >> buffer;

	std::istringstream ss(buffer);
	bool ok = (ss >> output);
	if(!ok)
	{
		std::cerr << "Error from input, expected type " << typeid(T).name() << std::endl;
		exit(1);
	}
}

void get_from_cin_full(std::string& output)
{
	std::getline(std::cin, output);
}

template<typename T>
void split(const T& str, const T& delimiters, std::vector<T>& v)
{
	T::size_type start = 0;
	auto pos = str.find_first_of(delimiters, start);
	while(pos != T::npos) {
		if(pos != start) // ignore empty tokens
			v.emplace_back(str, start, pos - start);
		start = pos + 1;
		pos = str.find_first_of(delimiters, start);
	}
	if(start < str.length()) // ignore trailing delimiter
		v.emplace_back(str, start, str.length() - start); // add what's left of the string
}

struct PrintGoogleCase
{
	PrintGoogleCase(int i)
	{
		std::cout << "Case #" << i << ":";
	}

	~PrintGoogleCase()
	{
		std::cout << std::endl;
	}
};

int main()
{
#ifdef USE_EXAMPLE
	freopen(FILENAME("example.in"),"rt", stdin);
#ifndef SHOW_IN_SCREEN
	freopen(FILENAME("example.out"),"wt", stdout);
#endif
#else
#ifdef WORK_WITH_SMALL 
	freopen(FILENAME("small-practice.in"),"rt", stdin);
#ifndef SHOW_IN_SCREEN
	freopen(FILENAME("small-practice.out"),"wt", stdout);
#endif
#else
	freopen(FILENAME("large-practice.in"),"rt", stdin);
#ifndef SHOW_IN_SCREEN
	freopen(FILENAME("large-practice.out"),"wt", stdout);
#endif
#endif
#endif
	
	int N;
	get_from_cin(N);
	get_from_cin_full(std::string());
	
	for(int i=0; i<N; ++i)
	{
		Real cost;
		get_from_cin(cost);

		Real income_increase;
		get_from_cin(income_increase);

		Real objetive;
		get_from_cin(objetive);
		get_from_cin_full(std::string());

		/*
		cost = 30.50000;
		income_increase = 3.14159;
		objetive = 1999.19990;
		*/
		/*
		cost = 500.0;
		income_increase = 100.0;
		objetive = 750.0;

		cost = 500.0;
		income_increase = 4.0;
		objetive = 2000.0;
		*/
		/*
		cost = 30.0;
		income_increase = 1.0;
		objetive = 2.0;
		*/
		/*
		cost = 387.00000;
		income_increase = 2.00000;
		objetive = 774.00000;
		*/

		Real money = 0.0;
		Real income = 2.0;
		Real time = 0.0;

		Real time_total_now = 999999999.0f;
		Real time_total_prev;

		bool exit = false;
		bool prev_was_best = false;
		while(!exit)
		{
			time_total_prev = time_total_now;
			time_total_now = time + (objetive / income);

			prev_was_best = (time_total_now > time_total_prev);
			if(prev_was_best)
			{
				// rollback
				time = time_total_prev;
				money = objetive;
			}
			else
			{
				Real time_wait_objetive = objetive / income;
				Real time_wait_buy = cost / income;
				if((time_wait_buy < time_wait_objetive))
				{
					time += time_wait_buy;
					income += income_increase;
				}
				else
				{
					money += (income * time_wait_objetive);
					time += time_wait_objetive;
				}
			}

			exit = (money >= objetive);
		}

		{
			PrintGoogleCase aux(i + 1);

			printf(" %.7f", time);
			//std::cout << " " << time;
		}
		

	}
	return 0;
}

