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
		string s;
		cin >> s;
		int count = 1;
		for (int i = 1; i < s.size(); ++i)
			if (s[i - 1] != s[i])
				++count;

		if (s.back() == '+')
			--count;

		cout << "Case #" << _ << ": " << count << "\n";
	}
}


/*
1 - 1
2 - 2
3 - 2
01010000000101011100
*/
