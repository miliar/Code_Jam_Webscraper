#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstring>
#include <algorithm>
#include <fstream>

using namespace std;

string s;
int t,ans,fr,len;

int main()
{
    scanf("%d",&t);
    ofstream fp("B.out");
    int cnt=0;
    while(t--)
    {
        cin>>s;
        fr=true;
        len=s.size();
        ans=0;
        for (int i=0;i<=len;++i)
        {
            if(s[i]=='+') fr=false;
            while(s[i]==s[i+1]) ++i;
            if (s[i]=='-')
            {
                if (fr) ans+=1;
                else ans+=2;
            }
        }
        fp<<"Case #"<<++cnt<<": "<<ans<<endl;
    }
    return 0;
}
