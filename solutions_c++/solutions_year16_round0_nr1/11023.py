#include <iostream>
#include <fstream>
#include <string>
#include <stdlib.h> 
#include <vector>
#include <algorithm>
#include <sstream>
using namespace std;



string to_string(int i)
{
    std::stringstream ss;
    ss << i;
    return ss.str();
}

void function()
{
	ifstream input;
	input.open("A-large.in");
	string str;
	input>>str;
	int entries = atoi(str.c_str());
	ofstream output;
	output.open("result.txt");
	for (int i=0;i<entries;i++)
	{
		int mul = 2;
		vector<int> temp;
		input>>str;
		int size = str.length();
		int number = atoi(str.c_str());
		int original = number;
		if (number == 0)
		{
			output<<"Case #"<<i+1<<": "<<"Insomnia"<<endl;
			continue;
		}

		for (int j= 0 ; j<size;j++)
		{
			if (find(temp.begin(), temp.end(), str[j]) == temp.end() )
			{
				temp.push_back(str[j]);
			}
		}
		while (temp.size()<10)
		{
			number = original * mul;

			str = to_string(number);
			size = str.length();
			for (int j= 0 ; j<size;j++)
			{
				if (find(temp.begin(), temp.end(), str[j]) == temp.end() )
				{
					temp.push_back(str[j]);
				}
			}

			mul++;

		}

		output<<"Case #"<<i+1<<": "<<str<<endl;
		temp.clear();

	}
}

int main()
{
	function();
}