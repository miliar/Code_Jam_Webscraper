#include <bits/stdc++.h>

using namespace std;

int main ()
{
    int n;
    cin>>n;
    for (int i = 1 ; i <= n ; i++)
    {
        string s;
        deque <char> resp;
        cin>>s;
        resp.push_back(s[0]);
        for (int i = 1; i < s.size() ; i++)
        {
            if(resp.front()>s[i])
                resp.push_back(s[i]);
            else
                resp.push_front(s[i]);
        }
        string ans(resp.begin(),resp.end());
        cout<<"Case #"<<i<<": "<<ans<<endl;
    }
    return 0;
}
