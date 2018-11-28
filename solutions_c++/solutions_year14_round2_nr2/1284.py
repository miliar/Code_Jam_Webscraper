#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <fstream>
#include <map>
#include <sstream>

using namespace std;

int main()
{
	ifstream in("B-small-attempt0.in");
   ofstream out("B-small-attempt0.out");

	//ifstream in("B-large.in");
   //ofstream out("B-large.out");
//   out.setf(ios_base::fixed, ios_base::floatfield);
   //out.precision(7);
	int iTasks;
	in >> iTasks;

	for( int iCount = 1; iCount <= iTasks; iCount++ )
	{
      int A, B, K;
      in >> A >> B >> K;
      int nWins = 0;
      for( int i = 0; i < A; i++ )
      {
         for( int j = 0; j < B; j++ )
         {
            if( (i & j) < K )
            {
               nWins++;
            }
         }
      }
		out << "Case #" << iCount << ": " << nWins << endl;
	}
	return 0;
}
