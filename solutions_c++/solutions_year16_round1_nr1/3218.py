#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
#include <deque>
#include <algorithm>

using namespace std;



int main()
{
	ifstream f("A-large.in", std::ios::in);
	int t;
	f >> t;	
	string s;
	getline(f, s);
	deque<char> d;
	for (int i = 0; i < t; i++)
	{
		getline(f, s);
		d.push_back(s.front());
		for (int i = 1; i < s.size(); i++)
		{
			if (s[i] >= d.front())
				d.push_front(s[i]);
			else
				d.push_back(s[i]);
		}
		cout << "Case #" << i + 1 << ": ";
		for (auto it : d)
			cout << it;
		cout << endl;
		d.clear();
	}


	return 0;
}