#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main()
{
  vector<int> vv(26, 0);
  vector< vector<int> > dict(10, vv);
  string ds[] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
  
  for (int i=0; i<10; i++)
  {
    for (int k=0; k<ds[i].length(); k++)
    {
      dict[i][ds[i][k]-'A'] ++;
    }
  }
  
  int T; cin >> T;
  for (int t=0; t<T; t++)
  {
    cout << "Case #" << t+1 << ": ";
    
    vector<int> v(26, 0);
    string s; cin >> s;
    for (int k=0; k<s.length(); k++)
    {
      v[s[k]-'A'] ++;
    }

    vector<int> n(10, 0);
    
    int k, l;
    
    k = 0; l = 'Z';
    n[k] = v[l-'A'];
    for (int i = 0; i<26; i++)
    {
      v[i] -= n[k] * dict[k][i];
    }
    
    k = 6; l = 'X';
    n[k] = v[l-'A'];
    for (int i = 0; i<26; i++)
    {
      v[i] -= n[k] * dict[k][i];
    }
    
    k = 2; l = 'W';
    n[k] = v[l-'A'];
    for (int i = 0; i<26; i++)
    {
      v[i] -= n[k] * dict[k][i];
    }
    
    k = 8; l = 'G';
    n[k] = v[l-'A'];
    for (int i = 0; i<26; i++)
    {
      v[i] -= n[k] * dict[k][i];
    }
     
    k = 4; l = 'U';
    n[k] = v[l-'A'];
    for (int i = 0; i<26; i++)
    {
      v[i] -= n[k] * dict[k][i];
    }
     
    k = 5; l = 'F';
    n[k] = v[l-'A'];
    for (int i = 0; i<26; i++)
    {
      v[i] -= n[k] * dict[k][i];
    }
     
    k = 7; l = 'V';
    n[k] = v[l-'A'];
    for (int i = 0; i<26; i++)
    {
      v[i] -= n[k] * dict[k][i];
    }
     
    k = 9; l = 'I';
    n[k] = v[l-'A'];
    for (int i = 0; i<26; i++)
    {
      v[i] -= n[k] * dict[k][i];
    }
    
    k = 1; l = 'N';
    n[k] = v[l-'A'];
    for (int i = 0; i<26; i++)
    {
      v[i] -= n[k] * dict[k][i];
    }
    
    k = 3; l = 'R';
    n[k] = v[l-'A'];
    for (int i = 0; i<26; i++)
    {
      v[i] -= n[k] * dict[k][i];
    }
    
    for (int i=0; i<10; i++)
    {
      for (int k=0; k<n[i]; k++)
      {
        cout << i;
      }
    }
    
    cout << endl;
  }  
  return 0;
}