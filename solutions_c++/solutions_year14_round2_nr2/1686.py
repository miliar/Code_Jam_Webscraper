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
	long long aa, bb, k;
	cin >> aa >> bb >> k;
	long long a = max(aa, bb);
	long long b = min(aa, bb);
	long long result = 0;
	rrep (i, 0, a) {
		rrep (j, 0, b) {
			if ((i&j) < k) {
				++result;
			}
		}
	}
	cout << "Case #" << _ << ": " << result << "\n";
}

int main()
{
	int t;
	cin >> t;
	rrep (_, 0, t){
		run(_ + 1);
	}
	return 0;
}