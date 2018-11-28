
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>

using namespace std;

inline int readint() {
	char c = getchar();
	while (!isdigit(c)) c = getchar();
	int x = 0;
	while (isdigit(c)) {
		x = x * 10 + c - '0';
		c = getchar();
	}
	return x;
}

inline long long readlong() {
	char c = getchar();
	while (!isdigit(c)) c = getchar();
	long long x = 0;
	while (isdigit(c)) {
		x = x * 10 + c - '0';
		c = getchar();
	}
	return x;
}

#define FOR(i, n) for (int i = 0; i < (int)(n); i++)
#define REP(i, a, b) for (int i = (int)(a); i <= (int)(b); i++)
#define CIR(i, a, b) for (int i = (int)(b); i >= (int)(a); i--)
#define ADJ(i, u) for (int i = hd[u]; i != -1; i = edge[i].nxt)
#define ECH(i, v) for (__typeof((v).begin()) i = (v).begin(); i != (v).end(); ++ i)
#define PII pair<int, int>
#define FI first
#define SE second
#define MP make_pair
#define PB push_back
#define SZ(v) v.size()
#define ALL(v) v.begin(), v.end()
#define CLR(v, a) memset(v, a, sizeof(v))
#define IT iterator
#define LL long long
#define DB double
#define PI 3.1415926
#define INF 1000000000
int n, m, tot;

int mat[55][55];
int dx[] = {0, 0, -1, 1, -1, 1, -1, 1};
int dy[] = {-1, 1, 0, 0, -1, 1, 1, -1};

bool jud(int x, int y) {
	return x >= 0 && x < n & y >= 0 && y < m;
}

bool check() {
	FOR(i, n) {
		FOR(j, m) {
			if (mat[i][j] == 0 || mat[i][j] == 10) continue;
			bool ok = 0;
			FOR(k, 8) {
				int tx = i + dx[k], ty = j + dy[k];
				if (jud(tx, ty)) {
					if (mat[tx][ty] == 0) {
						ok = 1;
						break;
					}	
				}
			}

			if (!ok) 
				return 0;	
		}
	}

	return 1;
}

void output() {
	FOR(i, n) {
		FOR(j, m) {
			if (mat[i][j] == 10) {
				putchar('*');
			}	
			else {
				putchar('.');
			} 
		}
		puts("");
	}
}

void build() {
	FOR(i, n) {
		FOR(j, m) {
			int cnt = 0;
			if (mat[i][j] == 10) continue;
			FOR(k, 8) {
				int tx = i + dx[k], ty = j + dy[k];
				if (jud(tx, ty)) {
					if (mat[tx][ty] == 10) {
						cnt++;
					}
				}
			}		

			mat[i][j] = cnt;
		}
	}
}

int main() {
	int test;			
	cin >> test;

	FOR(cas, test) {
		cin >> n >> m >> tot;
		int r = n * m - tot;

		printf("Case #%d:\n", cas + 1);
		if (tot == 0) {
			FOR(i, n) {
				FOR(j, m) {
					if (i == 0 && j == 0)
						putchar('c');
					else
						putchar('.');
				}
				puts("");
			}
		}		
		else if (r == 1) {
			FOR(i, n) {
				FOR(j, m) {
					if (i == 0 && j == 0) {
						putchar('c');
					}
					else {
						putchar('*');
					}
				}
				puts("");
			}			
		}
		else {
			bool flag = 0;
			bool flip = 0;
			bool ff = 0;

			REP(i, 1, m) {
				if (i > r) continue;
				int t = r / i;
				int kk = t;
				if (r % i) t++;

				if (t > n) continue;


				int last = r % i;

				FOR(x, n) {
					FOR(y, m) {
						if ((x < kk && y < i) || (x == t - 1 && y < last)) {
							mat[x][y] = 0;
						}
						else {
							mat[x][y] = 10;
						}
					}
				}

				build();

				if (check()) {
					flag = 1;
					break;
				}	
			}

			if (!flag) {
				swap(n, m);
				flip = 1;

				REP(i, 1, m) {

					if (i > r) continue;
					int t = r / i;
					int kk = t;
					if (r % i) t++;

					if (t > n) continue;


					int last = r % i;

					FOR(x, n) {
						FOR(y, m) {
							if ((x < kk && y < i) || (x == t - 1 && y < last)) {
								mat[x][y] = 0;
							}
							else {
								mat[x][y] = 10;
							}
						}
					}

					build();

					if (check()) {
						flag = 1;
						break;
					}	
				}
			}

			if (!flag) {
				flip = 0;
				swap(n, m);
				r = tot;
				ff = 1;

				REP(i, 1, m) {

					if (i > r) continue;
					int t = r / i;
					int kk = t;
					if (r % i) t++;

					if (t > n) continue;


					int last = r % i;

					FOR(x, n) {
						FOR(y, m) {
							if ((x < kk && y < i) || (x == t - 1 && y < last)) {
								mat[x][y] = 10;
							}
							else {
								mat[x][y] = 0;
							}
						}
					}


					build();

					if (check()) {
						flag = 1;
						break;
					}	
				}
			}	

			if (!flag) {
				flip = 1;
				swap(n, m);

				REP(i, 1, m) {

					if (i > r) continue;
					int t = r / i;
					int kk = t;
					if (r % i) t++;

					if (t > n) continue;


					int last = r % i;

					FOR(x, n) {
						FOR(y, m) {
							if ((x < kk && y < i) || (x == t - 1 && y < last)) {
								mat[x][y] = 10;
							}
							else {
								mat[x][y] = 0;
							}
						}
					}

					build();

					if (check()) {
						flag = 1;
						break;
					}	
				}
			}


			if (!flag) {
				puts("Impossible");
			}
			else {

				int cnt = 0;

				if (!ff) {

					if (!flip) {
						FOR(i, n) {
							FOR(j, m) {
								if (i == 0 && j == 0) {
									putchar('c');
								}
								else if (mat[i][j] == 10) {
									cnt++;
									putchar('*');
								}
								else {
									putchar('.');
								}
							}
							puts("");	
						}	
					}
					else {
						FOR(i, m) {
							FOR(j, n) {
								if (i == 0 && j == 0) {
									putchar('c');
								}
								else if (mat[j][i] == 10) {
									putchar('*');
								}
								else {
									putchar('.');
								}
							}
							puts("");
						}
					}
				}
				else {

					if (!flip) {
						FOR(i, n) {
							FOR(j, m) {
								if (i == n - 1 && j == m - 1) {
									putchar('c');
								}
								else if (mat[i][j] == 10) {
									cnt++;
									putchar('*');
								}
								else {
									putchar('.');
								}
							}
							puts("");	
						}	
					}
					else {
						FOR(i, m) {
							FOR(j, n) {
								if (i == m - 1 && j == n - 1) {
									putchar('c');
								}
								else if (mat[j][i] == 10) {
									putchar('*');
								}
								else {
									putchar('.');
								}
							}
							puts("");
						}
					}
				}

			}			
		}
	}
	return 0;
}
