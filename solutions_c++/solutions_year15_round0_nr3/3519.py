#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t;
    cin>>t;
    for(int T=1;T<=t;T++)
    {
        int shy,friend_req=0,shy_ctr=0;
        cin>>shy;
        string s;
        cin>>s;
        int i;
        shy_ctr+=s[0]-'0';
        for(i=1;i<s.size();i++)
        {
            if(shy_ctr>=i)
                shy_ctr+=s[i]-'0';
            else if(shy_ctr<i&&s[i]-'0'!=0)
            {
                friend_req+=(i-shy_ctr);
                shy_ctr+=s[i]-'0';
                shy_ctr+=friend_req;
            }
        }
        printf("Case #%d: %d\n",T, friend_req);
    }
    return 0;
}
