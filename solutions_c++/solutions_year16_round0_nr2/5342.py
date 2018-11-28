#include <bits/stdc++.h>
using namespace std;
#define L long long
int main()
{
    L t,n;
    cin>>t;
    for(int I=1;I<=t;I++)
    {
        string s;
        string r;
        int res=0;
        cin>>s;
        int n=s.length();
        bool f=1;
        while(f)
        {
            f=0;
            for(int i=n-1;i>=0;i--)
            {
                if(s[i]=='-')
                {
                    for(int j=0;j<=i;j++)
                    {
                        if(s[j]=='+')
                            s[j]='-';
                        else
                            s[j]='+';
                    }
                    res++;
                    f=1;
                    break;
                }
            }
        }
        cout<<"Case #"<<I<<": "<<res<<"\n";
    }
    return 0;
}
