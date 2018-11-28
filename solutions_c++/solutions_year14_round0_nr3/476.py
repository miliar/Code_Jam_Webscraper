#include <cstdio>
#include <algorithm>
#include <cmath>
#include <vector>
#include <string>

using namespace std;

void gao(int r, int c, int m) {
	if (m == 1) {
		putchar('c');
		for (int i = 1; i < c; ++i) {
			putchar('*');
		}
		puts("");
		for (int i = 1; i < r; ++i) {
			for (int j = 0; j < c; ++j) {
				putchar('*');
			}
			puts("");
		}
		return;
	}

	if (r == 1) {
		putchar('c');
		for (int i = 1; i < m; ++i) {
			putchar('.');
		}
		for (int i = m; i < c; ++i) {
			putchar('*');
		}
		puts("");
		return;
	}

	if (c == 1) {
		puts("c");
		for (int i = 1; i < m; ++i) {
			puts(".");
		}
		for (int i = m; i < r; ++i) {
			puts("*");
		}
		return;
	}

	if (r == 2) {
		if (m % 2 == 1 || m == 2) {
			puts("Impossible");
			return;
		} else {
			putchar('c');
			for (int i = 1; i < m / 2; ++i) {
				putchar('.');
			}
			for (int i = m / 2; i < c; ++i) {
				putchar('*');
			}
			puts("");
			for (int i = 0; i < m / 2; ++i) {
				putchar('.');
			}
			for (int i = m / 2; i < c; ++i) {
				putchar('*');
			}
			puts("");
			return;
		}
	}

	if (c == 2) {
		if (m % 2 == 1 || m == 2) {
			puts("Impossible");
			return;
		} else {
			puts("c.");
			for (int i = 1; i < m / 2; ++i) {
				puts("..");
			}
			for (int i = m / 2; i < r; ++i) {
				puts("**");
			}
			return;
		}
	}

	// r, c >= 3
	if (m <= 3 || m == 5 || m == 7) {
		puts("Impossible");
		return;
	}

	bool swappedRC = false;
	if (r > c) {
		swap(r, c);
		swappedRC = true;
	}

	vector<string> vs(r);

	if (r * r <= m) {
		int cNeeded = m / r;
		int left = m % r;
		if (left == 0) {
			// r * cNeeded square
			for (int i = 0; i < r; ++i) {
				for (int j = 0; j < cNeeded; ++j) {
					vs[i].push_back('.');
				}
				for (int j = cNeeded; j < c; ++j) {
					vs[i].push_back('*');
				}
			}
		} else if (left == 1) {
			// rrr...rr(r-1)(2)
			for (int i = 0; i < 2; ++i) {
				for (int j = 0; j < cNeeded + 1; ++j) {
					vs[i].push_back('.');
				}
				for (int j = cNeeded + 1; j < c; ++j) {
					vs[i].push_back('*');
				}
			}

			for (int i = 2; i < r - 1; ++i) {
				for (int j = 0; j < cNeeded; ++j) {
					vs[i].push_back('.');
				}
				for (int j = cNeeded; j < c; ++j) {
					vs[i].push_back('*');
				}
			}

			for (int i = r - 1; i < r; ++i) {
				for (int j = 0; j < cNeeded - 1; ++j) {
					vs[i].push_back('.');
				}
				for (int j = cNeeded - 1; j < c; ++j) {
					vs[i].push_back('*');
				}
			}
		} else {
			// rrrr...rr(m%r)
			for (int i = 0; i < left; ++i) {
				for (int j = 0; j < cNeeded + 1; ++j) {
					vs[i].push_back('.');
				}
				for (int j = cNeeded + 1; j < c; ++j) {
					vs[i].push_back('*');
				}
			}
			for (int i = left; i < r; ++i) {
				for (int j = 0; j < cNeeded; ++j) {
					vs[i].push_back('.');
				}
				for (int j = cNeeded; j < c; ++j) {
					vs[i].push_back('*');
				}
			}
		}
	} else {
		int d = 0;
		for (d = 1; d * d < m; ++d);
		int cNeeded = m / d;
		int left = m % d;

		if (left == 0) {
			// dd..dd
			for (int i = 0; i < d; ++i) {
				for (int j = 0; j < cNeeded; ++j) {
					vs[i].push_back('.');
				}
				for (int j = cNeeded; j < c; ++j) {
					vs[i].push_back('*');
				}
			}
			for (int i = d; i < r; ++i) {
				for (int j = 0; j < c; ++j) {
					vs[i].push_back('*');
				}
			}
		} else if (left == 1) {
			// ddd..dd(d-1)(2)
			for (int i = 0; i < 2; ++i) {
				for (int j = 0; j < cNeeded + 1; ++j) {
					vs[i].push_back('.');
				}
				for (int j = cNeeded + 1; j < c; ++j) {
					vs[i].push_back('*');
				}
			}
			for (int i = 2; i < d - 1; ++i) {
				for (int j = 0; j < cNeeded; ++j) {
					vs[i].push_back('.');
				}
				for (int j = cNeeded; j < c; ++j) {
					vs[i].push_back('*');
				}
			}
			for (int i = d - 1; i < d; ++i) {
				for (int j = 0; j < cNeeded - 1; ++j) {
					vs[i].push_back('.');
				}
				for (int j = cNeeded - 1; j < c; ++j) {
					vs[i].push_back('*');
				}
			}
			for (int i = d; i < r; ++i) {
				for (int j = 0; j < c; ++j) {
					vs[i].push_back('*');
				}
			}
		} else {
			// ddddd(m%d)
			for (int i = 0; i < m % d; ++i) {
				for (int j = 0; j < cNeeded + 1; ++j) {
					vs[i].push_back('.');
				}
				for (int j = cNeeded + 1; j < c; ++j) {
					vs[i].push_back('*');
				}
			}
			for (int i = m % d; i < d; ++i) {
				for (int j = 0; j < cNeeded; ++j) {
					vs[i].push_back('.');
				}
				for (int j = cNeeded; j < c; ++j) {
					vs[i].push_back('*');
				}
			}
			for (int i = d; i < r; ++i) {
				for (int j = 0; j < c; ++j) {
					vs[i].push_back('*');
				}
			}
		}
	}

	vs[0][0] = 'c';
	if (swappedRC) {
		for (int j = 0; j < c; ++j) {
			for (int i = 0; i < r; ++i) {
				putchar(vs[i][j]);
			}
			puts("");
		}
	} else {
		for (int i = 0; i < r; ++i) {
			puts(vs[i].c_str());
		}
	}
}

int main() {
	int Tc;
	int r, c, m;
	scanf("%d", &Tc);
	for (int re = 1; re <= Tc; ++re) {
		scanf("%d%d%d", &r, &c, &m);
		printf("Case #%d:\n", re);
		gao(r, c, r * c - m);
	}
	return 0;
}