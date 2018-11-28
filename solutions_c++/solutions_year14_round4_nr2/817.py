#include <cstdio>
#include <iostream>
#include <string.h>
#include <cstring>
#include <algorithm>
//using namespace std;
const int maxn = 500010;

int n, m, testnum;
int a[maxn];
int b[maxn];
int c[maxn];

using namespace std;

bool cmp(int a, int b) {
	return a > b;
}

int main() {
	freopen("B-large.in.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &testnum);

	for (int test = 1; test <= testnum; test++) {
		scanf("%d", &n);
		int maxi = 0; a[maxi] = 0;
		for (int i = 1; i <= n; i++) {
			scanf("%d", &a[i]);
		}
		/*int ans = 1000000;
		b[0] = 0; c[n + 1] = 0;
		for (int i = 1; i <= n; i++) {
			b[i] = 0; 
			for (int j = i - 1; j >= 1; j--)
				if (a[i] < a[j]) b[i]++;
			b[i] = b[i - 1] + b[i];
		}
		for (int i = n; i >= 1; i--) {
			c[i] = 0;
			for (int j = i + 1; j <= n; j++)
				if (a[i] < a[j]) c[i]++;
			c[i] = c[i + 1] + c[i];
		}
		for (int i = 1; i <= n; i++) {
			printf("%d ", c[i]);
			int j = b[i - 1] + c[i];
			if (j < ans) ans = j;
		}*/
		int ll = 1; 
		int rr = n;
		int ans = 0;
		for (int i = 1; i <= n - 1; i++) {
			int mini = ll;
			for (int j = ll; j <= rr; j++)
				if (a[j] < a[mini]) {
					mini = j;
				}

			if (mini - ll < rr - mini) {
				ans+= mini - ll;
				for (int j = mini; j > ll; j--)
					a[j] = a[j - 1];
				ll++; 
			} else {
				ans+= rr - mini;
				for (int j = mini; j < rr; j++)
					a[j] = a[j + 1];
				rr--; 
			}
			/*for (int j = ll; j <= rr; j++)
				printf("%d ", a[j]);
			printf("\n");*/
			//printf("%d %d %d %d \n", ll, rr, mini, ans);
		}




		
		printf("Case #%d: %d\n", test, ans);
	}
}