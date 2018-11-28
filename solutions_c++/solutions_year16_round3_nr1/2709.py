#include "stdafx.h"
#include <iostream>
#include <cstdio>
#include <algorithm>
#include <map>
#include <string>
using namespace std;
const int N = 26;
int a[N];
int main (int argc, char** argv) {
	freopen ("in.txt", "r", stdin);
	freopen ("out.txt", "w", stdout);
	int t;
	scanf (" %d", &t);
	for (int qq = 1; qq <= t; qq++) {
		int n;
		scanf(" %d", &n);
		int all = 0;
		for (int it = 0; it < n; it++) {
			scanf(" %d", &a[it]);
			all += a[it];
		}
		printf("Case #%d:", qq);
		int ev = 0;
		while (ev < all) {
			for (int i = 0; i < n; i++) {
				if (a[i] <= 0) continue;
				int s = 0;
				for (int j = 0; j < n; j++) {
					if (a[j] <= 0) continue;
					s += a[j];
				}
				bool ready = true;
				for (int j = 0; j < n; j++) {
					if (a[j] <= 0) continue;
					int m;
					if (j == i) {
						m = a[j] - 1; 
					}
					else m = a[j];
					if ( (double) m / (double) (s - 1) > 0.5 ) {
						ready = false;
						break;
					}
				}
				if (ready) {
						a[i]--;
						ev += 1;
						printf(" %c", i + 'A');
						break;
				}
				for (int k = i; k < n; k++) {
					if (a[k] <= 0) continue;
					bool secready = true;
					for (int l = 0; l < n; l++) {
						int m2;
						if (l == k && l == i) m2 = a[l] - 2;
						else if (l == k || l == i) m2 = a[l] - 1;
						else m2 = a[l];
						if ( (double) m2 / (double) (s - 2) > 0.5 ) {
							secready = false;
							break;
						}
					}
					if ( secready ) {
						a[i]--;
						a[k]--;
						ev += 2;
						printf(" %c%c", i + 'A',  k + 'A');
						break;
					}
				}
			}
		}
		printf("\n");
	}
	return 0;
}