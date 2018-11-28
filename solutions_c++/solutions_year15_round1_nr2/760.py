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
int n, o, a[NSIZ];
long long m;
bool chk[NSIZ];
int main(){
    int test;
    scanf("%d", &test);
    for(int tt=1; tt<=test; tt++){
        int i, j, k;
        scanf("%d %lld", &n, &m);
        for(i=0; i<n; i++){
            scanf("%d", &a[i]);
        }
        long long l=0, r=100000000000000LL, mid;
        while(l<r){
            mid=(l+r)/2;
            long long ss=n;
            for(i=0; i<n; i++){
                ss+=mid/a[i];
            }
//            printf("%lld = %lld\n", mid, ss);
            if(ss>=m)r=mid;
            else l=mid+1;
        }
        r=-1;
//        printf("=%lld\n", l);
        for(i=0; i<n; i++){
            mid=a[i]*(l/a[i]);
            r=max(r,mid);
            m-=l/a[i];
        }
        for(i=0; i<n; i++){
            if(a[i]*(l/a[i])<r)m--;
        }
        for(i=0; i<n; i++){
            if(a[i]*(l/a[i])==r)m--;
            if(m==0)break;
        }
        printf("Case #%d: %d\n", tt, i+1);
    }
    return 0;
}
