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

char vet[MAXN];

int main() {
//    freopen("A-large.in", "r", stdin);
//    freopen("A-large_saida.txt", "w", stdout);
    int t;
    scanf("%d", &t);
    int teste;
    for (teste=1; teste<=t; teste++) {
        int n;
        scanf("%d %s", &n, vet);
        int soma=vet[0]-'0';
        int res=0;
        int i;
        for (i=1; i<=n; i++) {
            if (vet[i]!='0') {
                if (soma<i) {
                    res+=i-soma;
                    soma=i;
                }
                soma+=vet[i]-'0';
            }
        }
        printf("Case #%d: %d\n", teste, res);
    }
    return 0;
}
