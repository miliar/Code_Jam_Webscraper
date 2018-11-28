using namespace std;
#include <fstream>
#include <vector>
#include <algorithm>
#include <string>


int main()
{
	int i, j, t, n, ans;
	char s[105];
	ifstream fin("data.in");
	ofstream fout("data.out");

	fin >> t; fin.get();
	for (i = 1; i <= t; ++i)
	{
		fin.getline(s, 105);

		for (ans = 0, j = 1; s[j]; ++j)
			if (s[j] != s[j - 1])
				++ans;

		if (s[j - 1] == '-') ++ans;

		fout << "Case #" << i << ": " << ans << '\n';
	}

	fin.close();
	fout.close();

    return 0;
}
