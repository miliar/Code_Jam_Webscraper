#include <bits/stdc++.h>
using namespace std ;

int arr [1000000] ;

int main(){
 int i , j ,k , test ;
 
 

 
 
 cin >> test ;
 int a , b ;
 for ( int kase= 1 ; kase <= test; kase++){
    cin >> a >> b >> k ;
    int ans = 0 ;
    for ( i = 0 ;  i < a ; i++)
    for ( j = 0 ; j < b ; j++)
    {
    	// cout << (i&j) << endl; 
    	 if ( (i&j) < k)
    	 ans++ ;
    }
   
   printf("Case #%d: %d\n",kase , ans);

 }
return 0 ;

}