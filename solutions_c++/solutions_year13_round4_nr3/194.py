#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include<string>
#include<vector>
#include<algorithm>
#include<map>
#include<set>
#include<utility>
#include<iostream>
#include<sstream>
#include<fstream>

using namespace std;

const double eps = 1e-8;
const double pi = acos(-1.0);
const int maxn = 3000;

int ntest;
int n;
int a[maxn], b[maxn], x[maxn];
int pa[maxn], pb[maxn];
int ok[maxn];

int main() {
	
	freopen("C-small-attempt1.in", "r", stdin);
	freopen("C-small-attempt1.out", "w", stdout);

	scanf("%d", &ntest);
	for(int test = 1; test <= ntest; test++) {
		scanf("%d", &n);
		for(int i=0; i<n; i++) scanf("%d", &a[i]);
		for(int i=0; i<n; i++) scanf("%d", &b[i]);
		
		memset(ok, 0, sizeof(ok));
		for(int i=0; i<n; i++) {
			pa[i] = 1;
			if(a[i] <= pa[i]) ok[i] |= 1;
		}
		for(int i=0; i<n; i++) {
			pb[i] = 1;
			if(b[i] <= pb[i]) ok[i] |= 2;
		}
		
		memset(x, -1, sizeof(x));
		for(int t=1; t<=n; t++) {
			for(int i=0; i<n; i++) if(ok[i] == 3 && x[i] == -1) {

				bool bb = true;
				for(int j=0; j<n; j++) if(ok[j] == 3 && x[j] == -1 && i!=j) {
					if(j < i && b[j] == b[i]) bb = false;
					if(j > i && a[j] == a[i]) bb = false;
				}

				if(!bb) continue;

				x[i] = t;

				for(int j=i+1; j<n; j++) {
					pa[j] = max(pa[j], a[i] + 1);
					if(a[j] <= pa[j]) ok[j] |= 1;
				}
				for(int j=0; j<i; j++) {
					pb[j] = max(pb[j], b[i] + 1);
					if(b[j] <= pb[j]) ok[j] |= 2;
				}

				break;
			}
		}

		printf("Case #%d:", test);
		for(int i=0; i<n; i++) printf(" %d", x[i]);
		printf("\n");
	}
	return 0;
}
