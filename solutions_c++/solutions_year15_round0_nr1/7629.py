#include <iostream>
using namespace std;
int main()
{
	ios_base::sync_with_stdio(false);
	int t;
	while (cin>> t)
	{
		for (int j = 1; j <= t; j++)
		{
			int n;
			string s;
			cin>> n>> s;
			int cnt = 0, res = 0;
			for (int i = 0; i < s.size(); i++)
			{
				if (cnt < i)
				{
					res += (i - cnt);
					cnt = i;
				}
				cnt += s[i] - '0';
			}
			cout<< "Case #"<< j<<": "<< res<<endl;
		}
	}
}
