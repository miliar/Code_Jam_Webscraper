#include <iostream>
#include <cstring> 
#include <algorithm>  
using namespace std ;  
 
int main() {  
    int t , p , n , i , j , max1 , min1 , sum ;  
   	std::ios::sync_with_stdio(false);
    int a[1300] ; 
 
   cin>>t;
    for(p=1;p<=t;p++)
    {  
       cin>>n; 
        for(i = 0 ; i < n ; i++) {  
           cin>>a[i];
            max1 = max(max1,a[i]) ;  
        }  
        min1 = max1 ;  
        for(i = 1 ; i <= max1 ; i++)
        {  
            sum = i ;  
            for(j = 0 ; j < n ; j++)
            {  
                if( a[j] > i ) 
                {  
                    if( a[j]%i != 0 )  
                        sum += (a[j]/i) ;  
                    else  
                        sum += (a[j]/i-1) ;  
                }  
            }  
            min1 = min(min1,sum) ;  
        }  
       cout<<"Case #"<<p<<":"<<" "<<min1<<endl;
    }  
    return 0 ;  
}  
