#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t;
    cin>>t;
    for(int i=0;i<t;i++)
    {
        int n;
        char s[1010];
        cin>>n;
        cin>>s;
        int count=0;
        int in=s[0]-'0';
        for(int i=1;i<=n;i++)
        {
            if((s[i]-'0')>0)
            {
                if(in<i)
                {
                    count+=(i-in);
                    in=i+s[i]-'0';
                    cout<<count;
                }
                else
                {
                    in+=s[i]-'0';
                }
            }
        }
        cout<<"Case #"<<(i+1)<<": "<<count<<endl;
    }
    return 0;
}

