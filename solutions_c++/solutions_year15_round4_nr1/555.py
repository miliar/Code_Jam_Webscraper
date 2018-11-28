#include <bits/stdc++.h>
using namespace std;
#define REP(i,n) for(int i=0;i<int(n);++i)
#define out(x) cout<<#x"="<<x<<endl
char a[123][123];
int dx[]={ 1, 0,-1, 0};
int dy[]={ 0, 1, 0,-1};
int n, m;
bool inside(int i, int j){
    return i>=0 && j>=0 && i<n && j<m;
}
int get(char c){
    int id;
    switch (c) {
        case 'v': id=0; break;
        case '>': id=1; break;
        case '^': id=2; break;
        case '<': id=3; break;
    }
    return id;
}
bool ok(int x, int y, int id){
    do {
        x = x + dx[id];
        y = y + dy[id];
        if(!inside(x,y))return false;
        if(a[x][y]!='.')return true;
    } while(true);
}
int calc(){
    int ans=0;
    REP(i,n)REP(j,m)if(a[i][j]!='.'){
        int id=get(a[i][j]);
        if(!ok(i, j, id)){
            bool flag=0;
            REP(k, 4)if(k!=id && ok(i,j,k)){
                flag=1;
                break;
            }
            if(flag){
                ans++;
                //out(i);
                //out(j);
            } else return -1;
        }
    }
    return ans;
}
int main(){
    int T;
    scanf("%d",&T);
    REP(tt,T){
        scanf("%d%d ",&n,&m);
        REP(i,n)gets(a[i]);
        int ans=calc();
        printf("Case #%d: ", tt+1);
        if(~ans)printf("%d\n", ans);
        else puts("IMPOSSIBLE");
    }
}
