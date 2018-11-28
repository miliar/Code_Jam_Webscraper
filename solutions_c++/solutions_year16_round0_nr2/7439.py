#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
string flip(string s,int n)
{
    for(int i=0;i<n+1;i++)
    {
        if(s[i]=='-')
            s[i]='+';
        else
            s[i]='-';
    }
    return s;
}

int main() {

    freopen("B-large.in","r",stdin);
    freopen("CJ16-02.out","w",stdout);
    int t,j,i,n,ans;
    string s;
    cin>>t;
    for(i=1;i<=t;i++)
    {
        ans=0;
        cin>>s;
        for(j=s.length()-1;j>=0;j--)
        {
            if(s[j]=='-')
            {
                ans++;
                s=flip(s,j);
            }
            //cout<<s<<endl;
        }
        cout<<"Case #"<<i<<": "<<ans<<endl;
    }
    return 0;
}

