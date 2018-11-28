#include <iostream>
#include <algorithm>
#include <stdio.h>
#include <cstdlib>
#include <string>
#include <string.h>
#include <deque>
using namespace std;
int main(){
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	for(int o = 1; o <= t; o++)
	{
		string s, ans;
		deque<char> d;
		cin >> s;
		int f = -1;
		for(int i = 0; i < s.size(); i++)
		{
			if(f == -1)
			{
				d.push_front(s[i]);
				f = int(s[i]);
			}
			else
			{
				if(f <= int(s[i]))
				{
					d.push_front(s[i]);
					f = int(s[i]);
					// Forwards
				}
				else
				{
					d.push_back(s[i]);
				}
			}
		}
		cout << "Case #"<< o << ": ";
		while(!d.empty())
		{
			char b = d.front();
			cout << b;
			d.pop_front();
		}
		cout << endl;
	}
	return 0;
}