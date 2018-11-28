#include <bits/stdc++.h>
using namespace std;
int main()
{
	int t, x=0;
	cin >> t;
	while(t--)
	{
		x++;
		string s;
		cin >> s;
		int l=s.length();
		list<char> y;
		y.push_back(s[0]);
		list<char>::iterator it=y.begin();
		for(int i=1; i<l; i++)
		{
			if(s[i]>=*it)
				{
					y.push_front(s[i]);
					it=y.begin();
				}
			else
				y.push_back(s[i]);
		}
		cout << "Case #" << x << ": " ;
		for(it=y.begin(); it!=y.end(); it++)
			cout << *it;
		cout << "\n";
	}
	
	return 0;
}