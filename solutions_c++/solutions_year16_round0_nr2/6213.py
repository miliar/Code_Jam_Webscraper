#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t;
    cin>>t;
    for(int i=1;i<=t;++i)
    {
        char s[101];
        cin>>s;
        int x=0,j;
        for(j=1;s[j]!=0;j++)
        {
            if(s[j]!=s[j-1])
            {
                x++;
            }
        }
        if(s[j-1]=='-')
        {
            x++;
        }
        cout<<"Case #"<<i<<": "<<x<<endl;
    }
}
