#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <fstream>
#include <map>
#include <sstream>

using namespace std;

void ReadRow(int nRow, vector<int>& rvRow, ifstream& in)
{
   int nBound = 4;
   for( int i = 0; i < nBound; i++ )
   {
      for( int j = 0; j < nBound; j++ )
      {
         if( i == nRow - 1 )
         {
            in >> rvRow[j];
         }
         else
         {
            int a;
            in >> a;
         }
      }      
   }
}

int main()
{
	ifstream in("A-small-attempt0.in");
   ofstream out("A-small-attempt0.out");

	//ifstream in("A-large.in");
 //  ofstream out("A-large.out");
   string sBad = "Bad magician!";
   string sCheater = "Volunteer cheated!";
	int iTasks;
	in >> iTasks;

	const int nMaxLines = 10;
	for( int iCount = 1; iCount <= iTasks; iCount++ )
	{
      int nRow1;
      in >> nRow1;
      vector<int> vRow1(4);
      ReadRow(nRow1, vRow1, in);

      int nRow2;
      in >> nRow2;
      vector<int> vRow2(4);
      ReadRow(nRow2, vRow2, in);

      vector<int> vMatches;

      for( size_t i = 0; i < vRow1.size(); i++ )
      {
         for( size_t j = 0; j < vRow2.size(); j++ )
         {
            if( vRow1[i] == vRow2[j] )
            {
               vMatches.push_back(vRow1[i]);
               break;
            }
         }
      }      

      out << "Case #" << iCount << ": ";
      if( vMatches.size() == 1 )
      {
         out << vMatches.front() << endl;
      }
      else if( vMatches.empty() )
      {
         out << sCheater << endl;
      }
      else
      {
         out << sBad << endl;
      }
	}
	return 0;
}
