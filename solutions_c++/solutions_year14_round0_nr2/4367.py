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

		printf("Case #%d: ", tt + 1);
		printf("%.12lf", res);
		puts("");
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