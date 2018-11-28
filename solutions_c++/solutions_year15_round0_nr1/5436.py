#include <iostream>
#include <string>
using namespace std;
int T, Smax, sol, cnt;
string str;
int main()
{
#ifdef _CONSOLE
	freopen("input.txt", "r", stdin);
	freopen("output2.txt", "w", stdout);
#endif
	cin >> T;
	for (int i = 1; i <= T; i++)
	{
		cnt = sol = 0;
		cin >> Smax >> str;
		for (int i = 1; i <=Smax; i++)
		{
			cnt += str[i-1] - '0';
			if (i > cnt)
			{
				sol += 1;
				cnt += 1;
			}
		}
		cout << "Case #" << i << ": " << sol << endl;
	}

}