# include <iostream>
# include <cmath>
# include <cstring>
using namespace std ;
int main()
{
    int t , i ;
    cin>>t ;
    for(i=0;i<t;i++)
    {
        char str[105] , temp  ;
        cin>>str ;
        int len , j ;
        len=strlen(str) ;
        long long int ans = 1 , k=0  ;
        temp=str[0];
        for(j=1 ; j< len ;j++)
        {
            if( str[j]!=temp)
                ans++ ;
            temp=str[j] ;
            
        }
        if(str[0]=='-')
        {
            ans--;
            k = 1 ;
        }
        if(ans%2==1)
            ans--;
        k+=ans ;
        printf("Case #%d: %lld\n",i+1,k ) ;
        
        
    }
    return 0 ;
}