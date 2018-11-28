#include <cstdio>
#include <cstring>
#include <cmath>
#include <iostream>
#include <string>
#include <set>
#include <map>
#include <vector>
#include <algorithm>

using namespace std;

#define debug 1

#define cerr if(debug) cerr

#define For(i, a, b) for(int i = a; i < b; i++)
#define sz(a) ((int)a.size())
#define mp make_pair
#define pb push_back
#define all(a) a.begin(), a.end()

typedef pair<int, int> pii;
typedef long long lint;

const int inf = 0x7fffffff;
const int Size = 1000 * 1000 + 1;
char buffer[Size];


void init() {

}

map<pair<vector<int>, int>, int > st;
void clear(int i) {
	st.clear();
}
int r, c, w;

int recb(vector<int> &a, int shoot, int step);

int reca(vector<int> &a, int step) {
	if (st.count(mp(a, step))) {
		return st[mp(a,step)];
	}
	For (j, 0, c - w + 1) {
		int flag = false;
		For (k, 0, j) {
			if (a[k] == 2) {
				flag = true;
				break;
			}
		}
		if (flag) {
			continue;
		}
		For (k, w + j, c) {
			if (a[k] == 2) {
				flag = true;
				break;
			}
		}
		if (flag) {
			continue;
		}
		For (k, j, w + j) {
			if (a[k] != 2) {
				flag = true;
				break;
			}
		}
		if (flag) {
			continue;
		}
		return step;
	}
	int cnt = 0;
	int res = inf;
	For (i, 0, c) {
		if (a[i] != 0) {
			continue;
		}
		int hit = 0;
		For (i, 0, sz(a)) {
			if (a[i] == 2) {
				hit++;
			}
		}
		//if (step + (w - hit) >= res) {
//			cerr << "opt" << endl;

		//continue;

	//}
		int cnt = recb(a, i, step);
		if (cnt != -1) {
			res = min(res, cnt);
		}
	}
	st[mp(a, step)] = res;
	return res;
}

int recb(vector<int> &a, int shoot, int step) {
	int res = -1;
	For (j, 0, c - w + 1) {
		int flag = false;
		For (k, 0, j) {
			if (a[k] == 2) {
				flag = true;
				break;
			}
		}
		if (flag) {
			continue;
		}
		For (k, w + j, c) {
			if (a[k] == 2) {
				flag = true;
				break;
			}
		}
		if (flag) {
			continue;
		}
		int cnt2 = 0;
		int posR = 0;
		int posL = inf;
		For (k, j, w + j) {
			if (a[k] == 1) {
				flag = true;
				break;
			} else if (a[k] == 2) {
				cnt2++;
				posR = max(posR, k);
				posL = min(posL, k);
			}
		}
		if (flag) {
			continue;
		}
		/*
		if (cnt2 == 0) {
			int tt = 0;
			For (i, 0, c - w + 1) {
				int can = true;
				For (k, 0, w) {
					if (a[i + k] == 1) {
						can = false;
						break;
					}
				}
				if (can) {
					tt++;
				}
			}
			if (tt + step <= res) {
				continue;
			}
		} else {

		}
		*/

		if (shoot >= j && shoot < w + j) {
			a[shoot] = 2;
		} else {
			a[shoot] = 1;
		}
		int cnt = reca(a, step + 1);
		if (cnt != inf) {
			res = max(res, cnt);
		} else {
			cerr << "INF" << endl;
		}
		
		a[shoot] = 0;
	}
	return res;
}

int solution(int nTest) {
	cin >> r >> c >> w;
	cerr << nTest << ":" << c << " " << w << endl;
	vector<int> a;
	a.resize(c);

	int res = reca(a, 0);
	cout << res << endl;

	return 0;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int i = 0, n = 999999;
	scanf("%d", &n);
	init();
	For(i, 0, n) {
		printf("Case #%d: ", i + 1);
		clear(i);
		solution(i);
	}

	return 0;
}
	
