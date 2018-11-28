#include<bits/stdc++.h>
using namespace std;
class comp{
     public:
     bool operator()(pair<int,int> p1,pair<int,int> p2)
     {
          if(p1.first<p2.first)
          return 1;
          return 0;
     }
};
int main()
{
     int t,n,a[1000],o=0;
     cin>>t;
     while(t--)
     {o++;
     cout<<"Case #"<<o<<": ";
          int b,sum=0;
          cin>>n;
          char ch;
          priority_queue<pair<int,int>,vector<pair<int,int> >,comp> pq;
          for(int i=0;i<n;i++)
          {
               cin>>b;
               sum+=b;
               pq.push(make_pair(b,i));
          }
          while(pq.size()>1)
          {
               pair<int,int> c=pq.top();
               pq.pop();
               pair<int,int> d=pq.top();
               if((sum-1)/2>=d.first)
               {
                    c.first--;
                    sum--;
                    ch=c.second+'A';
                    cout<<ch<<" ";
                    if(c.first>0)
                    pq.push(c);
               }
               else
               {
                    pq.pop();
                    c.first--;
                    d.first--;
                    sum-=2;
                      ch=c.second+'A';
                    cout<<ch;
                      ch=d.second+'A';
                    cout<<ch<<" ";
                    if(c.first>0)
                    pq.push(c);
                    if(d.first>0)
                    pq.push(d);
                    
               }
          }
          
          pair<int,int> d=pq.top();
          if(pq.size()>0)
          while(d.first>0)
          {
               ch=d.second+'A';
               cout<<ch<<" ";
               d.first--;
          }
          cout<<"\n";
     }
}