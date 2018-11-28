#include <bits/stdc++.h>
#define ll long long int 
using namespace std;

int main() {
  // your code goes here
  ll t,t1,i,c;
  char ch,ch1,l;
  string s;
  cin>>t;
  t1=0;
  while(t--)
  {
      cin>>s;
      t1++;
      cout<<"Case #"<<t1<<": ";
      ch=s[0];l=ch;
      i=1;
      c=1;
      while(s[i]!=NULL)
      {
         // printf("!");
          ch1=s[i];
          if(ch!=ch1)
          c++;
          l=ch1;
          i++;
          ch=ch1;
      }
      if(l=='+')
      c--;
      cout<<c<<"\n";
  }
  return 0;
}
