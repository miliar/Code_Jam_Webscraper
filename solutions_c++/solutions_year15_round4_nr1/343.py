#include<bits/stdc++.h>
#define MAX   227
#define FOR(i,a,b) for (int i=(a),_b=(b);i<=_b;i=i+1)
#define REP(i,n) for (int i=0,_n=(n);i<_n;i=i+1)
using namespace std;
const char noAns[]="IMPOSSIBLE";
char a[MAX][MAX];
int m,n;
const char ch[]="^>v<";
const int dx[]={-1,0,1,0};
const int dy[]={0,1,0,-1};
bool isArrow(char c) {
    REP(i,4) if (ch[i]==c) return (true);
    return (false);
}
bool inside(int x,int y) {
    if (x<1 || x>m || y<1 || y>n) return (false);
    return (true);
}
bool haveArrow(int x,int y,int dir) {
    while (true) {
        x+=dx[dir];
        y+=dy[dir];
        if (!inside(x,y)) return (false);
        if (isArrow(a[x][y])) return (true);
    }
}
void process(int tc) {
    scanf("%d%d",&m,&n);
    FOR(i,1,m) scanf("%s",a[i]+1);
    int res=0;
    FOR(i,1,m) FOR(j,1,n) if (isArrow(a[i][j])) {
        bool ok=false;
        REP(d,4) if (haveArrow(i,j,d)) ok=true;
        if (!ok) {
            printf("Case #%d: %s\n",tc,noAns);
            return;
        }
        res++;
        REP(d,4) if (a[i][j]==ch[d] && haveArrow(i,j,d)) res--;
    }
    printf("Case #%d: %d\n",tc,res);
}
int main(void) {
    int t;
    scanf("%d",&t);
    FOR(i,1,t) process(i);
    return 0;
}
