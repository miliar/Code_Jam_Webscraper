#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
   unsigned int testCases;
   cin >> testCases;
   for( size_t i = 1; i <= testCases; ++i ) {
      unsigned int maxShyness;
      cin >> maxShyness;
      cin.ignore();

      //Gather input
      vector<unsigned short int> audience;
      for( size_t j = 0; j <= maxShyness; ++j ) {
	 char c;
	 cin.get(c);
	 audience.push_back( c - '0' );
      }

      //Main Logic
      unsigned int up = 0, need = 0;
      for( size_t j = 0; j <= maxShyness; ++j ) {
	 if ((up + need) < j) {
	    need += j - up - need;
	 }
	 up += audience[j];
      }

      cout << "Case #" << i << ": " << need << endl;
   }
   return 0;
}
