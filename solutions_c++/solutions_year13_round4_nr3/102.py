#include <stdio.h>
#include <vector>
using namespace std;
int a[2010], b[2010], d[2010], u[2010], d0[2010], d1[2010];
vector<int> e[2010], e0[2010], e1[2010];
int c[2010];
int main(){
    int T, ri = 1, n, i, j;
    freopen("C-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    scanf("%d", &T);
    while (T--){
        scanf("%d", &n);
        for (i = 0; i < n; i++) scanf("%d", &a[i]);
        for (i = 0; i < n; i++) scanf("%d", &b[i]);
        for (i = 0; i < n; i++){
            d[i] = u[i] = 0;
            d0[i] = d1[i] = 0;
            e[i].clear();
            e0[i].clear();
            e1[i].clear();
        }
        for (i = 0; i < n; i++){
            for (j = 0; j < i; j++){
                if (a[j] >= a[i]){
                    e[i].push_back(j);
                    d[j]++;
                }else if (a[j] == a[i] - 1){
                    d0[i] = 1;
                    e0[j].push_back(i);
                }
            }
            for (j = i + 1; j < n; j++){
                if (b[j] >= b[i]){
                    e[i].push_back(j);
                    d[j]++;
                }else if (b[j] == b[i] - 1){
                    d1[i] = 1;
                    e1[j].push_back(i);
                }
            }
        }
        for (j = 0; j < n; j++){
            for (i = 0; i < n; i++){
                if (d[i] == 0 && u[i] == 0 && d0[i] == 0 && d1[i] == 0){
                    break;
                }
            }
            c[i] = j + 1;
            u[i] = 1;
            for (int k = 0; k < (int)e[i].size(); k++){
                d[e[i][k]]--;
            }
            for (int k = 0; k < (int)e0[i].size(); k++){
                d0[e0[i][k]] = 0;
            }
            for (int k = 0; k < (int)e1[i].size(); k++){
                d1[e1[i][k]] = 0;
            }
        }
        printf("Case #%d:", ri++);
        for (i = 0; i < n; i++) printf(" %d", c[i]);
        printf("\n");
    }
    return 0;
}
