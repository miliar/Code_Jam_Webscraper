

#include<bits/stdc++.h>
using namespace std;
#define pb push_back
#define vec vector
#define maxn  100004
#define FOR(i,n) for(i=0;i<n;i++)
#define plld(x) printf("%lld",x)
#define pd(x) printf("%d",x)
#define pld(x) printf("%ld",x)
#define ps(x)  printf("%s",x)
#define plldn(x) printf("%lld\n",x)
#define pdn(x) printf("%d\n",x)
#define pldn(x) printf("%ld\n",x)
#define psn(x)  printf("%s\n",x)
#define slld(x) scanf("%lld",&x)
#define sd(x) scanf("%d",&x)
#define sld(x) scanf("%ld",&x)
#define ss(x)  scanf("%s",x)
#define bitcount __builtin_popcountll
#define ll long long
#define mod 1000000007

//std::priority_queue<int, std::vector<int>, std::greater<int> > my_min_heap;
//getline(cin,s) ;
int main(){
std::ios_base::sync_with_stdio (false);
long long t ,n,x,y,z,i,j,k ,l,m,p ;
char a[128],f ;
freopen("input2.in","r",stdin) ;
freopen("output.txt","w",stdout) ;

slld(t) ;
m=1 ;
while(t--){
    ss(a) ;
    k=0 ;
    l = strlen(a) ;
    f='+' ;
    for(i=l-1;i>=0;i--){
        if(a[i]!=f) {
            k++ ;
            if(f=='+')
                f='-' ;
            else
                f='+' ;

        }

    }
    ps("Case #");
    plld(m) ;
    ps(": ") ;
    plldn(k) ;
    m++ ;
}

return 0 ;
}
