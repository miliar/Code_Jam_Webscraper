#include <bits/stdc++.h>

using namespace std;

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int tn;
    cin>>tn;
    for(int tc=1; tc<=tn; tc++)
    {
        string str;
        cin>>str;
        deque<char> ans;
        ans.push_back(str[0]);
        for(int i=1; i<(int)str.size(); i++)
            if(ans.front() <= str[i])
                ans.push_front(str[i]);
            else
                ans.push_back(str[i]);
        cout<<"Case #"<<tc<<": ";
        while(!ans.empty())
        {
            cout<<ans.front();
            ans.pop_front();
        }
        cout<<endl;
    }

    return 0;
}