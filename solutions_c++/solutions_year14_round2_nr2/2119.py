#include <bits/stdc++.h>
using namespace std;

#define sc(a) scanf("%d",&a)
#define scm(a,b,c) scanf("%d%d%d",&a,&b,&c)
#define fl(c,i,n) for(i=c;i<n;i++)
#define f(i,n) for(i=0;i<n;i++)
#define mem(a,val) memset(a,val,sizeof(a))
#define ll long long int
#define ull unsigned long long int
#define inf INT_MAX
#define linf LONG_LONG_MAX
#define pb push_back
#define pp pop_back()
#define aov(a) a.begin(),a.end()
#define mp make_pair
#define nl printf("\n")
#define PI 2.0*acos(0.0) //#define PI acos(-1.0)
#define xx first
#define yy second

#define mxv(a) *max_element(aov(a))
#define mnv(a) *min_element(aov(a))

#define LB(a,x) (lower_bound(aov(a),x)-a.begin())
#define UB(a,x) (upper_bound(aov(a),x)-a.begin())

#define to_c_string(a) a.c_str()
#define strtoint(c) atoi(&c[0])

#define M 10000

#define COUT(x) #x

int main ()
{
    FILE  *fo;
    fo=fopen("out.txt","w");

    int t,a,b,k,i,j,q=1;
    ll s;
    sc(t);
    while(t--){
        scm(a,b,k);
        s=0;
        f(i,a){
            f(j,b){
                if((i&j)<k)
                    s++;
            }
        }
        fprintf(fo,"Case #%d: %lld\n",q++,s);
    }

    return 0;
}


