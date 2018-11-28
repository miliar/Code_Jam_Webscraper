

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
freopen("input4.in","r",stdin) ;
freopen("output.txt","w",stdout) ;
int loc[10] ;
slld(t) ;
m=1 ;
while(t--){
    slld(n) ;
    p=0 ;
    FOR(i,10){
        loc[i]=0 ;
    }
    y=n ;
    if(n!=0){
            while(1){
            l=y ;
            while(l>0){
                if(loc[l%10]==0){
                    loc[l%10]=1;
                    p=p+1 ;
                    if(p==10){
                        break ;
                    }
                }
                l=l/10 ;
            }
            if(p==10)
                break ;
            y=y+n ;
        }
        ps("Case #");
        plld(m) ;
        ps(": ") ;
        plldn(y) ;

    }
    else{
                ps("Case #");
        plld(m) ;
        ps(": ") ;
        psn("INSOMNIA") ;

    }




    m++ ;
}

return 0 ;
}
