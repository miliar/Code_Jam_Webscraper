#include<bits/stdc++.h>
using namespace std;


int main()
{
    //freopen("B-large.in", "r", stdin);
    //freopen("outb.txt", "w", stdout);

    int t, len, tc,i;
    char s[105];

    cin>> t;
    for(tc=1; tc<=t; tc++)
    {
        cin>>s;
        len= strlen(s);
        bool bp=1;
        int cnt=0;
        if(s[0]=='-') bp=0;
        for(i=1; i<len; i++)
        {
            if(s[i]=='+' && bp==0)
            {
                bp=1;
                cnt++;
            }
            else if(s[i]=='-'&& bp==1)
            {
                bp=0;
                cnt++;
            }
        }
        if(bp==0) cnt++;

        printf("Case #%d: %d\n",tc,cnt);
    }
    return 0;
}
