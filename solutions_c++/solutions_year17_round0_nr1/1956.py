#include <bits/stdc++.h>

using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    ifstream cin("A-large.in");
    ofstream cout("A-large.out");
    int n;
    cin>>n;
    for (int test=1; test<=n; test++)
    {
        int k;
        string s;
        cin>>s>>k;
        int ans=0;
        for (int i=0; i<=(int)s.size()-k; i++)
        {
            if (s[i]=='-')
            {
                for (int j=0; j<k; j++)
                {
                    if (s[i+j]=='+')
                        s[i+j]='-';
                    else
                        s[i+j]='+';
                }
                ans++;
            }
        }
        int f=0;
        for (int i=0; i<s.size(); i++)
        {
            if (s[i]=='-')
            {
                f=1;
                break;
            }
        }

        if (f)
            cout<<"Case #"<<test<<": IMPOSSIBLE\n";
        else
            cout<<"Case #"<<test<<": "<<ans<<'\n';;
    }
    return 0;
}
