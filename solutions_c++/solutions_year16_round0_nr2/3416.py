#include <iostream>
#include <string>
#include <cstring>
#include <stack>
#include <queue>
using namespace std;

int main()
{
	freopen("test.in", "r", stdin);
	freopen("test.out", "w", stdout);
	int n; cin>> n;
	for (int T = 1; T < n+1; T++)
	{
		string str;cin>> str;
		stack<char> st,q;
		int total = 0;
		int index = 0;
		for (int i = (int)str.length() -1; i>=0; i--)
		{
			st.push(str[i]);
			if (str[i] == '-') total ++;
		}
		while (total > 0)
		{
			index++;
			while (total > 0)
			{
				if (st.top() == '-') total --;
				q.push(st.top());
				st.pop();
			}
			while (!q.empty())
			{
				if (q.top() == '+') total ++;
				st.push(q.top() == '+' ? '-' : '+');
				q.pop();
			}
		}
		cout << "Case #" << T << ": " << index << endl;
	}
}