#include <iostream>
#include <algorithm>
#include <map>
#include <set>
#include <vector>
#include <string>
#include <sstream>
#include <time.h>
#include <stdlib.h>
#include <queue>
#include <random>
#include <fstream>
#include <stack>
#include <cmath>

using namespace std;

ifstream in("input.txt");
ofstream out("output.txt");

#define cin in
#define cout out
/**/
int main()
{
	cin.tie(0);
	ios_base::sync_with_stdio(0);
	int test;
	cin >> test;
	for (int _ = 1; _ <= test; ++_)
	{

		int n;
		cin >> n;
		long long ans = 0;
		if (n == 0)
		{
			cout << "Case #" << _ << ": INSOMNIA\n";
			continue;
		}
		set<int> mapka;

		do
		{
			ans += n;
			int k = ans;
			while (k)
			{
				mapka.insert(k % 10);
				k /= 10;
			}
		} while (mapka.size() != 10);
		cout << "Case #" << _ << ": " << ans << "\n";
	}
}


/*
1 - 1
2 - 2
3 - 2
01010000000101011100
*/