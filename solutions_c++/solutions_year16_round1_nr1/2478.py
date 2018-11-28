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
char a[NSIZ], b[NSIZ];
bool chk[NSIZ];
int main(){
    int i, j, k, l;
    long long ll=0, rr=mxll, mid;
    int test;
    scanf("%d", &test);
    for(int zz=1; zz<=test; zz++){
        scanf("%s", a);
        n=strlen(a);
        k=0;l=n-1;
        int cc=0, bc=n-1;
        while(k<=l){
            j=k;
            for(i=k; i<=l; i++){
//                printf("%c %c\n", a[i], a[j]);
                if(a[i]>=a[j])j=i;
            }
//            printf("%c %d\n", a[j], j);
            b[cc++]=a[j];
            for(; l>j; l--){
                b[bc--]=a[l];
            }
            l--;
        }
        printf("Case #%d: ", zz);
        for(i=0; i<n; i++){
            printf("%c", b[i]);
        }
        printf("\n");
    }
    return 0;
}

