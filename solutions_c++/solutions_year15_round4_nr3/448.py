#include <iostream>
#include <math.h>
#include <string.h>
#include <string>
#include <cmath>
#include <stdio.h>
#include <vector>
#include <map>
#include <list>
#include <queue>
#include <functional>
#include <algorithm>
#include <bitset>
#include <set>
#include <stack>
#include <limits>
#include <sstream>
#include <ctime> 
#define endl '\n'
#pragma warning (disable : 4996)

using namespace std;

#define lli long long int
#define ull unsigned long long int
#define MP make_pair

const int N = (int)(1e5 + 20);
const int L = 20;
const lli M = 1000000007;
const double E = 1e-7;

vector<int> v[N];

int cnt = 0;
map<string, int> sNum; 

void clear() {
	cnt = 0;
	sNum.clear();
}

int getNum(string s) {
	if (sNum.find(s) == sNum.end()) {
		v[cnt].clear();
		sNum[s] = cnt++;
	}
	return sNum[s];
}

bool engl[N];

int check() {
	int ans = 0;
	for (int i = 0; i < cnt; ++i) {
		bool eng = false;
		bool fren = false;
		for (int j = 0; j < v[i].size(); ++j) {
			eng |= engl[v[i][j]];
			fren |= !engl[v[i][j]];
		}
		ans += (eng && fren);
	}
	return ans;
}

int main()
{
	ios_base::sync_with_stdio(0);

	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	engl[0] = 1;
	int T;
	cin >> T;
	for (int qq = 0; qq < T; ++qq) {
		std::cout << "Case #" << (qq + 1) << ": ";
		
		clear();

		int n;
		cin >> n; string whole; getline(cin, whole);
		for (int i = 0; i < n; ++i) {
			getline(cin, whole);
			stringstream stream(whole);
			string s;
			while (stream >> s) {
				int num = getNum(s);
				v[num].push_back(i);
			}
		}
		int ans = 1000000;

		if (n == 2) {
			cout << check();
		} else {
			int bound = 1 << (n - 2);
			for (int mask = 0; mask < bound; ++mask) {
				int tm = mask;
				for (int i = 2; i < n; ++i) {
					engl[i] = tm & 1;
					tm >>= 1;
				}

				ans = min(ans, check());
			}

			std::cout << ans;
		}


		std::cout << endl;
	}
}
