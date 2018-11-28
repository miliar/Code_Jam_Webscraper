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
#define NSIZ 3010
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
int a[NSIZ], b[NSIZ], co[NSIZ];
bool chk[NSIZ];
int t[NSIZ][2][NSIZ], tab[NSIZ][NSIZ], t2[NSIZ][2][NSIZ];
void print(){
    printf("-----\n");
    for(int i=0; i<n; i++){
        for(int j=0; j<n; j++){
            printf("%2d ", tab[i][j]);
        }printf("\n");
    }printf("\n");
}
bool putcol(int d);
bool putrow2(int d, int cc){
    for(int i=0; i<n; i++){
        if(tab[d][i]!=-1){
            if(t[tab[d][0]][cc][i]!=tab[d][i])return false;
        }
        else{
            tab[d][i]=t[tab[d][0]][cc][i];
        }
    }
    return true;
}
bool putrow(int d){
//    print();
    if(d==n)return true;
    int tmp[NSIZ];
    for(int i=0; i<n; i++){
        tmp[i]=tab[d][i];
    }
    if(t[tab[d][0]][0][n]==-1 && t[tab[d][0]][0][0]!=-1){
        bool check=putrow2(d,0);
        t[tab[d][0]][0][n]=1;
        if(check && putcol(d))return true;
        t[tab[d][0]][0][n]=-1;
        for(int j=0; j<n; j++)tab[d][j]=tmp[j];
    }
    if(t[tab[d][0]][1][n]==-1 && t[tab[d][0]][1][0]!=-1){
        bool check=putrow2(d,1);
        t[tab[d][0]][1][n]=1;
        if(check && putcol(d))return true;
        t[tab[d][0]][1][n]=-1;
        for(int j=0; j<n; j++)tab[d][j]=tmp[j];
    }
//    printf("%d %d\n", co[tab[d][0]], (t[tab[d][0]][0][0]!=-1)+(t[tab[d][0]][1][0]!=-1));
    if(o==-1 && co[tab[d][0]]>(t[tab[d][0]][0][0]!=-1)+(t[tab[d][0]][1][0]!=-1)){
        o=d;
        if(putcol(d))return true;
        o=-1;
    }
    return false;
}
bool putcol2(int d, int cc){
    for(int i=0; i<n; i++){
        if(tab[i][d]!=-1){
//            if(tab[0][d]==7)printf("%d,%d ", t[tab[0][d]][cc][i],tab[i][d]);
            if(t[tab[0][d]][cc][i]!=tab[i][d])return false;
        }
        else{
            tab[i][d]=t[tab[0][d]][cc][i];
        }
    }
//    printf(".");
    return true;
}
bool putcol(int d){
//    printf("+%d+", d); print();
    int tmp[NSIZ];
    for(int i=0; i<n; i++){
        tmp[i]=tab[i][d];
    }
    if(t[tab[0][d]][0][n]==-1 && t[tab[0][d]][0][0]!=-1){
        bool check=putcol2(d,0);
//        printf("++%d\n", check);
        t[tab[0][d]][0][n]=1;
        if(check && putrow(d+1))return true;
        t[tab[0][d]][0][n]=-1;
        for(int j=0; j<n; j++)tab[j][d]=tmp[j];
    }
    if(t[tab[0][d]][1][n]==-1 && t[tab[0][d]][1][0]!=-1){
        bool check=putcol2(d,1);
        t[tab[0][d]][1][n]=1;
        if(check && putrow(d+1))return true;
        t[tab[0][d]][1][n]=-1;
        for(int j=0; j<n; j++)tab[j][d]=tmp[j];
    }
//    printf(".");
//    printf("%d %d\n", co[tab[d][0]], (t[tab[d][0]][0][0]!=-1)+(t[tab[d][0]][1][0]!=-1));
    if(o==-1 && co[tab[0][d]]>(t[tab[0][d]][0][0]!=-1)+(t[tab[0][d]][1][0]!=-1)){
        o=n+d;
        if(putrow(d+1))return true;
        o=-1;
    }
    return false;
}
int main(){
    int i, j, k, l;
    long long ll=0, rr=mxll, mid;
    int test;
    scanf("%d", &test);
    for(int zz=1; zz<=test; zz++){
        memset(t,-1,sizeof(t));
        memset(tab,-1,sizeof(tab));
        memset(chk,0,sizeof(chk));
        memset(co,0,sizeof(co));
        scanf("%d", &n);
        re=mxint;
        o=-1;m=0;
        for(i=0; i<2*n-1; i++){
            scanf("%d", &k);
            re=min(re,k);
            for(j=0; j<2; j++){
                if(t[k][j][0]!=-1)continue;
                t[k][j][0]=k;
                for(l=1; l<n; l++){
                    scanf("%d", &t[k][j][l]);
                }
                break;
            }
        }
        if(t[re][1][0]==-1){
            re=-1;m=1;
            memset(t2,-1,sizeof(t2));
            for(i=0; i<NSIZ; i++){
                for(j=0; j<2; j++){
                    if(t[i][j][0]==-1)continue;
                    re=max(re,t[i][j][n-1]);
                    int cc=0;
                    if(t2[t[i][j][n-1]][cc][0]!=-1)cc++;
                    for(k=0; k<n; k++){
                        t2[t[i][j][n-1]][cc][k]=t[i][j][n-1-k];
                    }
                }
            }
            memset(t,-1,sizeof(t));
            for(i=0; i<NSIZ; i++){
                for(j=0; j<2; j++){
                    for(k=0; k<n; k++){
                        t[i][j][k]=t2[i][j][k];
                    }
                }
            }
        }
        tab[0][0]=re;
//        printf("=%d\n", re);
        for(i=1; i<n; i++){
            co[t[re][0][i]]++;
            co[t[re][1][i]]++;
        }
        putrow(0);
        printf("Case #%d: ", zz);
        if(o>=n){
            o-=n;
            if(m){
                for(i=n-1; i>=0; i--){
                    printf("%d ", tab[i][o]);
                }
            }
            else for(i=0; i<n; i++){
                printf("%d ", tab[i][o]);
            }
        }
        else{
            if(m){
                for(i=n-1; i>=0; i--){
                    printf("%d ", tab[o][i]);
                }
            }
            else for(i=0; i<n; i++){
                printf("%d ", tab[o][i]);
            }
        }
        printf("\n");
    }
    return 0;
}

