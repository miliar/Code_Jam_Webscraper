#include <cstdio>
#include <iostream>
#include <cstring>
#include <cctype>
#include <cmath>
#include <stack>
#include <string>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <queue>
using namespace std;
#define INF 0x3f3f3f3f
#define REP(i,n) for(int i=0; i<n; i++)
typedef long long int64;

int main() {
    int nt,r1,x;
    int us[30];

    scanf("%d",&nt);
    REP(ct,nt) {
        scanf("%d",&r1);

        memset(us,0,sizeof(us));
        REP(i,4)
            REP(j,4) {
                scanf("%d",&x);
                if (i==r1-1) us[x]++;
            }
        scanf("%d",&r1);
        REP(i,4)
            REP(j,4) {
                scanf("%d",&x);
                if (i==r1-1) us[x]++;
            }

        int qc=0, res;
        REP(i,16)
            if (us[i+1]==2) {
                res=i+1;
                qc++;
            }

        printf("Case #%d: ",ct+1);
        if (!qc) printf("Volunteer cheated!\n");
        else if (qc>1) printf("Bad magician!\n");
        else printf("%d\n",res);
    }
    return 0;
}

