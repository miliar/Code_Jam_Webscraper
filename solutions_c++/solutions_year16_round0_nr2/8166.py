#include <iostream>
#include<cstdio>
#include<cstring>
using namespace std;
int t;
char st[1000];
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d",&t);
    for(int tid=1;tid<=t;tid++)
    {
        scanf("%s",st);
        int len=strlen(st);
        st[len]='+';
        int ans=0;
        for(int i=0;i<len;i++)
            if(st[i]!=st[i+1]) ans++;
        printf("Case #%d: %d\n",tid,ans);
    }
    return 0;
}
