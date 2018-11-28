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
char a[NSIZ], b[NSIZ], f[NSIZ], g[NSIZ];
bool chk[NSIZ];
pip mn, p;
void check(){
    p.S.F=0;p.S.S=0;
    for(int i=0; i<n; i++){
        p.S.F*=10;p.S.F+=a[i]-'0';
        p.S.S*=10;p.S.S+=b[i]-'0';
    }
    p.F=ab(p.S.F-p.S.S);
//    printf("%d %d\n", p.S.F, p.S.S);
    mn=min(mn,p);
}
void func(int d, int e){
    if(e==n){
        check();return ;
    }
    if(d==n){
        if(g[e]!='?'){func(d,e+1);return ;}
        for(int i=0; i<=9; i++){
            b[e]=i+'0';
            func(d,e+1);
        }
    }
    else{
        if(f[d]!='?'){func(d+1,e);return ;}
        for(int i=0; i<=9; i++){
            a[d]=i+'0';
            func(d+1,e);
        }
    }
}
int main(){
    int i, j, k, l;
    long long ll=0, rr=mxll, mid;
    int test;
    scanf("%d", &test);
    for(int zz=1; zz<=test; zz++){
        scanf("%s %s", a, b);
        n=strlen(a);
        for(i=0; i<n; i++){
            f[i]=a[i];g[i]=b[i];
        }
        mn=pip(mxint,pii(mxint,mxint));
        func(0,0);
        for(i=n-1; i>=0; i--){
            a[i]=mn.S.F%10+'0';mn.S.F/=10;
            b[i]=mn.S.S%10+'0';mn.S.S/=10;
        }
        printf("Case #%d: %s %s\n", zz, a, b);
    }
    return 0;
}

