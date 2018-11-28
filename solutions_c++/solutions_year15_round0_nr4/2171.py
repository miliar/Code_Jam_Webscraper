#include <iostream>
#include <vector>
#include <algorithm>
#include <complex>

using namespace std;

int main()
{
   unsigned int testCases;
   cin >> testCases;
   for( size_t i = 1; i <= testCases; ++i )
   {
      unsigned int N_omino, r, c;
      cin >> N_omino >> r >> c;

      bool success = false;
      string reason = "";
      if((r * c) % N_omino != 0) {
	 success = false;
	 reason = "indivisible";
      } else if ( N_omino == 1 ) {
	 success = true;
	 reason = "size 1";
      } else if ( N_omino == 2 ){
	 success = true;
	 reason = "size 2";
      } else if ( N_omino == 3 && (r==1 || c==1) ) {
	 success = false;
	 reason ="narrow for 3";
      } else if ( N_omino == 3 ) {
	 success = true;
	 reason = "default for 3";

      // By here it should be size 4
      } else if ( N_omino > r && N_omino > c ) {
	 success = false;
	 reason = "edge could sticking out";
      } else if( sqrt(N_omino) > r || sqrt(N_omino) > c ) {
	 success = false;
	 reason = "shape could be square";
      } else if( (r == 2 || c == 2) && N_omino == 4 ) {
	 success = false;
	 reason = "narrow and weird shape";
      } else {
	 success = true;
	 reason = "default";
      }

      string winner = "undetermined";
      if(success)
	 winner = "GABRIEL";
      else
	 winner = "RICHARD";

      //if (reason == "indivisible" )
      //cout << "Case #" << i << ": " << N_omino << " " << r << " " << c << " " << (success? "yay" : "boo") << " " << winner << " " << reason << endl;
      cout << "Case #" << i << ": " << winner  << endl;
   }
   return 0;
}
