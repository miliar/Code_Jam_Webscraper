#include <iostream>
#include <string>
#include <fstream>
using namespace std;

int main()
{
	int T;
	ifstream ifs("A-large.in");
	ofstream ofs("A-large.out");
	ifs >> T;
	for (int i = 0; i < T; ++i)
	{
		int k;
		ifs >> k;
		string s;
		ifs >> s;

		int res = 0;
		int cur = 0;
		for (int j = 0; j < s.size(); ++j)
		{
			int num = s[j] - '0';
			if(cur >= j)
				cur += num;
			else
			{
				res = res + (j - cur);
				cur += j - cur + num;
			}
		}
		ofs << "Case #" << i + 1 << ": " << res << endl;
	}
		

	
	return 0;
}