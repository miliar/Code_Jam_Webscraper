#include <iostream>
#include <cstdio>
#include <ctime>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#include <vector>
#include <map>
#include <queue>
#include <stack>
#include <set>
#include <utility>
#include <fstream>
#include <cassert>

#define INF 999999999999999999LL
#define MOD 1000000007
#define MAX 201000
#define ALL 50
#define DEBUG false

using namespace std;

int n,t;
vector<int> V;

int main()
{
	scanf("%d", &t);
	int maxT = t;
	while (t--) {
		scanf("%d", &n);
		string str;
		cin >> str;
		int res = 0;
		int sum = 0;
		for (int i = 0; i <= n; ++i) {
			if (sum < i) {
				res += i-sum;
				sum = i;
			}

			sum += (str[i]-'0');
		}

		cout << "Case #" << maxT - t << ": " << res << endl;
	}

	return 0;
}
