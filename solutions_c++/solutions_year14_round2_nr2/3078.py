#include <iostream>
#include <vector>
#include <unordered_map>


using namespace std;

int main()
{
   unsigned long long int testCases;
   cin >> testCases;
   for( size_t t = 1; t <= testCases; ++t )
   {
      unsigned long long int a,b,c;
      cin >> a >> b >> c;
      unsigned long long int counter = 0;
      for( unsigned long long int i = 0; i<a;++i )
      {
	 for( unsigned long long int j = 0; j<b;++j )
	 {
	    if( (i & j) < c )
	       ++counter;
	 }
      }      
      cout << "Case #" << t << ": " << counter << endl;
      
      
   }
   return 0;
}
