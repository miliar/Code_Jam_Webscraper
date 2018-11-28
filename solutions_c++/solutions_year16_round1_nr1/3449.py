#include<bits/stdc++.h>
using namespace std;
deque <char> q;
int main()
{
    long long int tmp,ans,i,j,n,m,v=1,t,d1,d2;
    freopen("output.txt", "w", stdout);
    cin>>t;
    string s;
    while(t--)
    {

    cin>>s;
    n=s.length();
    q.push_back(s[0]);
    for(i=1;i<n;i++)
    {
        //d1=abs(s[i]-q.front());
        //d2=abs(s[i]-q.back());
        if(q.front()<=s[i])
        {
            q.push_front(s[i]);
        }
        else if( q.back()>=s[i])
        {
            q.push_back(s[i]);
        }
        else
        {
           q.push_back(s[i]);
        }
    }
     cout<<"Case #"<<v++<<": ";
     while(!q.empty())
     {
         cout<<q.front();
         q.pop_front();
     }
       cout<<endl;
    }

    }

