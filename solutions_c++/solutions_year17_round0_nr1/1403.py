#include <bits/stdc++.h>
using namespace std;

ifstream fin("A-large.in");
ofstream fout("A-large.sol");

int main()
{
    int t,k;
    string s;
    fin>>t;
    for(int i=0;i<t;i++)
    {
        int ans=0,br=0;
        fin>>s>>k;
        for(int j=0;j<s.size()-k+1;j++)
        {
            if(s[j]=='-')
            {
                for(int r=0;r<k;r++)
                {
                    if(s[j+r]=='-')s[j+r]='+';
                    else s[j+r]='-';
                }
                ans++;
            }
        }
        fout<<"Case #"<<i+1<<": ";
        for(int j=0;j<s.size();j++)if(s[j]=='+')br++;
        if(br==s.size())fout<<ans<<endl;
        else fout<<"IMPOSSIBLE\n";
    }
    return 0;
}
