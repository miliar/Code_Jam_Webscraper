#include<bits/stdc++.h>
#define ll long long
using namespace std;
int main()
{

    freopen("A-large.in", "r", stdin); // redirects standard input
    freopen("output.txt", "w", stdout); // redirects standard output

    int t;
    cin>>t;

    string s;
    int k;

    for(int cs=1;cs<=t;cs++)
    {
        cin>>s>>k;

        int cnt=0;

        for(int i=0;i<=s.size()-k;i++)
        {
            if(s[i]=='-')
            {
                cnt++;
                for(int j=i;j<=i+k-1;j++)
                    s[j]=(s[j]=='+')?'-':'+';
            }
        }

        bool ans=1;
        for(int i=0;i<s.size();i++)
            if(s[i]=='-')ans=0;


        cout<<"Case #"<<cs<<":"<<" ";

        if(ans)
            cout<<cnt<<"\n";
        else
            cout<<"IMPOSSIBLE\n";
    }

}
