#include <bits/stdc++.h>
using namespace std;

#define endl "\n"
typedef long long int ll;

int main()
{
  ios::sync_with_stdio(false);  cin.tie(0);  cout.tie(0);
  
  int t, teste=1;
  string s;
  
  cin >> t;
  while(t--)
  {
    cin >> s;
    int c=0;
    if(s[s.size()-1]=='-') c=1;
    for(int i = 1; i < s.size(); i++)
      if(s[i] != s[i-1]) c++;
    cout << "Case #" << teste++ << ": " << c << endl;
  }
  
  return 0;
}
