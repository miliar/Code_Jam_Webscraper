#include<bits/stdc++.h>
using namespace std;
int main()
{
  int t ;
  cin >> t;
  for( int test = 1 ; test <= t ; test++ )
  {
    string s;
    cin >> s;
    reverse( s.begin(), s.end() );
    int ans = 0;
    for( int i = 0 ; i < s.length() ; i++ )
    {
      if( s[i] == '-' )
      {
        ++ans;
        for( int j = i ; j < s.length() ; j++ )
        {
          if( s[j] == '+' )
            s[j] = '-';
          else s[j] = '+';
        }
      }
    }
    cout<<"Case #"<< test <<": "<< ans << endl;
  }
  return 0;
}

