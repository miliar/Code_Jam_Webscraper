#include <iostream>
#include <vector>
#include <fstream>
#include <algorithm>
using namespace std;

int solve(string & s)
{
	unsigned int count(0);
	vector<bool> bin;
	for(int i = 0;
		i < s.size();
		++i)
	{
		if(s[i] == '+')
			bin.push_back(1);
		else
			bin.push_back(0);
	}
	reverse(bin.begin(), bin.end());
	vector<bool>::iterator index;
	
	while(1)
	{

		for(vector<bool>::iterator i = bin.begin();
			i != bin.end();
			++i)
		{
			index = i;
			++index;
			if(*i == 0)
			{

				++count;
				bin.flip();
				bin.erase(bin.begin(), i);
				if(bin.empty())
					{cout << "EMPTY" << endl; return count;}
				break;
			}
			if(index == bin.end() && *i == 1)
				return count;
		}
	}
	return -1;	
}


int main()
{
	ifstream fin("q.txt");
	unsigned long int cases(0), i(0), j(1);
	string input;
	fin >> cases;
	while(cases>0)
	{
		fin >> input;
		i = solve(input);
		cout << "Case #" << j << ": " << i << endl;
		--cases;
		++j;
	}
	return 0;
}
