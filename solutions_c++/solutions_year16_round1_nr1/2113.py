#include<iostream>
#include<vector>
using namespace std;
int main()
{
    int t,t1=1,i,pos;
    cin>>t;
    while(t1<=t)
    {
      vector<char> s1,s2;
      string s;
      cin>>s;
      pos=0;
      s1.push_back(s[0]);
      s2.push_back(s[0]);
      for(i=1;i<s.size();i++)
      {
        if(s[i]>=s1[pos])
        {
          s1.push_back(s[i]);
          pos++;
        }
        else
        {
          s2.push_back(s[i]);
        }
      }
      cout<<"Case #"<<t1<<": ";
      for(i=s1.size()-1;i>=0;i--)
      {
        cout<<s1[i];
      }
      for(i=1;i<s2.size();i++)
      {
        cout<<s2[i];
      }
      cout<<endl;
      t1++;
    }
    return 0;
}
