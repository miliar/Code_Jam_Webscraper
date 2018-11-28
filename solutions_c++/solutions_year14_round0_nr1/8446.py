/*
 E-Mail : makiolo@gmail.com
 Twitter: @makiolo

 Yeah Nigga
 */

#define EXERCISE "A"
//#define SHOW_IN_SCREEN
#define WORK_WITH_SMALL
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

void read_matrix( std::vector<int> &matrix, int row) 
{
	for(int j=1; j<=4; ++j)
	{
		for(int k=1; k<=4; ++k)
		{
			int P;
			get_from_cin(P);
			if(j == row)
				matrix.push_back(P);
		}
		get_from_cin_full(std::string());
	}
}

template <typename T>
std::vector<T> instersection(std::vector<T> &v1, std::vector<T> &v2)
{
	std::vector<T> v3;

	std::sort(v1.begin(), v1.end());
	std::sort(v2.begin(), v2.end());

	std::set_intersection(v1.begin(),v1.end(),v2.begin(),v2.end(),back_inserter(v3));

	return v3;
}

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
		int first;
		get_from_cin(first);
		get_from_cin_full(std::string());

		std::vector<int> first_matrix;
		read_matrix(first_matrix, first);


		int second;
		get_from_cin(second);
		get_from_cin_full(std::string());

		std::vector<int> second_matrix;
		read_matrix(second_matrix, second);

		{
			PrintGoogleCase aux(i + 1);

			std::vector<int> common = instersection(first_matrix, second_matrix);
			if(common.size() == 1)
			{
				std::cout << " " << common[0];
			}
			else if(common.size() == 0)
			{
				std::cout << " Volunteer cheated!";
			}
			else
			{
				std::cout << " Bad magician!";
			}
		}
		

	}
	return 0;
}
