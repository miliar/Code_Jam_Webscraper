#include<stdio.h>
#include<cstring>
#include<algorithm>
#include<utility>
#include<vector>
#include<list>
#include<queue>
#include<set>
#include<map>
using namespace std;
#define NSIZ 1000010
#define MSIZ 1000010
#define inf 1010580540
#define mxint 2147483647
#define mxll 9223372036854775807LL
#define prime15 1000000000000037LL
#define prime16 10000000000000061LL
#define mod 1000000007LL
#define F first
#define S second
#define vit(T) vector<T>::iterator
#define lit(T) list<T>::iterator
#define sit(T) set<T>::iterator
#define mit(T1,T2) map<T1,T2>::iterator
#define MAXPQ(T) priority_queue<T>
#define MINPQ(T) priority_queue<T,vector<T>,greater<T> >
#define ab(x) ((x)<0?-(x):(x))
typedef pair<int,int> pii;
typedef pair<long long,int> pli;
typedef pair<long long,long long> pll;
typedef pair<double,double> pdd;
typedef pair<int,pair<int,int> > pip;
typedef pair<pair<int,int>,pair<int,int> > ppp;

int n, m, o, re=0;
long long res=0;
int a[NSIZ], b[NSIZ];
bool chk[NSIZ];
int main(){
    int i, j, k, l;
    long long ll=0, rr=mxll, mid;
    int test;
    scanf("%d", &test);
    for(int zz=1; zz<=test; zz++){
        scanf("%d %d %d", &n, &m, &o);
        printf("Case #%d: ", zz);
        if(m==1){
            if(o<n){printf("IMPOSSIBLE\n");continue;}
            for(i=1; i<=n; i++){
                printf("%d ", i);
            }
            printf("\n");
            continue;
        }
        if(o<(n+1)/2){printf("IMPOSSIBLE\n");continue;}
        for(ll=1, i=1; i<m; i++, ll*=n);
        for(i=0, rr=ll; i<(n+1)/2; i++,rr+=ll){
            printf("%lld ", rr-i);
        }
        printf("\n");
    }
    return 0;
}

