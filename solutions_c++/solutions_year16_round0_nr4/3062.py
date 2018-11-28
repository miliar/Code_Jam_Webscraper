#include <bits/stdc++.h>

using namespace std;

int t ;
int n , k , C , s;
int main()
{
    freopen("D-small-attempt0.in","r",stdin) ;
    freopen("out.txt","w",stdout) ;
    scanf("%d",&t) ;
    for ( int c = 1 ; c <= t ; c++ )
    {
        scanf("%d%d%d",&k,&C,&s) ;
        printf("Case #%d: ",c) ;
        for ( int i = 1 ; i <= k ; i++ )
            printf("%d ",i) ;
        puts("") ;
    }
    return 0;
}
