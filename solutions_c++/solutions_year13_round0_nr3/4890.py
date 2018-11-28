#include<iostream>
#include<string>
#include<cstring>
#include<cmath>

using namespace std;

int palindromecheck (int x)
{
  string s="";
  int y,l,r,n,mid;
  while(x!=0)
  {
    s+=char(x%10+'0');
    x/=10;
  }
  ///reverse(s.begin(),s.end());
  n=s.size();
  l=0;r=n-1;
  while(l<=r)
  {
    if(s[l]!=s[r])return 0;
    l++;r--;
  }
  return 1;
}

int main ()
{
  int t,k;
  cin>>t;
  for(k=0;k<t;k++)
  {
    int a,b,i,j,p,q,ans=0;
    cin>>a>>b;
    for(i=a;i<=b;i++)
    {
      if(palindromecheck(i)==1)
      {
        q=sqrt(i);
        if(q*q==i)
        if(palindromecheck(q)==1)ans++;
      }
    }
    cout<<"Case #"<<k+1<<": "<<ans<<endl;
  }
}