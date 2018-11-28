#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <fstream>
#include <map>
#include <sstream>
#include <list>

using namespace std;

int main()
{
	//ifstream in("D-small-attempt1.in");
   //ofstream out("D-small-attempt1.out");

	ifstream in("D-large.in");
   ofstream out("D-large.out");
	
	int iTasks;
	in >> iTasks;

	for( int iCount = 1; iCount <= iTasks; iCount++ )
	{
      if( iCount == 46 )
         int h = 1;
      int N;
      in >> N;
      vector<double> vNaomi(N);
      vector<double> vKen(N);
      for( int i = 0; i < N; i++ )
         in >> vNaomi[i];

      for( int i = 0; i < N; i++ )
         in >> vKen[i];

      sort(vNaomi.begin(), vNaomi.end());
      sort(vKen.begin(), vKen.end());

      int nWar = 0;
      int nDWar = 0;
      int nNaomiCurPos = vNaomi.size() - 1;
      int nNaomiLastPos = 0;
      int nKenCurPos = vKen.size() - 1;
      int nKenLastPos = 0;

      while(nNaomiCurPos >= nNaomiLastPos)
      {
         if(vKen[nKenCurPos] < vNaomi[nNaomiCurPos])
         {
            nKenLastPos++;
            nNaomiCurPos--;
            nWar++;
         }
         else
         {
            nKenCurPos--;
            nNaomiCurPos--;            
         }
      }

      nNaomiCurPos = vNaomi.size() - 1;
      nNaomiLastPos = 0;
      nKenCurPos = vKen.size() - 1;
      nKenLastPos = 0;

      while(nNaomiCurPos >= nNaomiLastPos)
      {
         if(vKen[nKenLastPos] >= vNaomi[nNaomiLastPos])
         {
            nKenCurPos--;
            nNaomiLastPos++;            
         }
         else
         {
            nDWar++;
            nKenLastPos++;
            nNaomiLastPos++;            
         }
      }
		out << "Case #" << iCount << ": " << nDWar << " " << nWar << endl;
	}
	return 0;
}
