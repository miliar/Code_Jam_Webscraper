#include<bits/stdc++.h>
using namespace std;
int main()
{
    //freopen("oj22.in","r",stdin);
    //freopen("test.txt","w",stdout);
  long long t,i,m;
  cin>>t;
  for(m=1;m<=t;m++)
  {
      long long counter=0;
      string s;
        cin>>s;
       for(i=1;i<s.length();i++)
       {
           if(s[i]!=s[i-1])
           {
               counter++;
           }
       }
       if(s[s.length()-1]=='-')
       {
           cout<<"Case #"<<m<<": "<<counter+1<<endl;
       }
       else
       {
           cout<<"Case #"<<m<<": "<<counter<<endl;
       }
  }
}
