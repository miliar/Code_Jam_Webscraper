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
#define MAXB 1010

typedef long long LL;

LL vet[MAXB];

int main() {
//    freopen("B-small-attempt0.in", "r", stdin);
//    freopen("B-small-attempt0_saida.txt", "w", stdout);
    LL t;
    scanf("%lld", &t);
    LL teste;
    for (teste=1; teste<=t; teste++) {
        LL b, n;
        scanf("%lld %lld", &b, &n);
        LL i;
        for (i=1; i<=b; i++) {
            scanf("%lld", &vet[i]);
        }

        LL ini, fim, meio, cand;
        ini=0;
        fim=100000000000010LL;
        cand=-1;
        while (ini<=fim) {
            LL meio=(ini+fim)/2;
            LL soma=0;
            LL quant=b;
            for (i=1; i<=b; i++) {
                soma+=meio/vet[i];
                if (meio%vet[i]==0) {
                    quant--;
                }
            }
            if (soma+quant<n) {
                ini=meio+1;
                cand=meio;
            }
            else {
                fim=meio-1;
            }
        }
        LL soma=0;
        LL quant=b;
        for (i=1; i<=b; i++) {
            soma+=cand/vet[i];
            if (cand%vet[i]==0) {
                quant--;
            }
        }
        LL pos=n-(soma+quant);
        LL res;
        for (i=1; i<=b; i++) {
            if (cand%vet[i]==0) {
                if (pos==1) {
                    res=i;
                    break;
                }
                pos--;
            }
        }
        printf("Case #%lld: %lld\n", teste, res);
    }
    return 0;
}
