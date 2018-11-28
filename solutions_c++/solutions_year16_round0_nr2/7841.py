#include<iostream>
#include<cstring>
#include<cstdio>
using namespace std;
int main()
{
    int t;
    char ch[1000];
    freopen("B-large.in","r",stdin);
    freopen("output22.out","w",stdout);
    cin>>t;
    for(int i=0;i<t;i++)
    {
        cin>>ch;
        int s=strlen(ch);
        int ans=0;
        for(int j=1;j<s;j++)
            if(ch[j]!=ch[j-1])
                ans++;
        if(ch[s-1]=='-')
            ans++;
        cout<<"Case #"<<i+1<<": "<<ans<<endl;
    }
    return 0;
}
