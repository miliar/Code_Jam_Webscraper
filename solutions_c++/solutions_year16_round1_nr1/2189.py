#include <bits/stdc++.h>
#define pf printf
#define sf scanf
#define INF 2000000000
#define PI (acos(-1.0))
#define i64 long long int
#define DBG printf("Hi\n")
#define loop(i,n) for(i =1 ; i<=n; i++)
#define mp make_pair
#define pb push_back
#define mod 1000000007
#define maxn 200005
#define ff first
#define sc second

using namespace std ;

char s[2010] , str[1005] ;

int main()
{
    int i , j  , k , l=1001 , n , m , r=1001 , t=1, tc , mx ;

    freopen("Al.in","r",stdin) ;
    freopen("out.txt","w",stdout) ;

    sf("%d",&tc) ;

    while(t<=tc)
    {
        sf("%s",str) ; ;
        l = 1001 ; r = 1001 ;
        s[l] = str[0] ;
        mx =  str[0] ;

        for(i=1 ; str[i]!='\0' ; i++)
        {
            if(str[i]<mx){
                s[++r] = str[i] ;
            }
            else{
                mx = str[i] ;
                s[--l] = str[i] ;
            }
        }
        for(i=l,j=0; i<=r ; j++,i++) str[j] = s[i] ;
        pf("Case #%d: %s\n",t++,str) ;
    }
    return  0 ;
}
