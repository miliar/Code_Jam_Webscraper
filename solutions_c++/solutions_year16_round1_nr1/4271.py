#include <fstream>
#include <iostream>
#include <string>

using namespace std;

int main()
{
	ifstream file_reader("large_input.in");
	ofstream file_writer("large_output.txt");
	int t;
	file_reader >> t;

	for (int c = 1; c <= t; ++c)
	{
		string s;
		file_reader >> s;

		string ans = "";
		ans += s[0];
		for (int i = 1; i < s.size(); ++i)
		{
			if (s[i] >= ans[0])
				ans = s[i] + ans;
			else
				ans += s[i];
		}
		file_writer << "Case #" << c << ": " << ans << endl;
	}
	return 0;
}