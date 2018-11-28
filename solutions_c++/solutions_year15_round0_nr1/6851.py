#include <iostream>
#include <string>

using namespace std;

#define rf freopen("in.txt", "r", stdin)
#define wf freopen("out.txt", "w", stdout)

string people;
int p [1001];

int main ()
{
	rf;
	wf;
	int t, ans, s, num;
	cin >> t;
	for (int j = 1; j <= t; ++j)
	{
		ans = 0;
		num = 0;
		cin >> s >> people;
		for (int i = 0; i < people.length(); i++)
			p[i] = people[i] - '0';
		for (int i = 0; i <= s; i++)
		{
			if (num < i)
			{
				ans += i - num;
				num = i;
			}
			num += p[i];
		}
		cout << "Case #" << j << ": " << ans << '\n';
	}
}