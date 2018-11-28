#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <list>
#include <set>
#include <map>
#include <string>
#include <iostream>

using namespace std;

#define INF 1000000007
#define MAXN 1010

int vet[MAXN];
int n;

int main() {
//    freopen("A-large.in", "r", stdin);
//    freopen("A-large_saida.txt", "w", stdout);
    int t;
    scanf("%d", &t);
    int teste;
    for (teste=1; teste<=t; teste++) {
        scanf("%d", &n);
        int i;
        for (i=1; i<=n; i++) {
            scanf("%d", &vet[i]);
        }
        int a=0;
        for (i=2; i<=n; i++) {
            if (vet[i]<vet[i-1]) {
                a+=vet[i-1]-vet[i];
            }
        }

        int maior=0;
        for (i=2; i<=n; i++) {
            maior=max(maior, vet[i-1]-vet[i]);
        }
        int b=0;
        int atual=vet[1];
        for (i=2; i<=n; i++) {
            if (atual>=maior) {
                b+=maior;
                atual=vet[i];
            }
            else {
                b+=atual;
                atual=vet[i];
            }
        }
        printf("Case #%d: %d %d\n", teste, a, b);
    }
    return 0;
}
