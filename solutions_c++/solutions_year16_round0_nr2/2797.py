#include<iostream>
#include<stdio.h>
#include<cstring>
using namespace std;
const int maxn=1000;
char s[maxn];
void work()
{
        scanf("%s",s);
        int ans=1;
        for (int i=1;s[i]!=0;i++)
                if (s[i]!=s[i-1]) ans++;
        if (s[strlen(s)-1]=='+') ans--;
        cout<<ans<<endl;
}
int main()
{
        int T,cas=0;
        scanf("%d",&T);
        while (T--)
        {
                printf("Case #%d: ",++cas);
                work();
        }
}
