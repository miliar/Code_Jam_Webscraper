#include <iostream>
#include <string>
#include <cmath>
#include <stack>
#include <deque>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <iomanip>

using namespace std;

int main()
{
	int T = 0;
	cin >> T;

	for (long long i = 1; i <= T; i++ )
	{
		long long N = 0;
		string str = "";
		cin >> str;

		stack <char> st;
		int stringSize = str.size() - 1;
		while(stringSize >= 0)
		{
			if(!st.empty())
			{
				if((str[stringSize] == '+' && st.top() == '-') || (str[stringSize] == '-' && st.top() == '+'))
				{
					st.push(str[stringSize]);
					N++;
				}
			}
			else if((st.empty() && (str[stringSize] == '-')) )
			{
				st.push(str[stringSize]);
				N++;
			}
			//str = str.substr(0, str.size() - 1);
			stringSize--;
		}

		cout << "Case #" << i << ": "<< N << endl;
	}

	return 0;
}


