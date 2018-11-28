#include <iostream>
#include <cstdio>
#include <fstream>
#include <string>
#include <cstring>
#include <cmath>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <queue>
#include <bitset>
#include <climits>
using namespace std;

typedef pair<int, int> pi;
typedef pair<int, string> ps;


int main()
{
	std::ios_base::sync_with_stdio(false);
	ifstream is; is.open("A-large.in");
	ofstream os; os.open("Answer_A_Large.txt");

	int testCase;
	//cin >> testCase;
	is >> testCase;

	for (int i = 0; i != testCase; ++i)
	{
		unsigned long long n;
		//cin >> n;
		is >> n;

		if (n == 0)
		{
			//cout << "Case #" << (i + 1) << ": INSOMNIA" << endl;
			os << "Case #" << (i + 1) << ": INSOMNIA" << endl;
		}
		else
		{
			unordered_set<int> seen;
			int k = 1;
			unsigned long long ans;

			while (seen.size() != 10)
			{
				ans = (n*k);
				int copy = ans;

				while (copy != 0)
				{
					seen.insert(copy % 10);
					copy /= 10;
				}
				++k;
			}
			//cout << "Case #" << (i + 1) << ": " << ans << endl;
			os << "Case #" << (i + 1) << ": " << ans << endl;
		}
	}
}