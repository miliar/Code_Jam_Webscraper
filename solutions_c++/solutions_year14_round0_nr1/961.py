
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <set>
#include <string>
#include <map>

using namespace std;

#define rep(i,n) for(int i=0; i<(n); i++)
#define repf(i,a,b) for (int i=(a); i<=(b); i++)
#define repb(i,a,b) for(int i=(a); i>=(b); i--)


int ba[4][4],bb[4][4];

int main(int argc, char **argv) {
    int T,a,b;
    cin >> T;
    rep(tc, T) {
        cin >> a;
        rep(i,4) rep(j,4) cin >> ba[i][j];
        cin >> b;
        rep(i,4) rep(j,4) cin >> bb[i][j];
        set<int> v;
        a--; b--;
        rep(i,4) rep(j,4) if (ba[a][i] == bb[b][j]) v.insert(ba[a][i]);
        printf("Case #%d: ",tc+1);
        if (v.size() == 1) {
            printf("%d\n",*(v.begin()));
        } else if (v.size() > 1) {
            printf("Bad magician!\n");
        } else {
            printf("Volunteer cheated!\n");
        }
    }
}

