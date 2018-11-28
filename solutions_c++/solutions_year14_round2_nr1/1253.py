#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <fstream>
#include <map>
#include <sstream>
#include <set>

using namespace std;

int main()
{
	//ifstream in("A-small-attempt0.in");
   //ofstream out("A-small-attempt0.out");

	ifstream in("A-large.in");
   ofstream out("A-large.out");
	int iTasks;
	in >> iTasks;

	for( int iCount = 1; iCount <= iTasks; iCount++ )
	{
      int N;
      in >> N;
      set<string> Strings;
      vector<vector<string> >vStrings;
      bool bCanWin = true;
      int nMoves = 0;
      for ( int i = 0; i < N; i++ )
      {
         string s;
         in >> s;
         if( !bCanWin )
            continue;
         vStrings.push_back(vector<string>());
         char c = 0;
         int same = 0;
         for( int j = 0; j < s.size() && bCanWin; j++ )
         {            
            if( s[j] != c )
            {
               if( c != 0 )
               {
                  vStrings[i].push_back(string(same, c));
               }
               same = 1;
               c = s[j];
            }
            else
            {
               same++;
            }
         }
         vStrings[i].push_back(string(same, c));
         if( i > 0 )
         {
            bCanWin = vStrings[i].size() == vStrings[i-1].size();
            for( int k = 0; k < vStrings[i].size() && bCanWin; k++ )
            {
               if( vStrings[i][k][0] != vStrings[i-1][k][0] )
                  bCanWin = false;
            }
         }
      }
      if( bCanWin )
      {
         int nMax = 0;
         for( int i = 0; i < vStrings[0].size(); i++ )
         {
            for( int k = 0; k < vStrings.size(); k++ )
            {
               if( vStrings[k][i].size() > nMax )
                  nMax = vStrings[k][i].size();
            }

            int nMinMoves = 1000000000;
            for( int j = 1; j <= nMax; j++ )
            {
               int nTempMoves = 0;
               for( int k = 0; k < vStrings.size(); k++ )
               {
                  nTempMoves += abs(j - (int)vStrings[k][i].size());
               }
               if( nTempMoves < nMinMoves )
                  nMinMoves = nTempMoves;
            }
            nMoves += nMinMoves;

         }         
      }
      
      out << "Case #" << iCount << ": ";
      if( bCanWin )
         out << nMoves;
      else
         out << "Fegla Won";
      out << endl;
	}
	return 0;
}
