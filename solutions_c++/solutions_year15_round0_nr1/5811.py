#include <bits/stdc++.h>
#include <fstream>
#define ll long long
using namespace std;
int t,n;
string s,ans[105];
int main()
{
    fstream fin("A-large.in",ios::in);
    fstream fot("out.txt",ios::out);
    fin>>t;
    for(int j=1;j<=t;j++)
    {
        fin>>n>>s;
        n+=1;
        int c=s[0]-'0';
        int tot=0;
        for(int i=1;i<n;i++)
        {
            if(c<i)
                c=i+int(s[i]-'0');
            else
                c+=int(s[i]-'0');
        }
        for(int i=0;i<n;i++)
            tot+=s[i]-'0';
        fot<<"Case #"<<j<<": "<<c-tot<<endl;
    }
}
