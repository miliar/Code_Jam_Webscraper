
#include<iostream>
#include<fstream>
#include<string>
#include<string.h>
#include<vector>

using namespace std;



int mincheck(vector<int> people);

int main(int agrc, char* agrv[])
{

	
	ifstream in("A-large.in");
	ofstream out("A-large.out");

	
	int testCase;
	in >> testCase;
	for (int t = 0; t < testCase;++t) 
	{
		int s;
		string str;
		in >> s >> str;
		vector<int> people;
		people.resize(s + 1);
		for (int i = 0; i < s + 1; ++i)
		{
			people[i] = atoi(str.substr(i, 1).c_str());
		}
		out << "Case #" << t + 1 << ": " << mincheck(people) << endl;
		
	}

	in.close();
	out.close();

	return 0;
}


int mincheck(vector<int> people)
{
	int min = 0;
	int sum = 0;

	for (int i = 0; i < people.size() - 1; ++i)
	{
		sum += people[i];
		if (sum + min > i)
		{

		}
		else
		{
			min += i + 1 - (sum+min);
		}
	}

	return min;
}
