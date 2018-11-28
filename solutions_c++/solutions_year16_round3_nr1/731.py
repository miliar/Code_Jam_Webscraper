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

#define MAXN 40

int p[MAXN];

int main() {
//    freopen("A-large.in", "r", stdin);
//    freopen("A-large.out", "w", stdout);
    int t;
    scanf("%d", &t);
    int caso;
    for (caso=1; caso<=t; caso++) {
        int n;
        scanf("%d", &n);
        int i;
        for (i=0; i<n; i++) {
            scanf("%d", &p[i]);
        }
        printf("Case #%d:", caso);
        while (true) {
            vector<int> res;
            int quant, maior;
            quant=0;
            maior=-1;
            for (i=0; i<n; i++) {
                if (p[i]>maior) {
                    res.clear();
                    res.push_back(i);
                    maior=p[i];
                }
                else if (p[i]==maior) {
                    res.push_back(i);
                }
                if (p[i]>0) {
                    quant++;
                }
            }
            if (quant==0) {
                break;
            }
            if (quant==2 && res.size()==2) {
                printf(" %c%c", res[0]+'A', res[1]+'A');
                p[res[0]]--;
                p[res[1]]--;
            }
            else {
                printf(" %c", res[0]+'A');
                p[res[0]]--;
            }
        }
        printf("\n");
    }
    return 0;
}






