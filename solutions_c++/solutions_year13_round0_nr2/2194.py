#include <cstdio>
#include <vector>
#include <map>
#include <iostream>
#include <algorithm>
#include <queue>

using namespace std;

int b[102][102], a[102][102];

bool used[102][102];
int n, m;

struct mst {
    int val;
    int y, x;
    mst(){}
    mst(int a, int b, int c) {
        val=a, y=b, x=c;
    }
    bool operator<(mst m) const {return val > m.val;}
};
mst d[102*102];

bool col(int y, int x) {
    int num = a[y][x];
    for (int i = 0; i < n; i++) {
        if (a[i][x] > num) return 0;
    }
    return 1;
}

bool row(int y, int x) {
    int num = a[y][x];
    for (int i = 0; i < m; i++) {
        if (a[y][i] > num) return 0;
    }
    return 1;
}

int main() {
    freopen("input.txt", "r" , stdin);
    freopen("output.txt", "w", stdout);

    int test; cin >> test;
    priority_queue<mst> h;

    for (int it = 0; it < test; it++) {
        cin >> n >> m;
        int len = 0;
        for (int i = 0 ; i < n; i++) {
            for (int j = 0; j < m; j++) {
                cin >> a[i][j];
                d[len++] = mst(a[i][j], i, j);
                used[i][j] = 0;
            }
        }

        sort(d, d + len);
     //   cout << len << endl;
       int ok = 1;

        for (int i = 0; i < len; i++) {
            int y = d[i].y, x = d[i].x;
          //  cerr << d[i].val << endl;
            bool c = col(y, x) | row(y, x);
            if (!c) {
				ok = 0;
                printf("Case #%d: NO\n", it + 1);
                break;
            }



		}
		if (ok) {
			printf("Case #%d: YES\n", it + 1);

		}
    }
	return 0;
}
