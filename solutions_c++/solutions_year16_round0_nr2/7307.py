#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;

#define printFile(output_file,c,value) output_file << "Case #" << (c) << ": " <<  (value) << endl

int calcTurnCharToChar(char checkstr, char checkSymbol)
{
   if (checkstr == checkSymbol)
      return 0;
   else
      return 1;
}

int calcTurnStringToChar(const string & st, char symbol)
{
   string s = st;
   int steps = 0;
   if (s.length() > 1)
   {
      steps += calcTurnStringToChar( s.substr(0,s.length()-1) , s.at(s.length()-1)) + calcTurnCharToChar(s.at(s.length()-1), symbol);
   }
   else if (s.length() == 1)
   {
      steps += calcTurnCharToChar(s.at(s.length()-1), symbol);
   }
   else
   {
      steps = 0;
   }
   return steps;
}

int main()
{
   ifstream in("input.in");
	ofstream out("output.out");

   int T = 0;
	in >> T;

	for (int _case = 1; _case <= T;  _case++)
   {
      int steps = 0;

      string S;
      getline(in, S);
      int l = S.length();
      while(l==0)
      {
         getline(in, S);
         l = S.length();
      }

      char c = S.at(l-1);

      if (l > 1)
      {
         int i;
         for (i = l - 1; i>=0; i--)
         {
            if (S.at(i) != c)
               break;
         }
         steps = calcTurnStringToChar(S.substr(0,i+1), c) + calcTurnCharToChar(c,'+');
      }
      else
      {
         steps = calcTurnCharToChar(S.at(l-1),'+');
      }
      printFile(out,_case,steps);
   }

   return 0;
}