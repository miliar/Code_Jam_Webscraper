#include <bits/stdc++.h>
using namespace std;

char opp(char x)
{
  if (x=='-') return '+';
  return '-';
}

void swap(int k,char* str)
{
  char firstK[k];
  for (int i = 0;i<k;++i)
    firstK[i] = str[i];
  for (int i = 0;i<k;++i)
    str[k-1-i] = opp(firstK[i]);
}

int solve(int n, char* str)
{
  int s = 0;
  for (int k = n; k>0;--k)
  {
    if (str[k-1] == '+') continue;
    //cout<<"Before "<<str<<endl;
    if (str[0] == '-')
    {
      swap(k,str);
      s++;
    }
    else
    {
      int p = 1;
      while (str[p]=='+') p++;
      swap(p,str);
      s++;
      swap(k,str);
      s++;
    }
    //cout<<"After "<<str<<endl;
  }
  return s;
}

main()
{
  int T;
  cin>>T;
  for (int t = 1;t<=T;++t)
  {
    cout<<"Case #"<<t<<": ";
    //cout<<endl;
    string pancakes;
    cin>>pancakes;
    char* s = new char[pancakes.length()];
    strcpy(s,pancakes.c_str());
    cout<<solve(pancakes.length(),s);
    cout<<endl;
  }
}
