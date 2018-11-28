#include<cstdio>
#include<algorithm>
#include<vector>
using namespace std;

struct gr {
    int height, m, n;
};

bool operator<(gr a, gr b) {
    return a.height > b.height;
}

int main() {
    int z; scanf("%d", &z);
    int all = z;
    while(z--) {
        int rows[101];
        int cols[101];
        for (int i=0; i<101; i++) {
            rows[i] = cols[i] = 0;
        }
        vector<gr> a;
        int n, m; scanf("%d %d", &m, &n);
        for (int i=0; i<m; i++) {
            for (int j=0; j<n; j++) {
                gr t;
                scanf("%d ", &t.height);
                t.m = i;
                t.n = j;
                a.push_back(t);
            }
        }
        sort(a.begin(), a.end());
        bool poss = true;
        for (vector<gr>::iterator it=a.begin(); it!=a.end(); it++) {
            if (rows[it->m] > it->height && cols[it->n] > it->height)
                poss = false;
            else {
                rows[it->m] = max(rows[it->m], it->height);
                cols[it->n] = max(cols[it->n], it->height);
            }
        }
        if (poss) {
            printf("Case #%d: YES\n", all-z);
        } else {
            printf("Case #%d: NO\n", all-z);
        }
    }
}
