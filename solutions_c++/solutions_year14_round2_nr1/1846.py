#include<iostream>
#include<iomanip>
#include<cstdio>
#include<vector>
#include<algorithm>
#include<functional>
#include<string>
#include<cstdlib>
#include<cmath>
#include<map>
#include<set>
#include<list>
#include<utility>
#include<cstring>
#include<queue>
#include<stack>
#include<climits>
using namespace std;

#define rrepp(i, from, to) for (int i = (from); i <= (to); ++i)
#define rrep(i, from, to) for (int i = (from); i < (to); ++i)
#define repp(i, from, to) for (i = (from); i <= (to); ++i)
#define rep(i, from, to) for (i = (from); i < (to); ++i)


void run(int _)
{
	int n;
	cin >> n;
	vector<string> strs(n);
	vector<vector<int> > shifts(n);
	rrep(i, 0, n) {
		cin >> strs[i];
		char ch = 0;
		rrep (j, 0, strs[i].length()) {
			if (strs[i][j] != ch) {
				shifts[i].push_back(1);
			} else {
				++shifts[i].back();
			}
			ch = strs[i][j];
		}
	}
	rrep(i, 1, n) {
		if (shifts[i - 1].size() != shifts[i].size()) {
			printf("Case #%d: Fegla Won\n", _+1);
			return;
		}
		int s1 = 0;
		int s2 = 0;
		rrep (j, 0, shifts[i].size()) {
			if (strs[i - 1][s1] != strs[i][s2]) {
				printf("Case #%d: Fegla Won\n", _+1);
				return;
			}
			s1 += shifts[i - 1][j];
			s2 += shifts[i][j];
		}
	}
	int result = 0;
	rrep (i, 0, shifts[0].size()) {
		int sum = 0;
		rrep (j, 0, n) {
			sum += shifts[j][i];
		}
		int avg = sum / n;
		int sum1 = 0;
		int sum2 = 0;
		rrep(j, 0, n) {
			sum1 += abs(shifts[j][i] - avg);
			sum2 += abs(shifts[j][i] - (avg + 1));
		}
		result += min(sum1, sum2);
	}
	printf("Case #%d: %d\n", _+1, result);
}

int main()
{
	int t;
	cin >> t;
	rrep (_, 0, t){
		run(_);
	}
	return 0;
}