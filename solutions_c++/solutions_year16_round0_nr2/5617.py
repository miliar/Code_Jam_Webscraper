#include<bits/stdc++.h>
using namespace std;
#define FOR(i,a,b) for(int i=a;i<=b;i++)
char s[150];
int best1[150],best2[150];
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    int T,l;
    cin>>T;
    getchar();
    int TT=0;
    while(T--)
    {TT++;
        gets(s);
        if(s[0]=='+')
        {
            best1[0]=0;best2[0]=1;
        }
        else
        {
            best2[0]=0;best1[0]=1;
        }
        l=strlen(s);
        FOR(i,1,l-1)
        {
            if(s[i]=='+')
            {
                best1[i]=best1[i-1];
                best2[i]=best1[i-1]+1;
            }
            else
            {
                best1[i]=best2[i-1]+1;
                best2[i]=best2[i-1];
            }
        }
        printf("Case #%d: %d\n",TT,best1[l-1]);
    }
    return 0;
}
