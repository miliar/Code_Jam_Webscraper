#include <bits/stdc++.h>

#define sf scanf
#define pf printf
#define INF 2000000000
#define PI (acos(-1.0))
#define mp make_pair
#define pb push_back
#define i64 long long int
#define DBG printf("Hi\n")

using namespace std ;

int n , j ,cnt= 0 , k = 11 ;
char s[105][105] , str[105] ;
char ans[505][35] ;

void recur(int pos , int ones )
{
    if(cnt*cnt>=j) return ;
    if(  ((n/2)-1)-(pos-1) + ones<k ) return ;
    if( ones > k ) return ;
    if( pos==(n/2) )
    {
        ++cnt ;
        int i ;
        for(i =1 ; i<pos ; i++)  s[cnt][i] = str[i] ;
        s[cnt][i] = '\0' ;
        s[cnt][0] = '#' ;
        return ;
    }
    str[pos] = '0' ;
    recur( pos+1 , ones ) ;
    if(cnt*cnt>=j) return ;
    str[pos] = '1' ;
    recur(pos+1,ones+1) ;

    return ;
}

int main()
{
    int i , m , c1 , c2 , x , y , l=0 , tc  ;

    freopen( "C-large.in" , "r" , stdin ) ;
    freopen( "out.txt" , "w" , stdout ) ;

    sf("%d %d %d",&tc,&n,&j) ;
    recur(1, 0) ;
  //  for(i=1 ; i<=cnt ; i++) pf("%s\n",s[i]) ;

    for( c1=1 ; c1<=cnt ; c1++ )
    {
        for( c2=1 ; c2<=cnt ; c2++ )
        {
            for(i=1,l++ ; i<(n/2) ; i++ )
            {
                ans[l][ 2*i-1] = s[c1][i] ;
            }
            for(i=1 ; i<(n/2) ; i++ )
            {
                ans[l][ 2*i] = s[c2][i] ;
            }
            ans[l][0] = ans[l][n-1] = '1' ;
            ans[l][n] = '\0' ;
         //   pf("%s\n",ans[l]) ;
            if(l>=j) break ;
        }
        if(l>=j) break ;
    }
    pf("Case #1:\n") ;
    for(i=1 ; i<=j ; i++){
        pf("%s",ans[i]) ; ;
        for(c1=2 ; c1<=10 ; c1++)
        {
            if(c1%2==0){
                if(c1==6) pf(" 7");
                else pf(" 3") ;
            }
            else pf(" 2") ;
        }
        pf("\n") ;
    }

    return 0 ;
}
