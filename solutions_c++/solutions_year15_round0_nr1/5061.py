#include<iostream>
#include<string>
#include<stdio.h>
#include<stdlib.h>
using namespace std;

int main()
{
    int tc,caseno=1;
    freopen("in.in","r",stdin);
    freopen("out","w",stdout);
    cin>>tc;
    while(caseno<=tc)
    {
        string s;
        int smax;
        cin>>smax;
        cin>>s;
        int cnt=0,need=0;
        for(int i=0;i<=smax;i++)
        {
            if(cnt>=i)
            {
                cnt+=s[i]-'0';
            }
            else
            {
                need+=(i-cnt);
                cnt+=(s[i]-'0'+i-cnt);
            }

        }
        printf("Case #%d: %d\n",caseno,need);
        caseno++;
    }
}
