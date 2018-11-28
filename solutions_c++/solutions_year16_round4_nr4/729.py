#include<cstdio>
#include<cmath>
#include<iostream>
#include<algorithm>
#include<cstring>
#include<vector>
#include<queue>
#include<map>
#include<set>
#include<list>
using namespace std;
#define INF (1<<29)
#define min(x,y) (((x)<(y))?(x):(y))
#define max(x,y) (((x)>(y))?(x):(y))
#define FOR(i,x,y) for(int i=(x);i<(y);++i)
#define FOE(i,x,y) for(int i=(x);i<=(y);++i)
#define FIT(it,x) for(typeof(x.begin()) it=x.begin(); it!=x.end(); ++it)
#define CLR(i) memset(i,0,sizeof(i))
#define eps (1e-8)
#define feq(x,y) (fabs((x)-(y))<=eps)
#define fgt(x,y) (((x)-(y)) > eps)
#define flt(x,y) (((y)-(x)) > eps)
#define fgeq(x,y) (fgt(x,y) || feq(x,y))
#define fleq(x,y) (flt(x,y) || feq(x,y))
#define ll long long

int T,N;
bool init[5][5];
bool a[5][5];
char s[100];
int order[5];
bool use[5];

bool check(int x){
    if (x == N){
        return 1;
    }

    bool found = 0;
    FOR(i,0,N){
        if (a[order[x]][i] && !use[i]){
            found = 1;
            use[i] = 1;
            bool t = check(x+1);
            use[i] = 0;
            if (!t) return 0;
        }
    }
    if (!found) return 0; else return 1;
}

int ans;

void f(int x,int y,int cnt){
    if (x==N && y==N){

        FOR(i,0,N) order[i]=i;
        bool all = 1;
        do{
            CLR(use);
            if (!check(0)) all = 0;
        }while(next_permutation(order,order+N));
        if (all){
            /*
            puts("!!!");
            FOR(i,0,N){
                FOR(j,0,N) printf("%d",a[i][j]);puts("");
            }
            puts("!!");
            */
            ans = min(ans,cnt);
        }
        return;
    }
    if (y==N){
        f(x+1,0,cnt);
        return;
    }

    if (init[x][y]){
        a[x][y] = 1;
        f(x,y+1,cnt);
        return;
    }

    a[x][y] = 1;
    f(x,y+1,cnt+1);
    a[x][y] = 0;
    f(x,y+1,cnt);
}

int main(){
    scanf("%d", &T);
    FOE(t,1,T){
        scanf("%d",&N); gets(s);
        FOR(i,0,N){
            gets(s);
            FOR(j,0,N) init[i][j] = (s[j]=='1');
        }
        ans = INF;
        f(0,0,0);
        printf("Case #%d: %d\n",t,ans);
    }
    return 0;
}
