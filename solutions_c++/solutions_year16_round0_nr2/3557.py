#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    cin>>t;
    for(int test=1;test<=t;test++)
    {
    string s;
    cin>>s;
    int sum=0;
    for(int i=1;i<s.size();i++)
    {
        if(s[i]!=s[i-1])
            sum++;
    }
    if(s[s.size()-1]=='-')
        sum++;
    printf("Case #%d: %d\n",test,sum);
    }
    return 0;
}
