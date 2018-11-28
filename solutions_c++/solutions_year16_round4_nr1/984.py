#include <cstdio>
#include <cmath>
#include <cstring>
#include <iostream>
#include <iomanip>
#include <set>
#include <stack>
#include <map>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

typedef long long ll;
typedef pair<int,int> pii;

const int NMAX = 10000 + 7;
const int INF = 1000000000;
char a[NMAX];
char b[NMAX];
int ca[15];
int cb[15];
int cc[15];

char test(int r,int p,int s, int n) {
	if (ca[n] == p && cb[n] == s && cc[n] == r) {
		return 'P';
	}
	if (ca[n] == s && cb[n] == r && cc[n] == p) {
		return 'S';
	}
	if (ca[n] == r && cb[n] == p && cc[n] == s) {
		return 'R';
	}
	return 0;
}

bool compare(int bl,int el,int br,int er) {
	for (int i=bl;i<el;i++) {
		if (a[i-bl+br] < a[i]) {
			return true;
		}
	}
	return false;
}

int main() {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t;


	ca[0] = 1;
	cb[0] = 0;
	cc[0] = 0;

	for (int i=1;i<=12;i++) {
		ca[i] = ca[i-1] + cb[i-1];
		cb[i] = cb[i-1] + cc[i-1];
		cc[i] = cc[i-1] + ca[i-1];
	}

	cin >> t;
	for (int testNumber = 1; testNumber <= t; testNumber++) {
		int n,r,p,s;
		cin >> n >> r >> p >> s;
		cout << "Case #" << testNumber << ": ";

		char first = test(r,p,s,n);

		if (first == 0) {
			cout << "IMPOSSIBLE";
			cout << endl;
			continue ;
		}
		a[0] = first;
		for (int i = 1;i <= n;i++) {
			int k = 0;
			for (int j=0;j < (1 << i); j++) {
				if (a[j] == 'R') {
					b[k++] = 'R';
					b[k++] = 'S';
				}
				if (a[j] == 'P') {
					b[k++] = 'P';
					b[k++] = 'R';
				}
				if (a[j] == 'S') {
					b[k++] = 'P';
					b[k++] = 'S';
				}
			}
			for (int j=0;j<k;j++) {
				a[j] = b[j];
			}
		}

		for (int i = 1;i < n;i++) {
			int step = (1 << i);
			for (int j = step;j < (1 << n); j+=step * 2) {
				if (compare(j-step,j,j,j+step)) {
					for (int k = j-step; k < j; k++) {
						b[k] = a[k];
					}
					for (int k = j-step; k < j; k++) {
						a[k] = a[k + step];
					}
					for (int k = j; k < j + step; k++) {
						a[k] = b[k - step];
					}
				}
			}
		}

		for (int i=0;i< (1<<n);i++) {
			cout << (char)a[i];
		}

		cout << endl;
	}
	return 0;
}