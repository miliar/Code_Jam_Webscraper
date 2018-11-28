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

#define MAXN 1010

using namespace std;

char vet[MAXN];
char res[MAXN*2];

int main() {
//    freopen("A-large.in", "r", stdin);
//    freopen("A-large.out", "w", stdout);
    int t;
    scanf("%d", &t);
    int caso;
    for (caso=1; caso<=t; caso++) {
        int n;
        scanf("%s", vet+1);
        int ini=MAXN;
        int fim=MAXN;
        n=strlen(vet+1);
        res[ini]=vet[1];
        int i;
        for (i=2; i<=n; i++) {
            if (vet[i]>=res[ini]) {
                ini--;
                res[ini]=vet[i];
            }
            else {
                fim++;
                res[fim]=vet[i];
            }
        }
        fim++;
        res[fim]='\0';
        printf("Case #%d: %s\n", caso, res+ini);
    }
    return 0;
}






