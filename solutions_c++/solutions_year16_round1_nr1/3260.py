#include<bits/stdc++.h>
using namespace std;
#define ll long long 
int main()
{
     ll t,n,o=0;
     string st;
     cin>>t;
     while(t--)
     {o++;
          cin>>st;
          list<char> q;
          
          n=st.size();
          char ch=st[0];
          q.push_back(st[0]);
          for(int i=1;i<n;i++)
          {
               if(st[i]>=ch)
               {
                    q.push_front(st[i]);
                    ch=st[i];
               }
               else
               {
                    q.push_back(st[i]);
               }
          } cout<<"Case #"<<o<<": ";
          while(q.size()>0)
          {
              
               cout<<q.front();
               q.pop_front();
          }cout<<"\n";
     }
}