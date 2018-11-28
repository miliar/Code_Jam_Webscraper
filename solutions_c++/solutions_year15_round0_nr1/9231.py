#include<bits/stdc++.h>
using namespace std;

string str;
int main()
{
    int t,n,sz,ans,now;
    cin>>t;
    for(int z =1;z<=t;z++)
    {
        cin>>sz>>str;
        ans = 0;
        now = 0;
        for (int i=0;i<=sz;i++)
        {
            if (now < i)
            {
                ans += (i-now);
                now = i;
            }
            now += (str[i] - '0');
        }
        cout<<"Case #"<<z<<": "<<ans<<endl;
    }
}
