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
        int ans=0;
        for(int i=1; i<(int)str.size(); i++)
            if(str[i]!=str[i-1])
                ans++;
        if(str[(int)str.size()-1]=='-')
            ans++;
        cout<<"Case #"<<tc<<": "<<ans<<endl;
    }
    return 0;
}