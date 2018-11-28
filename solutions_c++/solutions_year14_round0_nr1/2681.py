#include <iostream>
#include <fstream>
#include <set>
#include <algorithm>
#include <iterator>
using namespace std;

char const * badMagi = "Bad magician!";
char const * volcheated =  "Volunteer cheated!";
ofstream output("D:\\out.txt");

int main()
{
	ifstream file;
	file.open("D:\\in.txt");
	int counter;
	char in[8];
	file >> in;
	counter = atoi(in);

	int testnum = 1;
	//output << "Case #" << testnum << ": " << badMagi << endl;
	//output << "Case #" << testnum << ": " << volcheated << endl;
	//output << "Case #" << testnum << ": " << (testnum) << endl;
	while (!file.eof())
	{
		std::set<int> deck1;
		std::set<int> deck2;
		deck1.clear();
		deck2.clear();
		int firstrownum;
		int secondrownum;
		file >> firstrownum;
		for (int i = 0; i < 4; ++i)
		{
			if (i + 1 == firstrownum)
			{
				int arr[4];
				int num;
				for (int j = 0; j < 4; ++j)
				{			
					file >> num;
					arr[j] = num;
				}
				deck1.insert(arr, arr + 4);
				
				
			}
			else
			{
				int num;
				for (int j = 0; j < 4; ++j)
				{
					file >> num;
				}
			}
		}
		file >> secondrownum;
		for (int i = 0; i < 4; ++i)
		{
			if (i + 1 == secondrownum)
			{
				int arr[4];
				int num;
				for (int j = 0; j < 4; ++j)
				{
					file >> num;
					arr[j] = num;
				}
				deck2.insert(arr, arr + 4);
				

			}
			else
			{
				int num;
				for (int j = 0; j < 4; ++j)
				{
					file >> num;
				}
			}
		}
		
		set<int> intersect;
		std::set_intersection(deck1.begin(), deck1.end(), deck2.begin(), deck2.end(),
			std::inserter(intersect, intersect.begin()));
		if (intersect.empty())
		{
			output << "Case #" << testnum << ": " << volcheated << endl;
		}
		else if (intersect.size() == 1)
		{
			output << "Case #" << testnum << ": " << *(intersect.begin()) << endl;
		}
		else if (intersect.size() > 1)
		{
			output << "Case #" << testnum << ": " << badMagi << endl;
		}

		testnum++;
		if (counter+1 == testnum)
			break;
	}
	return 0;
}