#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<vector>
#include<list>
#define NSIZ 100100
#define MSIZ 100100
#define inf 1010540580
#define mxint 2147483647
#define mxll 9223372036854775807LL
#define primell 10000000000000061LL
#define mod 1000000007
#define pii pair<int,int>
#define pli pair<long long,int>
#define F first
#define S second
#define viit vector<int>::iterator
#define vpiiit vector<pii>::iterator
#define liit list<int>::iterator
#define lpiiit list<pii>::iterator
#define ab(x) ((x)<0?-(x):(x))
using namespace std;
int n, m, o, a[NSIZ];
bool chk[NSIZ];
int main(){
    int test;
    scanf("%d", &test);
    for(int tt=1; tt<=test; tt++){
        int i, j ,k=0;
        scanf("%d", &n);
        for(i=0; i<n; i++){
            scanf("%d", &a[i]);
            if(i>0)k=max(k,a[i-1]-a[i]);
        }
        int re1=0, re2=0;
        for(i=1; i<n; i++){
            re1+=max(0,a[i-1]-a[i]);
            re2+=min(a[i-1],k);
        }
        printf("Case #%d: %d %d\n", tt,re1,re2);
    }
    return 0;
}
