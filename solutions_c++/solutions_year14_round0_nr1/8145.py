#include <set>
#include <map>
#include <stack>
#include <cmath>
#include <ctime>
#include <queue>
#include <string>
#include <vector>
#include <cstdio>
#include <sstream>
#include <cstring>
#include <climits>
#include <cstring>
#include <iostream>
#include <algorithm>
#define ff first
#define ss second
#define LL long long
#define pb push_back
#define mp make_pair
#define sqr(x) ((x) * (x))
#define PI 3.1415926535897932384626433832795
using namespace std;

int main() {
	
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small-attempt0.out", "w", stdout);
	
	int i, j, l, k, n, t, ans, T = 1, con, a[5], tmp[5];
	scanf("%d", &t);
	while(t--) {
		scanf("%d", &n);
		for (i = 1; i <= 4; i++)
		for (j = 1; j <= 4; j++) {
			scanf("%d", &k);
			if (i == n) tmp[j] = k;
		}
		scanf("%d", &n); con = 0; ans = -1;
		for (i = 1; i <= 4; i++) {
			for (j = 1; j <= 4; j++) scanf("%d", &a[j]);
			if (i == n) {
				for (j = 1; j <= 4; j++)
				for (l = 1; l <= 4; l++) 
					if(a[j] == tmp[l]) con++, ans = a[j];
			}
		}
		cout << "Case #"<< T++ << ": ";
		if (con == 1) cout << ans << endl;
		if (!con) cout << "Volunteer cheated!" << endl;
		if(con > 1) cout << "Bad magician!" << endl;
	}
	return 0;
}

