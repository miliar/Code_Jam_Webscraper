#include <cstdio>
#include <iostream>
#include <algorithm>

using namespace std;

#define MAXN 100001
#define forn(i, n) for(int i = 0; i < (int)(n); ++i)

void main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int t;
	scanf("%d", &t);
	forn(tt, t) {
		printf("Case #%d: ", tt + 1);
		int n;
		cin >> n;
		double a[1234], b[1234];
		forn(i, n)
			cin >> a[i];
		forn(i, n)
			cin >> b[i];
		sort(a, a + n);
		sort(b, b + n);
		int y = 0;
		int i = n - 1, j = n - 1;
		while(i >= 0) {
			if (b[j] < a[i]) {
				--i;
				++y;
				continue;
			}
			--j, --i;
		}

		int z = 0;
		i = 0, j = 0;
		while(i < n) {
			if (a[i] < b[j]) {
				++i;
			} else {
				++j, ++i, ++z;
			}
		}
		printf("%d %d\n", z, y);
#if 0
		int r, c, m;
		cin >> r >> c >> m;
		printf("Case #%d:\n", tt + 1);
		if (r == 1 && c == 1) {
			if (m) {
				puts("Impossible");
			} else
				printf("c\n");
			continue;
		}
		if (r == 1 || c == 1) {
			if (m > r * c - 2) { puts("Impossible");continue; }
			int k = r * c - m - 2;
			forn(i, r){
				forn(j, c) {
					if (!i && !j)
						printf("c");
					else
						if (i <= 1 && j <= 1)
							printf(".");
						else{
							if (k) {
								printf(".");
								--k;
							} else
								printf("*");
						}
				}
				puts("");
			}
			continue;
		}
		if (m > r * c - 4) { puts("Impossible");continue; }
			int k = r * c - m - 4;
			forn(i, r){
				forn(j, c) {
					if (!i && !j)
						printf("c");
					else
						if (i <= 1 && j <= 1)
							printf(".");
						else{
							if (k) {
								printf(".");
								--k;
							} else
								printf("*");
						}
				}
				puts("");
			}
#endif
		/*
		double speed = 2.0, c, f, x;
		cin >> c >> f >> x;

		double res = 0;
		while(1) {
			double tm = x / speed;
			double tm2 = c / speed + x / (speed + f);
			if (tm + 1e-10 < tm2) {
				res += tm;
				break;
			}
			res += c / speed;
			speed += f;
		}
		*/


		/*
		int c[16];
		memset(c, 0, sizeof c);
		forn(p, 2) {
			int l;
			scanf("%d", &l);
			forn(i, 4)
				forn(j, 4) {
					int x;
					scanf("%d", &x);
					if (i + 1 == l)
						++c[x - 1];
			}
				
		}
		int k = 0, pp = -1;
		forn(i, 16)
			if (c[i] == 2)
				++k, pp = i + 1;
		printf("Case #%d: ", tt + 1);
		if (k == 0)
			printf("Volunteer cheated!");
		else
			if (k > 1)
				printf("Bad magician!");
			else
				printf("%d", pp);
		puts("");
		*/
	}
}