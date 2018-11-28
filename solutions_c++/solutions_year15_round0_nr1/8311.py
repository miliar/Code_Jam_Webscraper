#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main(int argc, char* argv[])
{
	ios_base::sync_with_stdio(false);

	int T;
	cin >> T;

	int stand, add;
	string s;

	int smax;
	for (int i = 0; i < T; ++i)
	{
		stand = add = 0;

		cin >> smax;
		cin >> s;

		int nj;
		for (int j = 0; j <= smax; j++)
		{
			nj = s.at(j) - '0';
			if (j > stand)
			{
				add += j - stand;
				stand += j - stand + nj;
			}
			else
			{
				stand += nj;
			}
		}

		cout << "Case #" << i + 1 << ": " << add << endl;
	}

	return 0;
}