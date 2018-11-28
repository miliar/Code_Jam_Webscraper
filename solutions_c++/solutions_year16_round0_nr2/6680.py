#include<bits/stdc++.h>
using namespace std;
int main()
{
    //freopen("input.txt","r",stdin);
    //freopen("output.txt","w",stdout);
    int t;
    cin>>t;
    for (int i=1;i<=t;i++)
    {
        int cnt = 1;
        char s[102];
        cin>>s;
        int j;
        for (j=1;s[j]!='\0';j++)
        {
            if (s[j]!=s[j-1])
                cnt++;
        }
        if (s[j-1]=='+')
            cnt--;
        cout<<"Case #"<<i<<": "<<cnt<<"\n";
    }
    return 0;
}
