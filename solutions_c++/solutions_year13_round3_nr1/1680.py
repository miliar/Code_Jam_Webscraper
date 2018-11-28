#include <iostream>
#include <string>
#include <ctype.h>

using namespace std;

bool consecutive(const string & sub, int n)
{
  int count = 0;
  int max = 0;
  for ( int i=0; i < sub.size(); i++ )
  {
    char a = tolower(sub[i]);
    if ( a == 'a' || a == 'e' || a == 'i' || a == 'o' || a == 'u' )
    {
      if ( count > max ) max = count;
      count = 0;
    }
    else count++;
  }
  if ( count > max ) max = count;
  if ( max >= n ) { return true; }
  return false;
}

int main(int argc, char const* argv[])
{
  int T, rT = 0;
  cin >> T;
  while ( rT++ != T )
  {
    string name;
    int n;
    int res = 0;
    cin >> name >> n;
    for ( int i=0; i < name.size(); i++ )
      for ( int j=i; j < name.size(); j++ )
      if ( j-i+1 >= n )
      {
        string sub = name.substr(i, j-i+1);
        if ( consecutive(sub, n) ) res++;
      }
    cout << "Case #" << rT << ": " << res << endl;
  }
  return 0;
}
