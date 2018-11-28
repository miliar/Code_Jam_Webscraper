#include <iostream> 
#include <cstdio> 
#include <vector>
#include <string>
#include <algorithm>
using namespace std;
void push_forward(vector<char>&a, char y)
{
	int tmp = a.size();
	a.push_back('0');
	for (int i = tmp - 1; i >= 0; i--)
	{
		a[i + 1] = a[i];
	}
	a[0] = y;
}
int main()
{
	freopen("A-large .in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T;
	cin >> T;
	for (int i = 0; i < T; i++)
	{
		string S;
		vector<char>ans;
		cin >> S;
		ans.push_back(S[0]);
		for (int j = 1; j < S.size(); j++)
		{
			char c = S[j];
			if (c>=ans[0])
			{
				push_forward(ans, c);

			} else
			{
				ans.push_back(c);
			}
		}
		cout << "Case #" << i+1 << ":" << " ";
		for (int k = 0; k < ans.size(); k++)
		{
			cout << ans[k];
		}
		cout << endl;
	}
	return 0;
}
