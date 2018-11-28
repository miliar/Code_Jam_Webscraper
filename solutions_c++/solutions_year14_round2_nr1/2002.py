#include <iostream>
#include <string>

using namespace std;

int main()
{
  int t;
  int n;
  int c = 1;
  int counta[26], countb[26];
  string a, b;
  ios_base::sync_with_stdio(false);
  cin>>t;
  while(t--)
  {
    bool flag = false;
    cin>>n;
    cin>>a>>b;
    for(int i = 0; i < 26; i++)
      counta[i] = 0;
    for(int i = 0; i < a.size(); i++)
      counta[a[i]-97]++;
    for(int i = 0; i < 26; i++)
      countb[i] = 0;
    for(int i = 0; i < b.size(); i++)
      countb[b[i]-97]++;
    int i;
    for(i = 0; i < 26; i++)
      if((counta[i] == 0 && countb[i] != 0) || (counta[i] != 0 && countb[i] == 0))
        break;
    if(i != 26)
      cout<<"Case #"<<c<<": Fegla Won\n";
    else
    {
      int j = 0;
      i = 0;
      int answer = 0;
      char prev = a[0];
      while(i != a.size() && j != b.size())
      {
        if(a[i] == b[j])
        {
          prev = a[i];
          i++; j++;
        }
        else
        {
          if(a[i] == prev) i++;
          else if(b[j] == prev) j++;
          else
          {
            flag = true;
            break;
          }
          answer++;
        }
      }
      while(i != a.size())
      {
        if(a[i] != prev)
        {
          flag = true;
          break;
        }
        i++, answer++;
      }
      while(j != b.size())
      {
        if(b[j] != prev)
        {
          flag = true;
          break;
        }
        j++, answer++;
      }
      if(flag)
        cout<<"Case #"<<c<<": Fegla Won\n";
      else
        cout<<"Case #"<<c<<": "<<answer<<"\n";
    }
    c++;
  }
  return 0;  
}
