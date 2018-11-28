#include <stdio.h>
#include <string.h>

#define CLR(x,y) memset(x,y,sizeof(x));

const int N = 300+10;

int n,m;
char a[N][N];
bool vis[N][N];
int row[N],col[N],answer;

const int xx[] = {-1,1,0,0};
const int yy[] = {0,0,-1,1};


int D(char c) {
    switch(c) {
        case '^':return 0;
        case 'v':return 1;
        case '<':return 2;
        case '>':return 3;
    }
}

bool check() {
    memset(row,0,sizeof(row));
    memset(col,0,sizeof(col));
    for(int i = 1 ;i <= n ; ++i) {
        for(int j = 1 ; j <= m ; ++j) {
            if(a[i][j] != '.') {
                ++row[i];
                ++col[j];
            }
        }
    }
    //printf("%d",col[1]);
    for(int i = 1 ; i <= n ; ++i) {
        for(int j = 1 ; j <= m ; ++j) {
            if(a[i][j] != '.' && row[i] <= 1 && col[j] <= 1) {
                //printf("%d",col[j]);
                return false;
            }
        }
    }
    return true;
}

int work() {
    if(!check())return -1;
    CLR(vis,0);
    int res = 0;
    for(int i = 1; i <= n ; ++i) {
        for(int j = 1 ; j <= m ; ++j) {
            if(vis[i][j] || a[i][j] == '.')continue;
            int x = i;
            int y = j;
            while(true) {
                int d = D(a[x][y]);
                vis[x][y] = 1;
                do {
                    x = x + xx[d];
                    y = y + yy[d];
                }while(a[x][y] == '.');
                if(vis[x][y])break;
                if(a[x][y] == '#') {
                    ++res;
                    break;
                }
            }
        }
    }
    return res;
}

int main() {
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);
    int T;
    scanf("%d",&T);
    for(int cas = 1 ;cas <= T ; ++cas) {
        scanf("%d%d",&n,&m);
        memset(a,'#',sizeof(a));
        getchar();
        for(int i = 1 ; i <= n ; ++i) {
            gets(a[i]+1);
            a[i][m+1] = '#';
        }
        answer = work();
        printf("Case #%d: ",cas);
        if(answer>=0) {
            printf("%d\n",answer);
        } else {
            printf("IMPOSSIBLE\n");
        }
    }
}
