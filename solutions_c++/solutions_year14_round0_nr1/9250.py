#define _CRT_SECURE_NO_WARNINGS
#define _USE_MATH_DEFINES
#pragma comment(linker, "/STACK:16777216")

#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <string>
#include <vector>
#include <iostream>
#include <map>
#include <stack>
#include <set>
#include <queue>
#include <numeric>
#include <algorithm>
#include <utility>
#include <bitset>
#include <cmath>
#include <sstream>
#include <functional>

#define all(a) (a).begin(),(a).end()
#define sz(a) (int)(a).size()

using namespace std;

typedef long long int64;
typedef vector<int> vi;
typedef vector< vi > vvi;
typedef vector<double> vd;
typedef vector< vd > vvd;
typedef vector< string > vs;
typedef pair< int, int > pii;
typedef vector< pii > vpii;



int main()
{
#ifndef ONLINE_JUDGE
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
#endif
	int T = 0;
	cin >> T;
	for (int t = 0; t < T; t++)
	{
		int r1;
		cin >> r1;
		set<int> r1s;
		for (int i = 0; i < 4; i++)
		{
			for (int j = 0; j < 4; j++)
			{
				int x;
				cin >> x;
				if (i == r1 - 1)
				{
					r1s.insert(x);
				}
			}
		}

		int ans = -1;
		int ans_cnt = 0;

		int r2;
		cin >> r2;
		for (int i = 0; i < 4; i++)
		{
			for (int j = 0; j < 4; j++)
			{

				int x;
				cin >> x;
				if (i == r2 - 1)
				{
					if (r1s.find(x) != r1s.end())
					{
						ans = x;
						ans_cnt++;
					}
				}
			}
		}
		cout << "Case #" << t + 1 << ": ";
		// TODO: Answer here

		if (ans_cnt == 0)
			cout << "Volunteer cheated!";
		else if (ans_cnt == 1)
			cout << ans;
		else
			cout << "Bad magician!";
		cout << endl;
	}

	return 0;
}