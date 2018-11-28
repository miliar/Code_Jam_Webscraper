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

int n,m;
int lcp[10][10], len[10],q[10],p[10][10];
char s[10][20];
int res,qr;

void busca(int x) {
    if (x==m) {
        int acc=0;

        REP(i,n) {
            if (q[i]) acc++;
            REP(j,q[i]) {
                acc+=len[p[i][j]];
                int mxl=0;
                REP(k,j)
                    mxl=max(mxl,lcp[p[i][k]][p[i][j]]);

                acc-=mxl;
            }
        }

        if (acc>res) { res=acc; qr=1; }
        else if (acc==res) qr++;
        return;
    }

    REP(i,n) {
        p[i][q[i]++]=x;
        busca(x+1);
        q[i]--;
    }
}

int main() {
    int nt;

    scanf("%d",&nt);
    REP(ct,nt) {
        scanf("%d%d",&m,&n);
        REP(i,m) {
            scanf(" %s",s[i]);
            len[i]=strlen(s[i]);
        }

        memset(lcp,0,sizeof(lcp));
        REP(i,m)
            REP(j,m)
                REP(k,min(len[i],len[j])) {
                    if (s[i][k]==s[j][k]) lcp[i][j]=k+1;
                    else break;
                }

        res=-1;
        busca(0);

        printf("Case #%d: %d %d\n",ct+1,res,qr);
    }
    return 0;
}

