/**
submitted by: prakhar8795
Sleep. Code. Eat. Repeat.
*/

#include<bits/stdc++.h>
using namespace std;


typedef long long int ll ;
typedef unsigned long long int ull ;

void solve()
{
    int test ;
    scanf("%d",&test) ;
    int z=1 ;
    while(test--) {
        int k,c,s ;
        scanf("%d %d %d",&k,&c,&s) ;
        if(k==s) {
            printf("Case #%d:",z) ;
            ull start=1 ;
            ull value = pow(k,c-1) ;
            for(int i=0 ; i<k ; i++) {
                printf(" %llu",start) ;
                start += value ;
            }
            printf("\n") ;
        }
        z++ ;
    }
}

int main()
{
    freopen("D-small-attempt0.in","r",stdin) ;
    freopen("Dout.txt","w",stdout) ;
    solve() ;
    return 0 ;
}


