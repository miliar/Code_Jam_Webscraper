#include<cstdio>
#include<cstring>
#include<algorithm>
#include<iostream>
#include<map>
#define nn 1100
using namespace std;
string s;
int main()
{
    freopen("Ain.txt","r",stdin);
    freopen("Aout.txt","w",stdout);
    int i,t;
    scanf("%d",&t);
    int cas=1;
    int smax;
    while(t--)
    {
        scanf("%d",&smax);
        int ans=0;
        int ix=0;
        cin>>s;
        for(i=0;i<=smax;i++)
        {
            if(ix>=i)
            {
                ix+=s[i]-'0';
            }
            else
            {
                ans+=i-ix;
                ix=i+s[i]-'0';
            }
        }
        printf("Case #%d: %d\n",cas++,ans);
    }
    return 0;
}
