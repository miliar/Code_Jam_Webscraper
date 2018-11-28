/**
**/
/**
Author : Sabariram
**/
#include <iostream>
#include<cstring>
using namespace std;

#define localTest 1
#define ll long long
#define MEMSET(a,v)  memset(a,v,sizeof(a))
#if localTest
#include<string.h>
#endif // localTest

int main()
{
    freopen("lain","r",stdin);
    freopen("laout","w",stdout);
    int tc,s,temp,ans = 0;
    string c;
    cin>>tc;
    for(int i=1;i<=tc;i++)
    {
        cout<<"Case #"<<i<<": ";
        cin>>s;
        cin>>c;
        ans = 0;
        if(s>0)
        {
            temp = c[0]-'0';
            int l;
            for(int j=1;j<=s;j++)
            {
                l = temp+ans;
                if(l<j)
                    ans += j-l;
                temp += c[j]-'0';
            }
        }
        cout<<ans<<endl;
    }
    return 0;
}
