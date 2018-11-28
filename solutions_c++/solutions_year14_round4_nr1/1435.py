#include<math.h>
#include<algorithm>
#include<cstdlib>
#include<iostream>
#include<stdio.h>
#include<map>
#include<ext/hash_map>
#include<ext/hash_set>
#include<set>
#include<string>
#include<assert.h>
#include<vector>
#include<time.h>
#include<queue>
#include<deque>
#include<sstream>
#include<stack>
#include<sstream>
#define MA(a,b) ((a)>(b)?(a):(b))
#define MI(a,b) ((a)<(b)?(a):(b))
#define AB(a) (-(a)<(a)?(a):-(a))
#define X first
#define Y second
#define mp make_pair
#define pb push_back
#define pob pop_back
#define ep 0.0000000001
#define pi 3.1415926535897932384626433832795

using namespace std;
using namespace __gnu_cxx;
const int N=1000111;
int n,m,i,j,k,l,r;
int a[N];
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("text.txt","w",stdout);
   int t;
   cin>>t;
   for (int test=1;test<=t;test++)
   {
       cin>>n>>m;
       for (i=1;i<=n;i++) scanf("%d",&a[i]);
       sort(a+1,a+n+1);
       k=1;
       i=n;
       l=0;
       while (i>=k)
       {
           if (i>k) {
            if (a[i]+a[k]<=m)
            {
                l++;
                i--;
                k++;
            } else {
            l++;
            i--;}
           } else
           {
               i--;
               l++;
           }
       }
       cout<<"Case #"<<test<<": "<<l<<endl;
    }
    return 0;
}
