// _template.cpp : Defines the entry point for the console application.
//

#include <cstdio>
#include <algorithm>
#include <iostream>
#include <vector>
#include <cmath>
#include <cstring>

typedef long long ll;
#define PI 3.1415926535897932384626433832795

using namespace std;

#define INF 10000000
#define MAX_VOC 600000
#define MAX_VOC_SIZE 30
#define MAXN 5000
#define MAXPEN 6
#define SHIFT 20


char w[MAX_VOC][MAX_VOC_SIZE];
int k;
int l[MAX_VOC];
char s[MAXN];

int f[MAXN][MAXPEN + 1];
int a[MAXN];

void read_voc() {
	freopen("garbled_email_dictionary.txt", "r", stdin);
	//freopen("short.txt", "r", stdin);
	k = 0;
	int tmp = 0;
	while (!feof(stdin)) {
		scanf("%s", w[k]);
		l[k] = strlen(w[k]);
		tmp = max(tmp, l[k]);
		k++;
	}

	//printf("read %i words, maxlen=%i\n", k, tmp);
	k--;
	//printf("last word = %s\n", w[k-1]);
}

int main()
{
	int tc = 0;
	read_voc();
	freopen("C-large.in", "r", stdin);	
	freopen("C-large.out", "w", stdout);
	gets(s);
	sscanf(s, "%i", &tc);

	for(int tt=1; tt<=tc; ++tt) {
		gets(s + SHIFT);
		int n = strlen(s + SHIFT);
		// init
		for(int i=0; i<SHIFT + n; ++i)
			for(int j=0; j<=MAXPEN; ++j) f[i][j] = INF;
		f[SHIFT-1][MAXPEN] = 0;

	//	printf("%s\n", s + SHIFT);

		int start = SHIFT;
		int finish = SHIFT + n;
		for(int i=start; i<finish; ++i) {
			for(int j=0; j<k; ++j) {
				int q = i - l[j] + 1;

				char *p1 = s + q;
				char *p2 = &w[j][0];

				int cnt = 0;
				bool ok = true;
				for(int t=0; t<l[j]; ++t, p1++, p2++) {
					if (*p1 != *p2) {
						a[cnt] = t;
						if (cnt) {
							if (t - a[cnt-1] < 5) {
								ok = false;
								break;
							}
						}
						cnt++;
					}

				}

				if (cnt==0) {
					for(int pen=0; pen<=MAXPEN; ++pen)
					{
						int newpen = pen + l[j];
						if (newpen > MAXPEN) newpen = MAXPEN;
						if (f[i][newpen] > f[q - 1][pen]) {
							f[i][newpen] = f[q - 1][pen];
						}
					}
				} else if (ok) { // cnt > 0
					for(int pen = 0; pen<=MAXPEN; ++pen) if (pen + a[0] + 1 >= 5) {
						int newpen = l[j] - a[cnt-1] - 1;
						if (newpen > MAXPEN) newpen = MAXPEN;
						if (f[i][newpen] > f[q - 1][pen] + cnt) {
							f[i][newpen] = f[q - 1][pen] + cnt;
						}
					}
				} // end of (cnt > 0)
			}
			if (i%100 == 0) fprintf(stderr, "%i\n", i);
		}

			int tmp = INF;
			for(int pen=0; pen<=MAXPEN; ++pen) {
				tmp = min(f[SHIFT + n - 1][pen], tmp);
			}
			printf("Case #%i: %i\n", tt, tmp);
	}
	return 0;
}

