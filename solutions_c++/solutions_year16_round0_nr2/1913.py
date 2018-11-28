#include<bits/stdc++.h>
using namespace std;

int main()
{
    int t,it;
    cin>>t;
    string s;
    for(it=1;it<=t;it++)
    {
        cin>>s;
        int len=s.size(),sign=s[0],ans=0,i=0;;
        while(i<len)
        {
            if(sign!=s[i])
            {
                ans++;
                sign=s[i];
            }
            i++;
        }
        if(sign=='-')
            ans++;
        cout<<"Case #"<<it<<": "<<ans<<endl;
    }
    return 0;
}
