#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<utility>
#include<vector>
#include<list>
#include<queue>
#include<set>
#include<map>
using namespace std;
#define NSIZ 110
#define MSIZ 100010
#define inf 1010540580
#define mxint 2147483647
#define mxll 9223372036854775807LL
#define prime15 1000000000000037LL
#define prime16 10000000000000061LL
#define mod 1000000007
#define F first
#define S second
#define vit(T) vector<T>::iterator
#define lit(T) list<T>::iterator
#define lrit(T) list<T>::reverse_iterator
#define sit(T) set<T>::iterator
#define mit(T1,T2) map<T1,T2>::iterator
#define MAXPQ(T) priority_queue<T>
#define MINPQ(T) priority_queue<T,vector<T>,greater<T> >
#define ab(x) ((x)<0?-(x):(x))
typedef pair<int,int> pii;
typedef pair<long long,int> pli;
typedef pair<long long,long long> pll;
typedef pair<int,pair<int,int> > pip;

int n, m, o, re=0;
long long res=0;
char a[NSIZ][NSIZ];
bool chk[NSIZ][NSIZ];
char tt[4]={'^','>','v','<'};
pii dir[200];
bool check(int i, int j){
    int ii=i+dir[a[i][j]].F, jj=j+dir[a[i][j]].S;
    while(a[ii][jj]=='.'){
        ii+=dir[a[i][j]].F;jj+=dir[a[i][j]].S;
    }
    if(a[ii][jj]=='#')return false;
    else return true;
}
void run(int i, int j, char d){
    while(1){
        if(chk[i][j]==1)return ;
        chk[i][j]=1;d=a[i][j];
        int ii=i+dir[d].F, jj=j+dir[d].S;
        while(a[ii][jj]=='.'){
            ii+=dir[d].F;jj+=dir[d].S;
        }
        if(a[ii][jj]=='#'){re++;return;}
        else i=ii;j=jj;
    }
}
int main(){
    int i, j, k, l;
    long long ll, rr, mid;
    int test;
    dir['^']=pii(-1,0);
    dir['>']=pii(0,1);
    dir['v']=pii(1,0);
    dir['<']=pii(0,-1);
    scanf("%d", &test);
    for(int zz=1; zz<=test; zz++){
        memset(a,'#',sizeof(a));
        memset(chk,0,sizeof(chk));
        scanf("%d %d", &n, &m);
        for(i=1; i<=n; i++){
            scanf("%s", a[i]);
            for(j=m; j>=1; j--){
                a[i][j]=a[i][j-1];
            }
            a[i][0]='#';
        }
        re=0;
        for(i=1; i<=n; i++){
            for(j=1; j<=m; j++){
                if(a[i][j]=='.')continue;
                if(chk[i][j]==1)continue;
                if(check(i,j)==false){
                    for(k=0; k<4; k++){
                        a[i][j]=tt[k];
                        if(check(i,j))break;
                    }
                    if(k==4)goto imp;
                    re++;
                }
                run(i,j,a[i][j]);
            }
        }
        printf("Case #%d: %d\n", zz, re);continue;
        imp:;
        printf("Case #%d: IMPOSSIBLE\n", zz);
    }
    return 0;
}
