#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <string.h>
#include <stack>
#include <queue>
#include <vector>
#include <utility>
#include <string>
#include <sstream>
#include <iostream>
#include <set>
#include <map>
#include <algorithm>
#include <memory.h>
#include <functional>
#include <numeric>
#include<time.h>
using namespace std;


//For Define
#define forstl(i,s) for(__typeof((s).end()) i=(s).begin(); i != (s).end(); i++)

#define ff first
#define se second
#define mkp make_pair
#define pb push_back
#define sz(a) ((int)a.size())
#define ms(a,n) memset(a, n, sizeof(a))
#define ms0(a) ms(a,0)
#define all(a) a.begin(), a.end()
#define Abs(x) (((x)<0)?-(x):(x))

#define pi 2*acos(0.0)
#define gcd(a,b) __gcd(a,b)
#define lcm(a,b) (a*(b/gcd(a,b)))

#define dbg(x) cout<<#x<<'='<<x<<endl;
#define dbgarr(i,a) cout<<#a<<"["<<i<<"] = "<<a[i]<<" "<<endl;
#define IOS ios_base::sync_with_stdio(0);
//typedef
typedef long long ll;
typedef pair<int,int> pii;
typedef pair<pair<int,int>,int > piii;
// Number theory
ll big_mod(ll b,ll p,ll m) {ll res=1;while(p){if(p & 1){res=((res%m)*(b%m))%m;}b=((b%m)*(b%m))%m;p>>=1;}return res;}
ll Pow(ll b,ll p) {ll res=1;while(p){if(p & 1){res=res*b;}b=b*b;p>>=1;}return res;}
ll modinv(ll n,ll m){return big_mod(n,m-2,m);}

////MAIN CODE HERE


int main(){
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);

    int t,cno=0;
    scanf("%d",&t);

    while(t--){
        int n;
        double a[10009],c[10009],d[10009],b[10009];
        scanf("%d",&n);

        for(int i=0;i<n;i++){
            scanf("%lf",&a[i]);
            c[i]=a[i];
        }
        for(int i=0;i<n;i++){
            scanf("%lf",&b[i]);
            d[i]=b[i];
        }

        sort(a,a+n);
        sort(b,b+n);
        sort(c,c+n);
        sort(d,d+n);

        int cnt1=0,cnt2=0;

        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                if(a[i]>b[j]){
                    cnt1++;
                    b[j]=11.0;
                    break;
                }
            }
        }
        bool flag=0;
        for(int i=n-1;i>=0;i--){
            flag=1;
            for(int j=0;j<n;j++){
                if(c[i]<d[j]){
                    flag =0;
                    d[j]=0.0;
                    break;
                }
            }
            if(flag)  cnt2++;
        }

        printf("Case #%d: %d %d\n",++cno,cnt1,cnt2);
    }
    return 0;
}



















