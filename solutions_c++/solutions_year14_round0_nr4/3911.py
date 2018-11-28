#include<cstdio>
#include<iostream>
#include<vector>
#include<map>
#include<stack>
#include<queue>
#include<bitset>
#include<list>
#include<iomanip>
#include<string>
#include<climits>
#include <sstream>
#include <fstream>
#include<cctype>
#include<time.h>
#include<assert.h>
#include<set>
#include <numeric>
#include <functional>
#include<cstring>
#include<cmath>
#include<iterator>
#include <memory.h>
#include<utility>
#include <ctime>
#include<algorithm>
#define read freopen("input.txt","r",stdin)
#define write freopen("output.txt","w",stdout)
#define all(v) v.begin(),v.end()
#define min3(a,b,c) min(a,min(b,c))
#define max3(a,b,c) max(a,max(b,c))
#define min4(a,b,c,d) min(min(a,b),min(c,d))
#define max4(a,b,c,d) max(max(a,b),max(c,d))
#define maxall(v) *max_element(all(v))
#define minall(v) *min_element(all(v))
#define pb push_back
#define mk make_pair
#define SORT(v) sort(all(v))
#define UN(v) SORT(v), (v).erase(unique(all(v)),v.end())
#define common(a,b) SORT(a), SORT(b), a.erase(set_intersection(all(a),all(b),a.begin()),a.end())
#define uncommon(a,b) SORT(a), SORT(b), a.erase(set_symmetric_difference(all(a),all(b),a.begin()),a.end())
#define FILL(a,d) memset(a,d,sizeof(a))
#define LL long long
#define ULL unsigned long long
#define PI 2*acos(0.0)
#define pi pair<int,int>
#define fr(i,n) for(LL i=0;i<n;i++)
#define DD double
#define sf(a) scanf("%d",&a)
#define pf(a) printf("%d\n",a)
#define sld(a) scanf("%lld",&a)
#define pld(a) printf("%lld\n",a)
#define eps 1e-6
using namespace std;

template<class T> T bigmod(T b,T p,T m){if(p==0) return 1%m; T x=b; T ans=1; while(p){ if(p&1) ans=(ans*x)%m; p>>=1; x=(x*x)%m; } return ans; }
template<class T> T gcd(T x, T y){if (y==0) return x; return gcd(y,x%y);}
template <typename T> T POW(T b,T p) { if (p == 1) return b; if (p%2 == 0) { T s = POW(b,p/2); return s*s; } return b*POW(b,p-1);}
template <typename T> T modinv(T num,T m) {return bigmod(num,m-2,m);}

int main()
{
    read;
    write;
    int t,k=0;
    sf(t);
    while(t--)
    {
        int n; sf(n);
        DD a[1009],b[1009];
        for(int i=0;i<n;i++) cin>>a[i];
        for(int i=0;i<n;i++) cin>>b[i];
        sort(a,a+n);
        sort(b,b+n);
//        for(int i=0;i<n;i++) cout<<a[i]<<" ";
//        cout<<endl;
//        for(int i=0;i<n;i++) cout<<b[i]<<" ";
//        cout<<endl;
        int c,d; c=d=0;
        for(int i=0;i<n;i++,d++)
        {
            while(i<n&&a[i]<b[d])
                i++;
            if(i<n)
            c++;
        }
        printf("Case #%d: %d ",++k,c);
        c=0,d=n-1;
        int an=0,bn=d,f=1;
        for(int i=n-1;i>=0;i--)
        {
            if(a[i]>b[d])
            {
                an++;
                c++;
            }
            else
                d--;
        }
        pf(c);
    }
    return 0;
}
