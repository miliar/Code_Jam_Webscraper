#include<iostream>
#include<algorithm>
using namespace std;
#define ull  long long 
#define inf 200000000000000000ull
ull r;

ull par( ull n ){
  if( n <= 0 ) return 0;
  return n * (  n * 2  + 1 );
}

ull impar( ull n ){
  if( n <= 0 ) return 0;
  return n * (  n * 2  - 1 );
}

ull go( ull n ){
  if( n  % 2 == 0 ){
	 return par( n  / 2  ) - par( (r -1 ) / 2 ) ;
  }
  else{
     return impar( ( n + 1 ) / 2  ) - impar( (r  )/ 2  );  
  }
}


ull f( ull t ){
   ull lo = 1 , hi = 1000ull ;
   while( hi - lo > 1 ){
     ull mid = ( lo + hi )/ 2;
	 if( go( r + mid * 2 - 1 ) <= t ) lo = mid;
	 else hi = mid;   
   }
   return lo;
}

int main(){
   ull  tc ,t, c= 1  ;
   cin >> tc;
   while( tc-- ){
      cin >> r >> t ;
	  cout << "Case #"<<c++<< ": ";
      cout << f ( t );
	  cout <<endl;
   }
}
