#include <bits/stdc++.h>
using namespace std;
string s;
int k;
void invert(int idx)
{
    int i;
    for(i=idx;i<=idx+k-1;i++)
    {
        if(s[i]=='+') s[i]='-';
        else s[i]='+';
    }
}
int main()
{
    int t,tc=1;
    cin>>t;
    while(t--)
    {
        
        cin>>s;
        int n=s.length();
        cin>>k;
        int i,cnt=0;
        for(i=0;i+k-1<n;i++)
        {
            if(s[i]=='+') continue;
            else
            {
                invert(i);
                cnt++;
            }
            //cout << "i = " << i << "s = " << s << "\n";
        }
        cout << "Case #" << tc << ": ";
        if(count(s.begin(),s.end(),'+')==n) cout << cnt << "\n";
        else cout << "IMPOSSIBLE\n";
        tc++;
    }
    return 0;
}

