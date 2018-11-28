/*
Date : 
Time : 
author - @alphaprticle
Problem id : 
Problem name : 
Problem Link : 
*/

#include <bits/stdc++.h>
using namespace std ;

#define INF 18446744073709551610 
#define LIM 1000000
#define readi(n) scanf("%d", &n) ;
#define readc(c) scanf("%c", &c) ;
#define read2i(n,m) scanf("%d %d", &n , &m) ;
#define read3i(a,b,c) scanf("%d %d %d",&a ,&b ,&c);
#define pb push_back
#define rep(i,n) for( int i = 0 ; i < n ; i++)
#define reps(i,a,b) for(int i = a ; i <= b ; i++) 
#define rev(i,b,a) for(int i = b ; i >= a ; i--)
#define P first
#define Q second

typedef long long ll ;
typedef pair <int,int> ii ;
typedef vector < ii > vii ;
typedef vector < vii> viii ;

/*
GCD
ll gcd(ll a, ll b) { return (b == 0 ? a : gcd(b, a % b)); }
*/

/*
  //Seive
  bool p[LIM] ;
  vector <ll> prime ;
  void seive(){
	 memset (p , true ,sizeof p);
	 p[0] = p[1] = false ;
	 for ( ll i = 2 ; i <= LIM ; i++){
	   if(p[i])
	   {
	     prime.pb(i);
	     for ( ll j = i*i ; j <= LIM ; j += i)
	     p[j] = false ;
	   }
	 }
  }

*/
string s[11] ;


int main(){
  ll ways , test ;
  ll kase , i , j , k ;
  cin >> test ; 
  int n;
  for ( kase = 1 ; kase <= test ; kase++){
  	   cin >> n ;
  	   for ( i = 0 ; i < n ; i++){
  	   	  cin >> s[i] ;
  	   }
  	  
  	  int arr[n] ;
      for ( i = 0; i  < n ; i++)
      arr[i] = i ;
      ways = 0;
     // cout << "yashsn\n" ;
      bool first = true ;

      do{  
      	   if (!first){
      	   bool f = true ;
      	   for ( i = 0 ; i < 9 ; i++)
      	   if( arr[i] != i){ f =false ; break ;}
      	   if(f)
      	   break ;
      	  }
      	   first = false ;
      	  string temp ;
      	  for ( i = 0 ; i < n ; i++)
      	  	temp += s [arr[i]] ;
      	  bool f = true ;
          int kcount[26] ;
          memset (kcount , 0 ,sizeof kcount );
          for ( i = 0; i < temp.length() ; i++){
          	   if ( kcount[ temp[i] - 'a'] == 0)
          	    {
          	    	 kcount [ temp[i] - 'a' ] = 1 ; continue ; 
          	    }
          	   else if ( kcount[ temp[i] - 'a' ] > 0 && temp[i-1] == temp[i] ){
          	   	  kcount [ temp[i]- 'a' ]++ ;
          	   }  
          	   else{
          	   	f = false ; break ;
          	   }
          }
          if(f){
           // cout << temp << endl;
          	ways++ ;
          }

         ways %= 1000000007 ;
      }
      while ( next_permutation(arr,arr+n) ) ;

        printf("Case #%lld: %lld\n",kase , ways) ;
  }


	return 0;
}