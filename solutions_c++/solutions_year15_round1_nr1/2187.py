#include <iostream>

// #include "Sort.h"

#include <math.h>

#include <list>
#include <vector>
#include <deque>
#include <functional>
#include <fstream>

using namespace std;

typedef deque<int> Container;



static int FillContainer(Container &container, int size, int maxVal)
{
	container.clear();

	int i = 0;
	for (i = 0; i < size; ++i)
	{
		container.push_back( rand() % maxVal );
	}

	return container.size();
}


static void PrintContainer(Container &container)
{
	for each (auto iter in container)
	{
		cout << iter << ' ';
	}
}

typedef vector<int> List;

static int getEatenMushrooms1(List &lst)
{
	List::iterator	begin = lst.begin(),
					end = lst.end();
	int step = 0;	// 0 - eating
					// 1 - placing
	int eaten = 0;

	if (begin == end)
		return 0;

	while (begin + 1 != end)
	{
		if (*(begin + 1) < *begin)
			eaten += *begin - *(begin + 1);

		++begin;
	}


	return eaten;
}

static int getEatenMushrooms2(List &lst)
{
	List::iterator	begin = lst.begin(),
					end =   lst.end();
	int step = 0;	// 0 - eating
	// 1 - placing
	int eaten = 0;

	if (begin == end)
		return 0;

	int maxDiff = 0;
	while (begin+1 != end)
	{
		if (*begin > *(begin + 1))
		{
			int diff = *begin - *(begin + 1);
			if (maxDiff < diff)
				maxDiff = diff;
		}

		++begin;
	}

	begin = lst.begin();
	while (begin + 1 != end)
	{
		eaten += (*begin > maxDiff) ? maxDiff : *begin;

		++begin;
	}

	return eaten;
}




int main()
{
	List listOfMushrooms;
	listOfMushrooms.reserve(10000);

	ifstream input( "D:\\A-large.in" );
	ofstream output("D:\\output.txt");

	int countOfTests;
	input >> countOfTests;

	
	for (int i = 0; i < countOfTests; ++i)
	{
		int countOfMushrooms;
		input >> countOfMushrooms;

		listOfMushrooms.clear();
		for (int j = 0; j < countOfMushrooms; ++j)
		{
			int mushrooms = 0;
			input >> mushrooms;
			listOfMushrooms.push_back(mushrooms);
		}

		int y = getEatenMushrooms1(listOfMushrooms);
		int z = getEatenMushrooms2(listOfMushrooms);
		output << "Case #" << i + 1 << ": " << y << ' ' << z << endl;
		
	}
	

	input.close();
	output.close();

	return 0;
}