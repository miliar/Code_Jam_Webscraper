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

int T,N,P,R,S;
char a[20][5000];
char ans[5000], tmp1[5000], tmp2[5000];
bool found;

void f(int n, int len, int st, int ed){
    if (len < 2) return;

    int mid = (st+ed)/2;
    f(n,len/2,st,mid);
    f(n,len/2,mid,ed);
    //printf("%d %d %d!\n",len,st,ed);

    for(int i=st,j=0;i<ed;++i,++j) tmp1[j] = a[n][i];
    int pos = 0;
    for(int i=mid;i<ed;++i) tmp2[pos++] = a[n][i];
    for(int i=st;i<mid;++i) tmp2[pos++] = a[n][i];
    tmp1[len] = tmp2[len] = 0;
    /*
    puts("1");
    puts(tmp1);
    puts("2");
    puts(tmp2);
    */

    if (strcmp(tmp2, tmp1) < 0) strncpy(a[n]+st, tmp2, len);
}

void gen(int n, int r, int len) {
    if (r == n){
        a[n][len] = 0;

        int cp,cr,cs;
        cp=cr=cs=0;
        FOR(i,0,len) {
            if (a[n][i] == 'P') ++cp;
            if (a[n][i] == 'R') ++cr;
            if (a[n][i] == 'S') ++cs;
        }
        if (cp != P || cr != R || cs != S) return;
        //puts(a[n]);
        f(n,len,0,len);

        if (!found || (strcmp(a[n], ans) < 0)){
            strcpy(ans, a[n]);
            found = 1;
        }
        ans[len] = 0;

        return;
    }
    FOR(i,0,len){
        if (a[r][i] == 'P'){
            a[r+1][i*2] = 'P';
            a[r+1][i*2+1] = 'R';
        }
        if (a[r][i] == 'R'){
            if (r+1 == n) {
                a[r+1][i*2] = 'R';
                a[r+1][i*2+1] = 'S';
            }
            else{
                a[r+1][i*2] = 'S';
                a[r+1][i*2+1] = 'R';
            }
        }
        if (a[r][i] == 'S'){
            a[r+1][i*2] = 'P';
            a[r+1][i*2+1] = 'S';
        }
    }
    gen(n,r+1,len*2);
}

int main(){
    scanf("%d", &T);
    FOE(t,1,T) {
        scanf("%d%d%d%d",&N,&R,&P,&S);

        found = 0;
        a[0][0] = 'P'; gen(N,0,1);
        a[0][0] = 'R'; gen(N,0,1);
        a[0][0] = 'S'; gen(N,0,1);
        if (found){
            printf("Case #%d: %s\n",t,ans);
        }
        else printf("Case #%d: IMPOSSIBLE\n",t);
    }
    return 0;
}
