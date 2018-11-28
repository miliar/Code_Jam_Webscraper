#include<cstdio>
#include<algorithm>
using namespace std;
int tc,n,m,togo[99],cnt;
int mp[22][22];

int dx[4] = {1,0,0,-1};
int dy[4] = {0,1,-1,0};

void print() {
    for(int i=1;i<=n;i++) {
        for(int j=1;j<=m;j++) {
            printf("%c",mp[i][j]==1?'\\':'/');
        }
        puts("");
    }
}

bool valid(int X,int Y) {
    if(X<1 || X>n) return false;
    if(Y<1 || Y>m) return false;
    return true;
}

int met(int X,int Y,int D) {
    if(!valid(X,Y)) return mp[X][Y];
    int nd = D^mp[X][Y];
    return met(X+dx[nd],Y+dy[nd],nd);
}

bool simulate(int idx) {
    int i,j,k=idx;
    for(i=1;i<=n;i++) {
        for(j=1;j<=m;j++) {
            mp[i][j] = k%2+1;
            k/=2;
        }
    }
    for(i=1;i<=m;i++) {
        if(met(1,i,0) != togo[mp[0][i]]) return false;
    }
    for(i=1;i<=n;i++) {
        if(met(i,m,2) != togo[mp[i][m+1]]) return false;
    }
    for(i=m;i>=1;i--) {
        if(met(n,i,3) != togo[mp[n+1][i]]) return false;
    }
    for(i=n;i>=1;i--) {
        if(met(i,1,1) != togo[mp[i][0]]) return false;
    }
    return true;
}

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int i,j,q;
    scanf("%d",&tc);
    for(q=1;q<=tc;q++) {
        printf("Case #%d:\n",q);
        scanf("%d%d",&n,&m);
        cnt = 0;
        for(i=1;i<=m;i++) mp[0][i] = ++cnt;
        for(i=1;i<=n;i++) mp[i][m+1] = ++cnt;
        for(i=m;i>=1;i--) mp[n+1][i] = ++cnt;
        for(i=n;i>=1;i--) mp[i][0] = ++cnt;
        for(i=1;i<=(n+m);i++) {
            int A,B;
            scanf("%d%d",&A,&B);
            togo[A] = B;
            togo[B] = A;
        }
        bool flag = false;
        for(i=0;i<(1<<(n*m));i++) {
            if(simulate(i)) {
                print();
                flag = true;
                break;
            }
        }
        if(!flag) puts("IMPOSSIBLE");
    }
}
