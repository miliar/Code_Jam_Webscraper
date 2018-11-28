#include <iostream>
#include <string>
#include <vector>
using namespace std;
int main()
{
	int T, shylevel;
	cin >> T;
	string testcase, shyaud;
	vector<int> vi;
	vector<string> vs;
	for (int i = 0; i < T; ++i)
	{
		getline(cin, testcase);
		cin >> shylevel;
		cin >> shyaud;
		vi.push_back(shylevel);
		vs.push_back(shyaud);
	}
	for (unsigned i = 0; i < vi.size(); ++i)
	{
		int cnt = 0, friendcnt = 0;
		for (int j = 0; j <= vi[i]; ++j)
		{
			int temp = vs[i][j] - '0';
			if (j > cnt)
			{
				++friendcnt;
				cnt += (temp + 1);
			}
			else
				cnt += temp;
		}
		cout << "Case #" << i + 1 << ": " << friendcnt << endl;
	}
	return 0;
}