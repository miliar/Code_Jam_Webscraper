#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main()
{
    int t;
    cin>>t;
    int cs=1;
    while(t--)
    {
        deque <char> dq;
        string s;
        cin>>s;
        for(int i=0;i<s.size();i++)
        {
            if(dq.size()==0)
            {
                dq.push_front(s.at(i));
            }
            else if(s.at(i)>=dq.front())
            {
                dq.push_front(s.at(i));
            }
            else
            {
                dq.push_back(s.at(i));
            }
        }
        cout<<"Case #"<<cs<<": ";
        for(int i=0;i<s.size();i++)
        {
            char c=dq.front();
            dq.pop_front();
            cout<<c;
        }
        cout<<"\n";
        cs++;
    }
    return 0;
}
