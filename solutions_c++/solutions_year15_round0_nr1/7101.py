#include <cstdio>
#include <cstring>
#include <algorithm>
#include<string>
#include<iostream>

using namespace std;


int main()
{

    int T;
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    cin>>T;
    for (int _=1;_<=T;_++)
    {
        int n;
        cin>>n;
        string s;
        cin>>s;
        int ans=0;
        int k=s[0]-'0';
        for (int i=1;i<s.length();i++)
        {
            int tmp=s[i]-'0';
            if (i>k)
            {
                ans+=i-k;
                k+=i-k;
            }
            k+=tmp;
        }
        printf("Case #%d: %d\n",_,ans);
    }
    return 0;
}

