#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <stdio.h>
#include <algorithm>
#include <cmath>
#include <string>
#include <vector>
#include <map>

#define sqr(a) (a) * (a)
#define INF 9900000
#define N 200


using namespace std;

bool fail;
bool used[N];
char a[N][N], b[N][N];
int i, j, tt, t, n, m;
int counter, ans;
int c[N];



void copyy() {
	int i, j;
	for (i = 1; i <= n; i++)
		for (j = 1; j <= n; j++)
			b[i][j] = a[i][j];
}

void gen(int i) {
	bool left = true;
	if (i > n)
        return;
	for (int j = 1; j <= n; j++) {
		if (b[c[i]][j] == '1' && !used[j]) {
			used[j] = true;
			gen(i + 1);
			used[j] = false;
			left = false;
		}
	}
	if (left)
		fail = true;
}

bool ok(int counter) {
	fail = false;

    int f = 1;
    for (int i = 1; i <= n; i++) {
        c[i] = i;
        f *= i;
    }

    while (f--) {
        gen(1);
        next_permutation(c+  1, c+ n+ 1);
    }
    /*	if (fail == false) {
	    cout << "result with " << counter <<":\n";
	    for (i = 1; i <= n; i++) {
        for (j = 1; j <= n; j++)
            cout <<b[i][j];
        cout <<endl;
	}
	cout << endl;
        if (counter == 2) {
            gen(1);
        }

	}
	*/
	return fail == false;
}

int main()  {

    #ifndef ONLINE_JUDGE
    freopen("a.in", "r" , stdin);
    freopen("a.out", "w", stdout);
    #endif

    scanf("%d\n", &t);
    for (tt = 1; tt <= t; tt++) {
    	scanf("%d\n", &n);
    	for (i = 1; i <= n; i++) {
    		for (j = 1; j <= n; j++)
    			scanf("%c", &a[i][j]);
            scanf("\n");
    	}

		m = n * n;
		ans = INF;

		for (int msk = 0; msk < (1 << m); msk++) {
			copyy();
			counter = 0;
			for (j = 0; j < m; j++)
				if ((msk & (1 << j)) > 0) {
					int ii = (j + 1) / n + ((j + 1) % n != 0);
    	            int jj = (j + 1) % n;
    	            if (!jj)
                        jj = n;
        	       	b[ii][jj] = '1';
        	       	counter++;
				}

			if (ok(counter))
				ans = min(ans, counter);
		}
		cout << "Case #"<<tt<<": " << ans<<endl;
    }

    return 0;
}
