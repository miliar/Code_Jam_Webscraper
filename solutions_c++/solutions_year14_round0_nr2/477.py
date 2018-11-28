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
	//ifstream in("B-small-attempt0.in");
   //ofstream out("B-small-attempt0.out");

	ifstream in("B-large.in");
   ofstream out("B-large.out");
   out.setf(ios_base::fixed, ios_base::floatfield);
   out.precision(7);
	int iTasks;
	in >> iTasks;

	for( int iCount = 1; iCount <= iTasks; iCount++ )
	{
      double C, F, X;
      in >> C >> F >> X;
      double V = 2.0;
      double rem = 0.0;
      int nFactories = 0;
      double timeFactories = 0.0;
      double timeAll = (X - rem)/(nFactories * F + V);
      double timePrev = timeAll + 1.0;
      while( timeAll < timePrev )
      {
         timePrev = timeAll;

         double timeFactory = (C - rem)/(nFactories * F + V);
         timeFactories += timeFactory;

         double timeXFactory = (X - rem)/((nFactories + 1) * F + V);
         timeAll = timeFactories + timeXFactory;

         nFactories++;         
         
      }

               //double timeFactoryNext = (C - rem)/((nFactories + 1) * F + V);
		out << "Case #" << iCount << ": " << timePrev << endl;
	}
	return 0;
}
