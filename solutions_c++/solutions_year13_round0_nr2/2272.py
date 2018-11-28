#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <queue>
#include <algorithm>
#include "stdio.h"
#include "stdlib.h"
#include "string.h"
#include "math.h"
using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef vector<double> vd;
typedef pair<int, int> ii;
typedef vector<ii> vii;

#define REP(i, a, b) \
    for(int i=int(a); i<int(b); ++i)

int main()
{
    FILE *fout = fopen("test.out", "w");
    int tc, cn=1, n, m, maxx[101], maxy[101], table[101][101];
    bool br;
    scanf("%d", &tc);
    while(tc--){
        memset(maxx,0,sizeof(maxx));
        memset(maxy,0,sizeof(maxy));
        br=false;
        scanf("%d %d", &n, &m);
        REP(i,0,n){
            REP(j,0,m){
                scanf("%d", &table[i][j]);
                if(table[i][j]>maxx[i])
                    maxx[i]=table[i][j];
                if(table[i][j]>maxy[j])
                    maxy[j]=table[i][j];
            }
        }
        REP(i,0,n){
            REP(j,0,m){
                if(table[i][j]<maxx[i] && table[i][j]<maxy[j]){
                    br=true;
                    break;
                }
            }
            if(br)
                break;
        }
        if(br)
            fprintf(fout, "Case #%d: NO\n", cn++);
        else
            fprintf(fout, "Case #%d: YES\n", cn++);
    }

    return 0;
}
