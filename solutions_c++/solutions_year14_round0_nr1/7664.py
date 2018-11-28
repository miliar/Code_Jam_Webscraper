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
	REP(1, T+1, t) {
		cout << "Case #" << t << ": ";
		
		int i, j;
		
		int ans0, ans1;
		cin >> ans0;
		--ans0;
		set<int> candidates;
		REP(0, 4, i) {
			REP(0, 4, j) {
				int num;
				cin >> num;
				if(ans0 == i) {
					candidates.insert(num);
				}
			}
		}
		
		int answer = -1;
		cin >> ans1;
		--ans1;
		bool flag = true;
		REP(0, 4, i) {
			REP(0, 4, j) {
				int num;
				cin >> num;
				if(ans1 == i) {
					if(flag) {
						if(candidates.find(num) != candidates.end()) {
							if(answer != -1) {
								cout << "Bad magician!" << endl;
								flag = false;
							}
							answer = num;
						}
					}
				}
			}
		}
		
		if(flag) {
			if(answer == -1) {
				cout << "Volunteer cheated!" << endl;
			}
			else {
				cout << answer << endl;
			}
		}
	}
	return 0;
}
