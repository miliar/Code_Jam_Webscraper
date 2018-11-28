#include<bits/stdc++.h>
using namespace std;
string s;
int main()
{
    freopen("B.in", "r", stdin);
    freopen("B.out", "w", stdout);
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int t;
    cin>>t;
    for(int c=1; c<=t; c++)
    {
        cin>>s;
        int len=s.size();
        int re=0;
        for(int i=1;i<len;i++)
        {
            if(s[i-1]!=s[i])re++;
        }
        if(s[len-1]=='-')re++;
        cout<<"Case #"<<c<<": "<<re<<endl;
    }
    return 0;
}
