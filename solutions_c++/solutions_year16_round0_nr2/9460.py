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
#define MAXN 110

using namespace std;

char vet[MAXN];

int main() {
//    freopen("B-large.in", "r", stdin);
//    freopen("B-large.out", "w", stdout);
    int t;
    scanf("%d", &t);
    int caso;
    for (caso=1; caso<=t; caso++) {
        int n;
        scanf("%s", vet+1);
        n=strlen(vet+1);
        int i, j, k;
        int res=0;
        for (i=1; i<=n-1; i++) {
            if (vet[i]!=vet[i+1]) {
                res++;
            }
        }
        if (vet[n]=='-') {
            res++;
        }
        printf("Case #%d: %d\n", caso, res);
    }
    return 0;
}






