#include <iostream>
#include <string>
#include <list>
using namespace std;
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t, i, l, j;
	string s;
	cin >> t;
	for(i = 1; i <= t; i++)
	{
		list<char> result;
		cin >> s;
		result.push_back(s[0]);
		l = s.size();
		for(j = 1; j < l; j++)
			if(s[j] >= result.front())
				result.push_front(s[j]);
			else
				result.push_back(s[j]);
		cout << "Case #" << i << ": ";
		list<char>::iterator it;
		for(it = result.begin(); it != result.end(); it++)
			cout << *it;
		cout << endl;
	}
}
