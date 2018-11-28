#include <stdio.h>
#include <algorithm>
#include <assert.h>
#include <string>
#include <cstring>
#include <map>
#include <set>
#include <vector>
#include <iostream>
#include <queue>
using namespace std;

typedef long long LL;
#define tr(container, it)for(typeof(container.begin()) it = container.begin(); it != container.end(); it++)

int GCD (int a, int b) { if (!a) return b; return GCD(b%a, a);}

int val[11];
int num[3];
int r,n,m,k;

bool solve() {
    int n[3];
    vector<int>prod;
    for (int i = 0; i < 8; i++) {
        n[0] = n[1] = n[2] = 0;
        for (int j = 0; j < 3; j++) {
            if ((i & (1<<j)) > 0) {
                n[j] = 1;
            }
        }
        LL p = 1;
        for (int i = 0; i < 3; i++) {
            if (n[i]) p *= num[i];
        }
        prod.push_back(p);
    }
    for (int i = 0; i < k; i++) {
        int v = val[i];
        bool pos = false;
        for (int i = 0; i < prod.size(); i++) {
            if (v == prod[i]) pos = true;
        }
        if (!pos) return false;
    }
    return true;
}

int main() {
    int ttt; scanf("%d", &ttt);

    cin>>r>>n>>m>>k;
    printf("Case #1:\n");
    for (int _tests = 1; _tests <= r; _tests++) {
        for (int i = 0; i < k; i++) {
            cin>>val[i];
        }
        bool ans = false;
        for (int i = 2; i <= m; i++) {
            for (int j = 2; j <= m; j++) {
                for (int k = 2; k <= m; k++) {
                    num[0] = i;
                    num[1] = j;
                    num[2] = k;
                    if (solve()) {
                        ans = true;break;
                    }
                }
                if (ans) break;
            }
            if (ans) break;
        }
        cout<<num[0]<<num[1]<<num[2]<<"\n";
    }
	return 0;
}
