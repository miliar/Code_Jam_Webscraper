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

void clear(int i) {

}

int solution(int nTest) {
	int r, n, m, k;
	scanf("%d%d%d%d", &r, &n, &m, &k);
	For(it, 0, r) {
		int t;
		vector<int> mul;
		For(i, 0, k) {
			scanf("%d", &t);
			mul.pb(t);
		}
		int flag = 0;
		For(a, 2, m + 1) {
			if(flag) {
				break;
			}
			For(b, 2, m + 1) {
				if(flag) {
					break;
				}
				For(c, 2, m + 1) {
					int ar[3];
					ar[0] = a; ar[1] = b; ar[2] = c;
					set<int> mult;
					For(i, 0, sz(mul)) {
						mult.insert(mul[i]);
					}
					For(mask, 0, 1 << 3) {
						int r = 1;
						For(i, 0, 3) {
							if(mask & (1 << i)) {
								r *= ar[i];
							}
						}
						mult.erase(r);
					}
					if(sz(mult) == 0) {
						flag = 1;
						printf("%d%d%d\n", a, b, c);
						break;
					}
				}
			}
		}
		if(flag == 0) {
			printf("222\n");
		}
	}



	return 0;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int i = 0, n = 999999;
	scanf("%d", &n);
	init();
	For(i, 0, n) {
		printf("Case #%d:\n", i + 1);
		clear(i);
		solution(i);
	}

	return 0;
}
	
