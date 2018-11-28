#include <iostream>

using namespace std;

int main()
{
   unsigned int testCases;
   cin >> testCases;
   for( size_t i = 1; i <= testCases; ++i )
   {
      unsigned int line1[4];
      unsigned int line2[4];
      for( size_t k = 0; k < 2; ++k )
      {
	 unsigned int rowPicked;
	 unsigned int scrap;
	 cin >> rowPicked;
	 for( size_t j = 1; j < rowPicked; ++j )
	 {
	    cin >> scrap >> scrap >> scrap >> scrap;
	 }
	 if( k == 0 )
	 {
	    cin >> line1[0] >> line1[1] >> line1[2] >> line1[3];

	 }
	 else
	 {
	    cin >> line2[0] >> line2[1] >> line2[2] >> line2[3];
	 }
	 for( size_t j = rowPicked + 1; j <=4; ++j )
	 {
	    cin >> scrap >> scrap >> scrap >> scrap;
	 }
      }

      unsigned int answer = 0;
      for( size_t m = 0; m < 16; ++m )
      {
	 if( line1[m/4] == line2[m%4] )
	 {
	    if( answer == 0 )
	    {
	       answer = line1[m/4];
	    }
	    else
	    {
	       answer = 17;
	       break;
	    }
	 }
      }

      cout << "Case #" << i << ": ";


      switch( answer )
      {
	 case 0:
	    cout << "Volunteer cheated!" << endl;
	    break;
	 case 17:
	    cout << "Bad magician!" << endl;
	    break;
	 default:
	    cout << answer << endl;
      }
   }
   return 0;
}
