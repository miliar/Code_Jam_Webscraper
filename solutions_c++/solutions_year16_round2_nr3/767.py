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
#define MAXN 16

string v[MAXN][2];
vector< vector<int> > gEsq(MAXN), gDir(MAXN);
int vis[MAXN][2];

int main() {
//    freopen("C-small-attempt0.in", "r", stdin);
//    freopen("C-small-attempt0.out", "w", stdout);
    int t;
    cin >> t;
    int teste;
    for (teste=1; teste<=t; teste++) {
        int n;
        cin >> n;
        int i, j;
        for (i=0; i<n; i++) {
            gEsq[i].clear();
            gDir[i].clear();
            for (j=0; j<2; j++) {
                cin >> v[i][j];
            }
        }
        for (i=0; i<n; i++) {
            for (j=0; j<n; j++) {
                if (i!=j) {
                    if (v[i][0]==v[j][0]) {
                        gEsq[i].push_back(j);
                    }
                    if (v[i][1]==v[j][1]) {
                        gDir[i].push_back(j);
                    }
                }
            }
        }
        int res=0;
        int limite=(1<<n);
        int conj;
        for (conj=0; conj<limite; conj++) {
            memset(vis, 0, sizeof(vis));
            int quantReal=0;
            for (i=0; i<n; i++) {
                if ((conj & (1<<i))!=0) {
                    quantReal++;
                    for (j=0; j<gEsq[i].size(); j++) {
                        vis[gEsq[i][j]][0]=1;
                    }
                    for (j=0; j<gDir[i].size(); j++) {
                        vis[gDir[i][j]][1]=1;
                    }
                }
            }
            int quantVis=0;
            for (i=0; i<n; i++) {
                if ((conj & (1<<i))==0 && vis[i][0]==1 && vis[i][1]==1) {
                    quantVis++;
                }
            }
            if (quantReal+quantVis==n) {
                res=max(res, quantVis);
            }
        }
        printf("Case #%d: %d\n", teste, res);
    }
    return 0;
}
