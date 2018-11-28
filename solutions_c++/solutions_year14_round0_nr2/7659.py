#include <cstdio>
#include <cmath>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <set>
#include <map>

using namespace std;
typedef long long i64;

typedef i64 nkr_int;

typedef vector<nkr_int> vi;
typedef vector<vi> vvi;
#define pb push_back
#define iter(T) T::iterator
#define sz(a) int((a).size())
#define all(c) (c).begin(), (c).end()
#define tr(c, i) for(i = (c).begin(); i != (c).end(); ++i)
#define present(c, x) ((c).find(x) != (c).end())
#define cpresent(c, x) (find(all(c), x) != (c).end())
#define REP(s, e, n)  for(n = (s); n < (e); ++n)

int main(int argc, const char *argv[]) {
	int T, t;
	cin >> T;
	REP(1, T + 1, t) {
		cout << "Case #" << t << ": ";
		
		double C, F, X;
		cin >> C >> F >> X;
		
		double min_time = -1;
		double sg = 0;
		i64 nC = 0;
		i64 n = 0;
		while(nC < X) {
			double time;
			time = sg + X / (2 + F * n);
			
			if(min_time < 0 || time < min_time) {
				min_time = time;
			}

			sg += C / (2 + F * n);
			nC += C;
			++n;
		}
		
		printf("%.7f\n", min_time);
	}
	return 0;
}
