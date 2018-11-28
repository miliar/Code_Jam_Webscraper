#include <cstdio>

int l[105][105];

int main() {
    int t; scanf("%d", &t);
    for(int i=0; i<t; i++) {
        int n, m; scanf("%d %d", &n, &m);
        for(int j=0; j<n; j++) {
            for(int k=0; k<m; k++) {
                scanf("%d", &l[j][k]);
            }
        }
        for(int j=0; j<n; j++) {
            for(int k=0; k<m; k++) {
                int f=2;
                for(int x=0; x<n; x++) {
                    if(l[x][k]>l[j][k]) {
                        f--;
                        break;
                    }
                }
                for(int x=0; x<m; x++) {
                    if(l[j][x]>l[j][k]) {
                        f--;
                        break;
                    }
                }
                if(f==0) {
                    printf("Case #%d: NO\n", i+1);
                    goto next;
                }
            }
        }
        printf("Case #%d: YES\n", i+1);
        next:;
    }
}
