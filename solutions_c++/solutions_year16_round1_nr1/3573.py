#include<bits/stdc++.h>
using namespace std;
string str;

string func(int len)
{
    if(len==0)
        return "";

    string ans,ans1,ans2;
    int i,m;

    m=0;
    for(i=0; i<len; i++)
        m=max(m,str[i]-64);

    i=0;
    while(i<len && (str[i]-64<m))
        i++;

    ans="";
    ans1="";
    ans2=func(i);

    for(; i<len; i++)
    {
        if(str[i]-64==m)
            ans.push_back(str[i]);
        else
            ans1.push_back(str[i]);
    }

    ans= ans+ans2;
    ans=ans+ ans1;
    return ans;
}

int t,X,len;
string ans;
int main()
{
    freopen("inp.txt","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&t);
    while(t--)
    {
        X++;
        printf("Case #%d: ",X);
        cin>>str;
        len=str.length();
        ans=func(len);
        cout<<ans<<"\n";
    }
    return 0;
}
