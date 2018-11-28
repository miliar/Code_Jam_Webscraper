#pragma comment(linker, "/STACK:1024000000,1024000000")
#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <vector>
#include <set>
#include <map>
#include <string>
using namespace std;
#define LL long long
#define mp make_pair
#define fr first
#define sc second
#define pb push_back
#define lc (x<<1)
#define rc ((x<<1)|1)
const int N=1005;
char s[N];
int a[N];
int main(){
   // freopen("in.txt","r",stdin);freopen("out.txt","w",stdout);
    int T,T0=0;cin>>T;
    while (T--){
        int i,j,n,k,sum=0;
        scanf("%s",s+1);n=strlen(s+1);cin>>k;
        for (i=1;i<=n;i++) if (s[i]=='+') a[i]=1; else a[i]=0;
        for (i=1;i<=n;i++)
         if (!a[i]){
            if (i+k-1>n) break;sum++;
            for (j=0;j<k;j++) a[i+j]^=1;
         }
        cout<<"Case #"<<++T0<<": ";
        if (i>n) printf("%d\n",sum); else puts("IMPOSSIBLE");
    }
    
  //  system("pause");
    return 0;
}
