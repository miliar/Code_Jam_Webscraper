/************************************************
 *                                              *
 *  Name: Andrew Wilkening                      *
 *  Date: 11 April 2015                         *
 *  File: 2015QualA.cpp                         *
 *  Description: Solving Problem A from the     *
 *    Google Code Jam 2015 Qualifier            *
 *                                              *
 ************************************************/

#include<iostream>
#include<fstream>

using namespace std;

int main()
{
  ifstream in("A-large.in");
  ofstream out("SO_Output.txt");
  int runs, sMax, sCurr, sK, inv;
  in >> runs;
  for(int i = 1; i <= runs; i++)
  {
    in >> sMax;
    sCurr = 0; inv = 0;
    for(int j = 0; j <= sMax; j++)
    {
      do
      {
        sK = in.get();
      }while(sK == ' ');
      sK = sK - '0';
      if(j > sCurr)
      {
        inv += j - sCurr;
        sCurr += j - sCurr;
      }
      sCurr += sK;
      if(sCurr >= sMax)
      {
        cout << "Exit early on: " << j << endl;
        in.ignore(1000, '\n');
        break;
      }
    }
    out << "Case #" << i << ": " << inv << endl;
  }
  in.close();
  out.close();
}
