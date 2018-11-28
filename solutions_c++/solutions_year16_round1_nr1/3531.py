#include<iostream>
#include<algorithm>
#include<vector>
#include<map>
#include <deque>
#include<cstdio>
#include<cstring>
using namespace std;
deque<char> m;
deque<char>::iterator it;

int main()
{
  long long i,n,t,k,sum,j;
  char a[100005],prev,fron;
  cin>>t;
  
 string s;
  for(j=1;j<=t;j++)
  {
     cin>>a;
     m.clear();
     prev=fron=a[0];
     m.push_front(a[0]);
     for(i=1;a[i]!='\0';i++)
     {
         if(a[i]>=prev)
         {
             prev=a[i];
             m.push_front(a[i]);
         }
         else
         m.push_back(a[i]);
     }
     it= m.begin();
     cout<<"Case #"<<j<<": ";
     while(it != m.end())
        cout<< *it++;
    cout<<endl;
  }
  
} 