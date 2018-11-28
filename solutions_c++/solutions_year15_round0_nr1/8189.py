#include <iostream>
#include <string>
#include <fstream>
using namespace std;
int main()
{
	ofstream fout("a.out");
	int t;
	cin >> t;
	for (int i = 1; i <= t; i++)
	{
		int cur = 0;
		int smax, ans = 0;
		string ss;
		cin >> smax >> ss;
		cur += ss[0] - '0';
		for (int j = 1; j <= smax; j++)
		{
			// cout << cur<<endl;
			while (cur < j)
			{
				ans++;
				cur++;
			}
			cur += ss[j] - '0';
		}
		fout << "Case #" << i << ": " << ans << endl;
	}
	return 0;
}