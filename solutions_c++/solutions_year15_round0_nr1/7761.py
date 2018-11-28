#include <bits/stdc++.h>

using namespace std;

int main()
{
    ios::sync_with_stdio(false);

    int t;
    cin>>t;
    int tc = 1;

    while(tc<=t)
    {
        int n;
        string str;

        cin>>n>>str;

        int people_stood_up=0;
        int ans = 0;

        for(int i=0;i<str.length();i++)
        {
            if(people_stood_up>=i)
            {
                people_stood_up += (int)(str[i]-'0');
            }
            else
            {
                    int req = i-people_stood_up;
                    ans+=i-people_stood_up;
                    people_stood_up = i;
                    people_stood_up += (int)(str[i]-'0');
            }
        }

        cout<<"Case #"<<tc<<": "<<ans<<endl;
        tc++;
    }
    return 0;
}
