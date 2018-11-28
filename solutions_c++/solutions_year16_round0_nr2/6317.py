#include<iostream>
#include<string>
#include<stack>
#include<fstream>
using namespace std;
int cakes[100], s;
bool flip(string s)
{
	int PC=0, NC = 0,counter=0;
	bool flag = false;
	int first = cakes[0];
	for (int i = 0; i < s.length(); i++)
	{
		if (cakes[i] != first) break;
		counter++;
	}
	if (first == 1 && counter == s.length()) return true;
	stack<int> stck;
	for (int i = 0; i < counter; i++)
	{
		stck.push(1 - cakes[i]);
	}
	int m = 0;
	while (!stck.empty())
	{
		cakes[m++] = stck.top();
		stck.pop();
	}
	for (int i = 0; i < s.length(); i++)
	{
		if (cakes[i] == 0)
			return false;
	}
	return true;
}
int main()
{
	ifstream input("B-small-attempt0.in");
	ofstream output("output.out");
	int t,x=1;
	input >> t;
	while (t--)
	{
		string s;
		input >> s;
		for (int i = 0; i < s.length(); i++)
		{
			cakes[i] = s[i] == '+' ? 1 : 0;
		}
		int counter = 0,PS=0;
		for (int i = 0; i < s.length(); i++)
		{
			if (cakes[i] == 1)
				PS++;
		}
		if (PS != s.length())
		{
			while (!flip(s))
			{
				counter++;
			}
			counter++;
		}
		output << "Case #" << x++ << ": " << counter << endl;
	}
}