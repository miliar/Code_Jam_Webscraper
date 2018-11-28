/**
submitted by: prakhar8795
Sleep. Code. Eat. Repeat.
*/

#include<bits/stdc++.h>
using namespace std;


typedef long long int ll ;

long long int getNext(long long int x)
{
    int j[20]={0} ;
    for(int i=1 ;  ; i++) {
            ll temp = i*x ;
            while(temp>0) {
                j[temp%10]=1 ;
                temp=temp/10 ;
            }
            int flag=1 ;
            for(int k=0 ; k<10 ; k++) {
                if(j[k]==0) {
                    flag=0 ;
                    break ;
                }
            }
            if(flag==1) {
                return i*x ;
            }
    }
}


void solve()
{
    int test ;
    scanf("%d",&test) ;
    int k=1 ;
    while(test--) {
        ll n ;
        scanf("%lld",&n) ;
        if(n==0) {
            printf("Case #%d: INSOMNIA\n",k) ;
        }
        else {
            ll res=getNext(n) ;
            printf("Case #%d: %lld\n",k,res) ;
        }
        k++ ;
    }
/*    for(int i=1 ; i<=1000000 ; i++) {
        ll res=getNext(i) ;
        cout << i << " " << res << " " << res/i << "\n" ;
    }
    */
}

int main()
{
    freopen("A-large.in","r",stdin) ;
    freopen("ALargeF.out","w",stdout) ;
    solve() ;
    return 0 ;
}
