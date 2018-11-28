#include <iostream>
#include <cstdio>
#include <cmath>
#include <string>
#include <sstream>
#include <cstring>
#include <vector>
#include <map>
#include <set>
using namespace std;

int n;
double a[10000], b[10000];
bool mark[10000];

int play(double *a, double *b) {
    memset(mark, 0, sizeof(mark));
    int ret = 0;
    for (int i = 0; i < n; i++) {
        bool flag = false;
        for (int j = 0; j < n; j++)
            if (!mark[j] && b[j] > a[i]) {
                flag = true;
                mark[j] = true;
                break;
            }
        if (!flag) {
            for (int j = 0; j < n; j++)
                if (!mark[j]) {
                    mark[j] = true;
                    ret++;
                    break;                    
                }
        }
    }    
    return ret;
}

int play_d(double *a, double *b) {
    memset(mark, 0, sizeof(mark));
    int ret = 0;
    for (int i = 0; i < n; i++) {
        bool flag = false;
        for (int j = 0; j < n; j++)
            if (!mark[j] && a[j] > b[i]) {
                flag = true;
                mark[j] = true;
                ret++;
                break;
            }
        if (!flag) {
            for (int j = 0; j < n; j++)
                if (!mark[j]) {
                    mark[j] = true;
                    break;                   
                }
        }
    }    
    return ret;
}

int main() {    
    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; t++) {
        scanf("%d", &n);
        for (int i = 0; i < n; i++) scanf("%lf", a + i);
        for (int i = 0; i < n; i++) scanf("%lf", b + i);
        sort(a, a + n);
        sort(b, b + n);
        int v1 = play_d(a, b);
        int v2 = play(a, b);
        printf("Case #%d: ", t);
        printf("%d %d", v1, v2);
        printf("\n");
    }
}

