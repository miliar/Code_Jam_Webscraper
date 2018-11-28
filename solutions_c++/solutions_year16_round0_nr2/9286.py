#include<iostream>

using namespace std;

string flip(string s)
{
  int len = s.length();
  string res="";
  for(int i=0;i<len;i++)
  {
    if(s[i] == '+')
      res = '-'+res;
    else if(s[i] == '-')
      res = '+'+res;
  }
  return res;
}

int func(int res, string s)
{
  int n = s.length();
  if(s=="")
  {
    return res;
  }
  if(s[n-1]=='+')
  {
    int ctr = n-1;
    while(ctr>=0 && s[ctr] == '+')
    {
      ctr--;
    }
    ctr++;
    return func(res, s.substr(0,ctr));
  }
  if(s[0] == '-')
  {
    return func(res+1, flip(s));
  }
  if(s[0] == '+')
  {
    int ctr = 0;
    while( ctr<n && s[ctr] == '+')
    {
      ctr++;
    }
    return func(res+1, flip(s.substr(0, ctr)) + s.substr(ctr,n));
  }
  
}


int main()
{
  int t;
  cin>>t;
  int icase =1;
  while(t--)
  {
    string s;
    cin>>s;   
    
    cout<<"Case #"<<icase++<<": "<<func(0, s)<<endl;
  }
  
  
  return 0;
}