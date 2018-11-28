#include <algorithm>
#include <bitset>
#include <cassert>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <fstream>
#include <functional>
#include <iostream>
#include <limits>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <random>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <tuple>
#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <utility>

using namespace std;

int main()
{
	unsigned T;
	cin >> T;
	for (unsigned it = 0; it < T; ++it)
	{
		cout << "Case #" << it + 1 << ": ";
		string s;
		cin >> s;
		stack<char> st;
		unsigned score = 0;
		for (unsigned i = 0; i < s.size(); ++i)
		{
			if (st.empty()) st.push(s[i]);
			else
			{
				if (st.top() == s[i])
				{
					st.pop(); score += 10;
				}
				else
				{
					st.push(s[i]);
				}
			}
		}
		unsigned sl = 0;
		for (; !st.empty(); st.pop()) ++sl;
		score += 5 * (sl / 2);
		//if (sl & 1)
		//{
		//	score += 10 * sl / 2;
		//}
		//else if (sl == 0)
		//{
		//}
		//else if (sl == 2)
		//{
		//	score += 5;
		//}
		//else
		//{
		//	score += 10 * (sl - 2) / 2;
		//}
		cout << score << endl;
	}
	return 0;
}
