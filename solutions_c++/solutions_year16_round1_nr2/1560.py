#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <sstream>
#include <vector>
#include <list>
#include <deque>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <utility>
#include <algorithm>
#include <limits>
#include <iomanip>

#define INF 1000000007

using namespace std;

#define MAXN 60

int quant[3000];
int vet[MAXN];

int main() {
//    freopen("B-large.in", "r", stdin);
//    freopen("B-large.out", "w", stdout);
    int t;
    scanf("%d", &t);
    int caso;
    for (caso=1; caso<=t; caso++) {
        int n;
        scanf("%d", &n);
        int i, j;
        memset(quant, 0, sizeof(quant));
        for (i=1; i<=2*n-1; i++) {
            for (j=1; j<=n; j++) {
                scanf("%d", &vet[j]);
                quant[vet[j]]++;
            }
        }
        vector<int> res;
        for (i=1; i<=2500; i++) {
            if (quant[i]%2==1) {
                res.push_back(i);
            }
        }
        printf("Case #%d:", caso);
        for (i=0; i<n; i++) {
            printf(" %d", res[i]);
        }
        printf("\n");
    }
    return 0;
}






