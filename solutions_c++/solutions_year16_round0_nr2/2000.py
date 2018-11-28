#include <fstream>
#include <iostream>
#include <string>
#include <queue>
#include <map>

using namespace std;

int LinearAlgorithm(string s)
{
	int cnt = 0;
	while(s.size() > 0 && s.back() == '+')
	{
		s.pop_back();
	}
	for(int i = 0, n = s.size(); i < n; i++)
	{
		if(i == 0 || s[i] != s[i - 1])
		{
			cnt++;
		}
	}
	return cnt;
}

int main()
{
	int t;
	string s;
	ifstream f("input.txt");
	ofstream g("output.txt");
	f >> t;
	for(int i = 1; i <= t; i++)
	{
		f >> s;
		g << "Case #" << i << ": " << LinearAlgorithm(s) << endl;
	}
	f.close();
	g.close();
	return 0;
}
