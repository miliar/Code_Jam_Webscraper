#include <cassert>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <cctype>
#include <cmath>
#include <algorithm>
#include <iostream>
#include <iomanip>
#include <numeric>
#include <bitset>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <sstream>
#include <iterator>

#define FOR(i,n)   for(int i=0;i<n;i++)
#define FORA(a,i,n)   for(int i=a;i<n;i++)
using namespace std;
template<class T> string tostring(T x){
ostringstream sout;
sout<<x;
return sout.str();
}
template< class T > int toint( T s ){
int v;
istringstream sin(tostring(s));
sin>>v;
return v;
}
vector< string > split( string sentence ){
   istringstream iss( sentence );
   vector< string > tokens;
   copy( istream_iterator< string >(iss), istream_iterator< string >(), back_inserter<vector< string > >(tokens));
   return tokens;
}
string conversion(int a, int b){

       string cambio;
       int suma=0;
       int coci = a;
       while(coci>0){
                     cambio += tostring(coci%b);
                     coci = coci/b;
      }
     return string(cambio.rbegin(),cambio.rend());

       }
int GCD( int a , int b ) {
     if ( a%b==0) return b ;
      else
      return GCD( b , a % b) ;
}

void count( int &k, vector<bool> &nums, int n){
   while(n>0){
      if(nums[n%10]==false){
         nums[n%10] =true;
         k++;
      }
      n = n/10;
      
   }
}
int main(){
    freopen("input.in","r",stdin);
    freopen("output.out","w",stdout);
    //system("pause");
    int m;
    cin>>m;
    int n;
    
    int cases = 1;
    
    while( m-- ) {
         vector<bool> num(10,false);
         int k = 0;
         int i=1;
       int z=0;
         cin>>z;
         n = z;
         printf("Case #%d: ",cases++);
         while(true){
            //cout<<n<<endl;
            if( k == 10){
               cout<<n<<endl;
               break;
            }
            if( n == 0 ){
               cout<<"INSOMNIA"<<endl;
               break;
            }
            n = (i++)*z;
            count(k,num,n);
            
         }
    
    }
    return 0;

    }
