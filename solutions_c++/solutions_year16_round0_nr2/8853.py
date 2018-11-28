#include <iostream>
#include <string>
typedef long long ll;
using namespace std;
#define not(x) ((x)==0?1:0)

int main()
{
	ios::sync_with_stdio(false);
	int T; cin >> T;
	for (int t = 1; t <= T; t++)
	{
		int ans = 0, N, i, f=0;
		string s; cin >> s;
		N = s.length();
		for (i = 0; i < N; i++)
		{
			if (s[i] == '-') { if (!f) { ans++; f = 1; } }
			else break;
		}
		if (i != N) {
			for (int j = i; j < N; j++)
				if (s[j] == '-')
					if (s[j - 1] != '-')
						ans += 2;
		}
		cout << "Case #" << t << ": ";
		cout << ans << endl;
	}
	return 0;
}