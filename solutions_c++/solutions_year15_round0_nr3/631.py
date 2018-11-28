#include <cstdio>
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <ctime>
#include <cstring>
#include <stack>
#include <deque>
using namespace std;
//-----------------------------------------------------------
#define forn(i, n) for(int i = 0; i < (int)(n); i++)
#define ford(i, n) for(int i = (int)(n) - 1; i >= 0; i--)
#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define last(a) int(a.size() - 1)
#define all(a) a.begin(), a.end()
#define seta(a,x) memset (a, x, sizeof (a))
#define I (int)
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> pii;
typedef long double ldb;

const long double eps = 1e-9;
const int inf = (1 << 30) - 1;
const ull inf64 = ((ull) 1 << 62) - 1;
const long double pi = 3.1415926535897932384626433832795;

#define bit(i) ((ull)1 << i)
//-----------------------------------------------------------

long long int L, X;
stack<char> str;
stack<char> onestr;
vector<char> vtmp;
char mod[4];
bool mods[4];

void setOneRound() {

	while (!onestr.empty())
		onestr.pop();

	for (int j = L - 1; j >= 0; j--) {
		onestr.push(vtmp[j]);
	}

	mods[1] = true;
	while (onestr.size() > 1) {

		char a = onestr.top();
		onestr.pop();
		char b = onestr.top();
		onestr.pop();

		if (a == b) {
			mods[1] = !mods[1];
		} else if (a == 'i' && b == 'j') {
			onestr.push('k');
		} else if (a == 'k' && b == 'i') {
			onestr.push('j');
		} else if (a == 'j' && b == 'k') {
			onestr.push('i');
		} else if (a == 'j' && b == 'i') {
			mods[1] = !mods[1];
			onestr.push('k');
		} else if (a == 'i' && b == 'k') {
			mods[1] = !mods[1];
			onestr.push('j');
		} else if (a == 'k' && b == 'j') {
			mods[1] = !mods[1];
			onestr.push('i');
		}
	}

	if (onestr.size() == 0) {
		mod[1] = ' ';
		mod[2] = ' ';
		mod[3] = ' ';
		mod[0] = ' ';
		mods[2] = true;
		mods[3] = mods[1];
		mods[0] = true;
	} else {
		mod[1] = onestr.top();
		mod[2] = ' ';
		mod[3] = mod[1];
		mod[0] = ' ';
		mods[2] = false;
		mods[3] = !mods[1];
		mods[0] = true;
	}

	for (int i = 0; i < 4; i++) {
		//printf("%d: [%c %d]\n", i, mod[i],mods[i]);
	}

	//printf("1: [%c %d] 2: [%c %d]\n",one , ones, two, twos);//
}

void solve() {
	setOneRound();
	//printf("%c %d\n", one, ones);
	//
	long long int ans = 0;
	long long int anscnt = 0;
	long long int cnt = 1;
	char rePush = ' ';
	bool s = true;
	bool needRepush = false;
	while (true) {
		if (str.size() < 2) {
			/* no more reload, check the answer */
			if (cnt == X) {
				if (str.size() == 0) {
					if (ans == 3 && s) {
						printf("YES\n");
					} else {
						printf("NO\n");	//printf("12333 %d\n",s);
					}
					return;
				} else if (str.size() == 1) {
					if (ans == 2 && str.top() == 'k' && s) {
						printf("YES\n");
					} else {
						printf("NO\n");	////
					}
					return;
				}
			}
			/* re push another set */
			else if (cnt < X) {
				long long int pushId = 0;
				if (ans == 2) {
					long long int left = X - cnt;
					pushId = (left % 4) + 1;// printf("%d left=%d\n", pushId, left);
					cnt = X;
				} else {
					cnt++;
					anscnt++;
					if (anscnt >= 10) {
						printf("NO\n"); //
						return;
					}
				}

				needRepush = false;
				if (str.size() == 1) {
					needRepush = true;
					rePush = str.top();
					str.pop();

					//printf("=> %c s %d cnt %d pushId %d\n", rePush, s,  X - cnt, pushId);
				}

				if (pushId == 0) {
					for (long long int j = L - 1; j >= 0; j--) {
						str.push(vtmp[j]);
						//printf("%c", vtmp[j]);
					}
					//printf(" %d cnt = %d\n", ans, cnt);
				} else {
					if (mod[pushId - 1] != ' ') {
						str.push(mod[pushId - 1]);
						//printf("size %d pushId = %d\n", str.size(), pushId);

					}
					s = !(s ^ mods[pushId - 1]);

				}

				if (needRepush) {
					str.push(rePush);
					//printf("size %d news = %d\n", str.size(), s);
				}

			}
		}
		//printf("%d %d %d??\n", test++, str.size(), cnt);
		fflush(stdout);

		if (str.size() == 0) {
			continue;
		}

		char a = str.top();
		str.pop();

		if (ans == 0 && a == 'i') {
			ans = 1;
			anscnt = 0;
			//printf("i (%d\n", ans);
			continue;
		} else if (ans == 1 && a == 'j') {
			ans = 2;
			anscnt = 0;
			//printf("j (%d\n", ans);
			continue;
		}

		if (str.size() == 0) {
			str.push(a);
			continue;
		}

		char b = str.top();
		str.pop();

		//printf("%c [%c %c] (%d\n", s ? '+' : '-', a, b, ans);

		if (a == b) {
			s = !s;
		} else if (a == 'i' && b == 'j') {
			str.push('k');
		} else if (a == 'k' && b == 'i') {
			str.push('j');
		} else if (a == 'j' && b == 'k') {
			str.push('i');
		} else if (a == 'j' && b == 'i') {
			s = !s;
			str.push('k');
		} else if (a == 'i' && b == 'k') {
			s = !s;
			if (ans == 1) {
				ans = 2;
			} else {
				str.push('j');
			}
		} else if (a == 'k' && b == 'j') {
			s = !s;
			if (ans == 0) {
				ans = 1;
			} else {
				str.push('i');
			}
		}

	}
}

int main() {
	int cases;
	int caseid = 1;

	freopen("input", "r", stdin);
	freopen("output", "w", stdout);
	scanf("%d", &cases);
	while (cases--) {
		printf("Case #%d: ", caseid++);
		scanf("%lld%lld", &L, &X);

		vtmp.clear();
		char tmp = getc(stdin); // for "\n"
		for (long long int i = 0; i < L; i++) {
			tmp = getc(stdin);
			//printf("c = [%c]\n", tmp);
			vtmp.push_back(tmp);
		}

		while (!str.empty())
			str.pop();

		//for(int i = 0; i < X; i++) {
		for (long long int j = L - 1; j >= 0; j--) {
			str.push(vtmp[j]);
		}
		//}
		solve();
	}
	return 0;
}

