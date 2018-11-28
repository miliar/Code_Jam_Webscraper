#include <bits/stdc++.h>

using namespace std;

int test;
string s;

int main ()
	{
		ios :: sync_with_stdio(false);
		cin.tie(0);

		cin >> test;

		int t = test;

		while (test--)
			{
				cout << "Case #" << t - test << ": ";
				cin >> s;

				deque <char> mydeque;

				mydeque.clear();

				deque <char> :: iterator it;

				mydeque.push_back(s[0]);

				for (int i = 1; i < s.size(); i++)
					{
						it = mydeque.begin();

						if (s[i] >= *it) mydeque.push_front(s[i]);
							else mydeque.push_back(s[i]);
					}

				for (it = mydeque.begin(); it != mydeque.end(); it++)
					cout << *it;

				cout << "\n";
			}
		return 0;
	}
