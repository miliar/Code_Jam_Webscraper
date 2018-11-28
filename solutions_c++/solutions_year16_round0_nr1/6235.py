#include<iostream>
#include<string>
#include<sstream>
#include<fstream>
using namespace std;
int NUMS[10];
bool check(int x)
{
	string s;
	stringstream convert;
	convert << x;
	s = convert.str();
	for (int i = 0; i < s.length(); i++)
	{
		NUMS[s[i] - '0'] = 1;
	}
	for (int i = 0; i < 10; i++)
	{
		if (NUMS[i] == 0)
			return false;
	}
	return true;
}
int main()
{
	ifstream input("A-small-attempt0.in");
	ofstream output("output.out");
	int t,n,counter=1;
	input >> t;
	while (t--)
	{
		memset(NUMS, 0, sizeof(NUMS));
		input >> n;
		if (n == 0)
		{
			output <<"Case #"<<counter++<< ": INSOMNIA" << endl;
		}
		else
		{

			int i = 1;
			while (!check(n*i++));
			output << "Case #" << counter++ << ": " << (i-1)*n << endl;
		}

	}
	return 0;
}