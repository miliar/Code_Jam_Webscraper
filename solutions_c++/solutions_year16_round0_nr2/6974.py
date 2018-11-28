#include<bits/stdc++.h>
using namespace std;
int main()
{
 int t;
 cin>>t;int k=1;
 while(t--)
   {
    string s;
    cin>>s;
    int count=0,ans=0,count1=0;
    int len=s.length();
    if(len==1)
    {
     if(s[0]=='+')
     cout<<"Case #"<<k<<": 0"<<endl;
     else
    cout<<"Case #"<<k<<": 1"<<endl;
    }
    else
    {
    for(int i=0;i<len-1;i++)
    {
     if(s[i]=='-' && s[i+1]=='+')
     count++;
    }
    for(int i=0;i<len-1;i++)
    {
     if(s[i]=='+' && s[i+1]=='-')
     {
      count1++;
     }

    }
    if(count==0 && count1==0)
    {
     if(s[0]=='-')
      cout<<"Case #"<<k<<": 1"<<endl;
     else
     cout<<"Case #"<<k<<": 0"<<endl;
    }
    else
    {
      if(count > count1)
      ans=2*count-1;
      else if( count==count1 && s[0]=='-' && s[len-1]=='-')
      {
        ans=2*(count1)+1;
      }
      else
      ans=2*count1;
       cout<<"Case #"<<k<<": "<<ans<<endl;
    }

    }
    k++;
   }
}
