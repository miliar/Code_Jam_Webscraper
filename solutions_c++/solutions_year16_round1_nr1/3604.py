#include <iostream>
#include <string>

using namespace std;

void stuff( int n)
{
  string is;
  getline(cin, is);
  //cout << is << endl; 

  string ostr;
  
  for (int i=0; i<is.length() && ostr[i] != '\n' && ostr[i] != '\t' ; i++)
  {
    char c = is[i];
    if (i == 0)
      ostr = c;
    else if (ostr[0] > c)
      ostr = ostr + c;
    else
      ostr = c + ostr;
    //cout << ostr << endl;  
  } 

  cout << "Case #" << n << ": " << ostr << endl;

}


int main()
{
  int doxman;   // For u daniel
  cin >> doxman;

  string empty;
  getline(cin, empty);
  for (int i=0; i<doxman; i++)
    stuff(i+1);
}
