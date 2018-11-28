// https://code.google.com/codejam/contest/2270488/dashboard

#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

#define FOR(i, s, t) for(i = (s); i < (t); i++)

vector<string> m(4);
int T, caseNo;

bool Verify (string);
void End (int status);

int main()
{
   cin >> T;
   int i, j;
   string line, col, d1, d2;
   bool status;
   FOR(caseNo, 1, T + 1) {
      status = false;
      d1 = d2 = "";
      
      // read
      FOR (i, 0, 4) {
         cin >> line;
         m[i] = line;
      }
      
      FOR (i, 0, 4) {
         if (status = Verify(m[i]))
            break;         // verify the lines
         d1 += m[i][i];    // build diagonals
         d2 += m[i][3 - i];
      }
      if (status)    continue;
      
      //verify the diagonals
      if (Verify(d1))
         continue;
      if (Verify (d2))
         continue;
      
      // verify the cols
      FOR (i, 0, 4) {
         col = "";
         FOR (j, 0, 4)
            col += m[j][i];
         if (status = Verify(col))
            break;
      }
      if (status)    continue;
      
      bool emptyPlaces = false;
      FOR (i, 0, 4)
         emptyPlaces = (m[i].find(".") != string::npos);
      if (emptyPlaces) {
         End(-1);     // Not Completed
         continue;
      }
         
      End(0);       // Draw
   }
   return 0;
}

bool Verify (string s)
{
   if (s.size() != 4)
      cerr << "Invalid string length: " << s << '(' << s.size() << ")\n";
   
   bool t = (s.find("T") != string::npos);
   int noX = count (s.begin(), s.end(), 'X');
   if ( noX == 4 || (noX == 3 && t)) {
      End(1);        // X won
      return true;
   }
      
   int noO = count (s.begin(), s.end(), 'O');
   if (noO == 4 || (noO == 3 && t)) {
      End(2);        // O won
      return true;
   }
   return false;
}

void End(int status)
{
   cout << "Case #" << caseNo << ": ";
   switch (status) {
      case 0:     cout << "Draw"; break;
      case 1:     cout << "X won"; break;
      case 2:     cout << "O won"; break;
      case -1:    cout << "Game has not completed"; break;
      default:    cerr << "Invalid game status\n";
   }
   cout << '\n';
}
