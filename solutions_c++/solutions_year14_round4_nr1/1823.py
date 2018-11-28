#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <stack>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <cmath>
#define clr(A) memset(A,0,sizeof(A))
#define mm 10005
#define eps  (1e-8)
using namespace std;
typedef long long LL;
typedef pair<int,int > P;
typedef pair<P,int> pp;
typedef unsigned int ULL;
const int INF = 10000010;
vector<P> by[mm];
int l[mm],a[mm],hash[mm],r[mm];

int main()
{
     int T,c = 0;
     int n,x;

    //freopen("in.txt","r",stdin);
    //freopen("gcj.out","w",stdout);
     scanf("%d",&T);
     while(T--){
        printf("Case #%d: ",++c);
         scanf("%d%d",&n,&x);
         for(int i = 0;i<n;i++)
         scanf("%d",a+i);
         sort(a ,a+n);
         clr(hash);
         int ans = 0;
         for(int i  = n-1;i>=0;i--)
         if(hash[i] == 0){
             for(int p = i-1;p>=0;p--) // = x - a[i];
             if(a[p]+a[i]<=x && !hash[p]){
                hash[p] = 1;
                break;
             }
             ans++;
         }
         printf("%d\n",ans);
     }
    return 0;
}
