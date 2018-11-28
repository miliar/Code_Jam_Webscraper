#include <iostream>
#include <algorithm>
#include <fstream>
using namespace std;
ifstream fin("t.txt");
ofstream fout("out.txt");
int n;
char s[1005];
int main()
{
	int T;
	fin >> T;
	for (int k = 1; k <= T; k++)
	{
		fout << "Case #" << k << ": ";
		fin >> n;
		fin >> s;
		int stand = s[0]-'0';
		int ans = 0;
		for (int i = 1; i <= n; i++)
		{
			if (stand < i) {
				ans += i - stand; stand = i;
			}
			stand += s[i] - '0';
		}
		fout << ans << "\n";
	}
}