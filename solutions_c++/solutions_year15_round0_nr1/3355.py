#include <bits/stdc++.h>

using namespace std;

int t;
int maior;
string str;

int main(void)
{
	cin >> t;
	int cases = 0;
	while (t--)
	{
		 cin >> maior;
		 cin >> str;

		 int total = str[0]-'0';
		 int num = 0;
		 int ans = 0;

		 for (int i = 1; i < str.size(); ++i)
		 {
		 	int num = str[i] - '0';

		 	if (total < i)
		 	{
		 		ans += i - total;
		 		total += i - total;
		 	}
		 	total += num;
		 }

		 cout << "Case #" << ++cases << ": " << ans << "\n";
	}
	return 0;
}