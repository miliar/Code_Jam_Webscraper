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
#define MAXN 2010

string vet[10]={"SIX", "ZERO", "TWO", "EIGHT", "SEVEN", "FIVE", "FOUR", "NINE", "THREE", "ONE"};
int num[10]={6, 0, 2, 8, 7, 5, 4, 9, 3, 1};
char s[MAXN];
int quant[1000];


int main() {
//    freopen("A-large.in", "r", stdin);
//    freopen("A-large.out", "w", stdout);
    int t;
    scanf("%d", &t);
    int teste;
    for (teste=1; teste<=t; teste++) {
        scanf("%s", s+1);
        int n=strlen(s+1);
        vector<int> res;
        int i, j;
        memset(quant, 0, sizeof(quant));
        for (i=1; i<=n; i++) {
            quant[s[i]]++;
        }
        for (i=0; i<10; i++) {
            int menor=INF;
            for (j=0; j<vet[i].size(); j++) {
                menor=min(menor, quant[vet[i][j]]);
            }
            for (j=0; j<menor; j++) {
                res.push_back(num[i]);
            }
            for (j=0; j<vet[i].size(); j++) {
                quant[vet[i][j]]-=menor;
            }
        }
        sort(res.begin(), res.end());
        printf("Case #%d: ", teste);
        for (i=0; i<res.size(); i++) {
            printf("%d", res[i]);
        }
        printf("\n");
    }
    return 0;
}
