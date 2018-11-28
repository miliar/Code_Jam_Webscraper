#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

#define FILE_NAME "A-small"

using namespace std;

int main()
{
	freopen(FILE_NAME ".in", "r", stdin);
	freopen(FILE_NAME ".out", "w", stdout);

	int numTestCaces = 0;
	cin >> numTestCaces;
	for(int Case = 1; Case <= numTestCaces; ++Case)
	{
		set<int> s1, s2;
		int first;
		cin >> first;
		for(int i = 0; i < 4; ++i)
		{
			int a,b,c,d;
			cin >> a >> b >> c >> d;
			if(i + 1 == first)
			{
				s1.insert(a);
				s1.insert(b);
				s1.insert(c);
				s1.insert(d);
			}
		}
		cin >> first;
		for(int i = 0; i < 4; ++i)
		{
			int a,b,c,d;
			cin >> a >> b >> c >> d;
			if(i + 1 == first)
			{
				if(s1.count(a))
					s2.insert(a);
				if(s1.count(b))
					s2.insert(b);
				if(s1.count(c))
					s2.insert(c);
				if(s1.count(d))
					s2.insert(d);
			}
		}
		cout << "Case #" << Case << ": ";
		if(s2.size() > 1)
			cout << "Bad magician!" << endl;
		else if(s2.size() < 1)
			cout << "Volunteer cheated!" << endl;
		else
			cout << *s2.begin() << endl;
	}

	return 0;
}
