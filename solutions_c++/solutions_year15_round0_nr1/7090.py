#include <bits/stdc++.h>
using namespace std;
int main()
{
    freopen ( "a1.in","r",stdin);
    freopen ("aout.txt","w",stdout);
    int t;
    cin>>t;
    int cc=0;
    while(t--)
    {
        cc++;
        int n ;string s;
        cin>>n>>s;
        int ans = 0; int i,j;
        int flag = 0;
        for(i=0;i<s.length();i++)
        {
            char aa=s[i];
            int c = (int)aa - 48;
            if (flag > i)
                ans =ans + 0;
            else
            {ans =ans + (i - flag);flag = i ;}
            flag =flag + c;

        }
        cout<<"Case #"<<cc<<": "<<ans<<endl;
    }
}
