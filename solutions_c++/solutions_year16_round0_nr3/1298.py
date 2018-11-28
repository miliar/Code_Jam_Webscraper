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
int a[NSIZ], b[NSIZ], p[NSIZ], pl=0;
bool chk[NSIZ];
bool divisor(int k, int bs){
    int remind=0;
    for(int i=n-1, j=1; i>=0; i--, j=(j*bs)%k){
        remind+=a[i]*j;
        remind%=k;
    }
    if(remind==0)return true;
    else return false;
}
void check(){
    int i;
    for(i=2; i<=10; i++){
        int j=0;int co=0;
        for(j=0; j<pl; j++){
            if(divisor(p[j],i)){
                co++;
                if(co>=2)break;
                b[i]=p[j];
            }
        }
        if(co<2)return ;
    }
    for(i=0; i<n; i++){
        printf("%d", a[i]);
    }
    for(i=2; i<=10; i++){
        printf(" %d", b[i]);
    }
    printf("\n");
    re++;
}
void solve(int d){
    if(d==n){
        check();
        return ;
    }
    a[d]=1;
    solve(d+1);
    if(re==m)return ;
    if(d>0 && d<n-1){
        a[d]=0;
        solve(d+1);
    }
}
void findprime(){
    p[pl++]=2;
    for(int i=3; i<=100000; i+=2){
        if(chk[i])continue;
        p[pl++]=i;
        for(int j=i; j<=100000; j+=i){
            chk[j]=1;
        }

    }
}
int main(){
    int i, j, k, l;
    long long ll=0, rr=mxll, mid;
    findprime();
    n=32;m=500;
    printf("Case #1:\n");
    solve(0);
    return 0;
}

