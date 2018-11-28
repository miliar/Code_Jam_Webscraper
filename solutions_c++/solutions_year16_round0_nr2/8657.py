#include <iostream>
#include <stack>
#include <string>
using namespace std;


int main()
{
	int T;
	cin >> T;
	for (int q = 1; q <= T;q++)
	{
		string data;
		cin >> data;
		stack<char> st;

		for (int i =data.length()-1 ; i >=0; i--)
		{
			st.push(data[i]);
		}

		int count = 0;
		while (!st.empty())
		{
			char temp = st.top();
			st.pop();
			if (temp == '+')
			{
				while (!st.empty() && st.top() == '+') st.pop(); //pop + until empty or '-'
				if (st.empty()) break;
				else
				{
					st.push('-');
					count++;
				}
			}
			else //- case
			{
				while (!st.empty() && st.top() == '-') st.pop(); //pop + until empty or '-'
				if (st.empty())
				{
					count++;
					break;
				}
				else
				{
					st.push('+');
					count++;
				}
			}
			
		}
		cout << "Case #" << q << ": ";
		cout << count << endl;

	}

	return 0;
}