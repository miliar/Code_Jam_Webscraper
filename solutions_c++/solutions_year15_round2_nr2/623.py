#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<vector>
#include<list>
#include<queue>
#include<stack>
#include<set>
#define NSIZ 10010
#define MSIZ 100010
#define inf 1010540580
#define mxint 2147483647
#define mxll 9223372036854775807LL
#define primell 10000000000000061LL
#define mod 1000000007
#define pii pair<int,int>
#define pli pair<long long,int>
#define pll pair<long long,long long>
#define F first
#define S second
#define viit vector<int>::iterator
#define vpiiit vector<pii>::iterator
#define liit list<int>::iterator
#define lirit list<int>::reverse_iterator
#define lpiiit list<pii>::iterator
#define ab(x) ((x)<0?-(x):(x))
using namespace std;
int n, m, o;
int a[NSIZ];
bool chk[NSIZ][NSIZ];
int main(){
//    freopen("B-small-attempt1.in","r",stdin);
//    freopen("B_small1.txt","w",stdout);
    int i, j, k, l, test;
    scanf("%d", &test);
    for(int tt=1; tt<=test; tt++){
        memset(chk,0,sizeof(chk));
        scanf("%d %d %d", &n, &m, &o);
        printf("Case #%d: ", tt);
        k=n*m;
        int re=n*m*2-n-m;
        if(o<=k/2+k%2){printf("0\n");continue;}
        if(n>m)swap(n,m);
        if(n==1){
            printf("%d\n", re-(m-o)*2);
            continue;
        }
        if((n*m)%2==0){
            j=(n-2)*(m-2)/2;
            if(k-j<=o){re-=(k-o)*4;goto print;}
            k-=j;
            re-=j*4;
            j=((n-2)/2+n%2+(m-2)/2+m%2)*2;
            if(k-j<=o){re-=(k-o)*3;goto print;}
            k-=j;
            re-=j*3;
            re-=(k-o)*2;
        }
        else{
            j=((n-2)*(m-2))/2+1;
            if(k-j<=o){re-=(k-o)*4;goto print;}
            k-=j;
            re-=j*4;
            j=((n-2)/2+(m-2)/2)*2;
            if(k-j<=o){re-=(k-o)*3;goto print;}
            k-=j;
            re-=j*3;
            re-=(k-o)*2;
            l=re;

            re=n*m*2-n-m;k=n*m;
            j=(((n-2)*(m-2))/2);re-=j*4;k-=j;
            re-=(k-o)*3;
            re=min(re,l);
        }
        print:;
        printf("%d\n", re);
    }
    return 0;
}
