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
char a[NSIZ], b[200];
int co[10];
bool chk[NSIZ];
int main(){
    int i, j, k, l;
    long long ll=0, rr=mxll, mid;
    int test;
    scanf("%d", &test);
    for(int zz=1; zz<=test; zz++){
        scanf("%s", a);
        n=strlen(a);
        memset(b,0,sizeof(b));
        memset(co,0,sizeof(co));
        for(i=0; i<n; i++){
            b[a[i]]++;
        }
        //0=Z
        k=b['Z'];co[0]+=k;
        b['Z']=0;b['E']-=k;b['R']-=k;b['O']-=k;
        //4=U
        k=b['U'];co[4]+=k;
        b['F']-=k;b['O']-=k;b['U']-=k;b['R']-=k;
        //2=W
        k=b['W'];co[2]+=k;
        b['T']-=k;b['W']-=k;b['O']-=k;
        //3=R
        k=b['R'];co[3]+=k;
        b['T']-=k;b['H']-=k;b['R']-=k;b['E']-=k;b['E']-=k;
        //1=O
        k=b['O'];co[1]+=k;
        b['O']-=k;b['N']-=k;b['E']-=k;
        //6=X
        k=b['X'];co[6]+=k;
        b['S']-=k;b['I']-=k;b['X']-=k;
        //7=S
        k=b['S'];co[7]+=k;
        b['S']-=k;b['E']-=k;b['V']-=k;b['E']-=k;b['N']-=k;
        //5=V
        k=b['V'];co[5]+=k;
        b['F']-=k;b['I']-=k;b['V']-=k;b['E']-=k;
        //8=H
        k=b['H'];co[8]+=k;
        b['E']-=k;b['I']-=k;b['G']-=k;b['H']-=k;b['T']-=k;
        //9=I
        k=b['I'];co[9]+=k;
        b['N']-=k;b['I']-=k;b['N']-=k;b['E']-=k;

        printf("Case #%d: ", zz);
        for(i=0; i<=9; i++){
            for(j=0; j<co[i]; j++){
                printf("%d", i);
            }
        }
        printf("\n");


    }
    return 0;
}

