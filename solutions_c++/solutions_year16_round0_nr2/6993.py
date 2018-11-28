#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main()
{
    ofstream file;
    file.open ("large");
    int t;
    cin>>t;
    for(int i=0; i<t; i++)
    {
        string s;
        cin>>s;
        stack<char>q;
        for(int i=(s.size()-1); i>=0; i--)
            if(q.empty())
                q.push(s[i]);
            else
            {
                if(s[i]==q.top())
                    continue;
                else
                    q.push(s[i]);
            }
        int coun=0;
        if(q.top()=='-')
            coun=-1;
        while(!q.empty())
        {
            if(q.top()=='-')
                coun+=2;
            q.pop();
        }
        file<<"Case #"<<i+1<<": "<<coun<<endl;
    }
    file.close ();
    return 0;
}
