#include<bits/stdc++.h>
using namespace std;

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t, c;
    string s;
    cin>>t;
    for(int j = 1; j <= t; j++)
    {
        cin>>s;
        c = 0;
        for(int i = 0; i < s.length() - 1; i++)
        {
            if(s[i] != s[i+1]) c++;
        }
        if(s[s.length()-1] == '-') c++;
        cout<<"Case #"<<j<<": "<<c<<endl;
    }
    return 0;
}
