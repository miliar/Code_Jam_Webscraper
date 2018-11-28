#include<iostream>
#include<fstream>

using namespace std;

int main()
{
	ifstream fin("input.txt");
	ofstream fout("output.txt");
	int t, smax,sum, j = 1, ans;
	char s[1001], ch;
	fin >> t;
	while (t--)
	{
		sum = ans = 0;
		fin >> smax;
		fin.get(ch);
		for (int i = 0; i < smax + 1; i++)
		{
			fin >> s[i];
			if (i > sum+ans)
				ans += i - (sum+ans);
			sum += (int)s[i] % 48;
		}
		fin.get(ch);
		fout << "Case #" << j++ << ": " << ans << endl;
	}
	fin.close();
	fout.close();
	return 0;
}