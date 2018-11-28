#include<cstdio>
#include<string>
#include<iostream>
using namespace std;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out.out","w",stdout);
    int T;
    cin>>T;
    for(int t=0; t<T; t++)
    {
        int n;
        string s;
        int sump=0;
        int ans=0;
        cin>>n>>s;
        for(int i=0; i<=n; i++)
        {
            int shyp=s[i]-'0';
            if(shyp!=0)
            {
                if(i<=sump)
                    sump+=shyp;
                else if(i>sump)
                {
                    ans+=i-sump;
                    sump=i+shyp;
                }
            }

        }
        printf("Case #%d: %d\n",t+1,ans);
    }
    return 0;
}
