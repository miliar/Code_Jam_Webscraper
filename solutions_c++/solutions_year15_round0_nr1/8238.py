#include<fstream>
#include<string>

#include<algorithm>
using namespace std;

string s;
int T, n, cas = 0;

int main()
{
	ifstream cin("A-large.in");
	ofstream cout("out.out");
	cin >> T;
	while (T--)
	{
		cin >> n >> s;
		int ans = 0, now = 0;
		for (int i = 0; i < s.length(); i++)
		{
			int a = s[i] - '0';
			if (a == 0)continue;
			if (i > now)
			{
				ans += i - now;
				now = i;
			}
			now += a;
		}
		cout << "Case #" << ++cas << ": " << ans << endl;
	}
	return 0;
}