#include <iostream>
#include <fstream>
#include <vector>
#include <string>
using namespace std;


int main()
{
	ifstream inf("in.txt");
	int t, T;
	inf >> T;
	
	ofstream outf("res.txt");
	for (t = 1;t <= T;t++)
	{
		int len;
		inf >> len;
		string s;
		inf >> s;
		int cur = 0, res = 0;
		int i;
		for (i = 0;i <= len;i++)
		{
			if (cur >= i)
			{
				cur += s[i] - '0';
			}
			else
			{
				res += i - cur;
				cur = i + s[i] - '0';
			}

		}
		outf << "Case #" << t << ": " << res << endl;
	}
    return 0;
}