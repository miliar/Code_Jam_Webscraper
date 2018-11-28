#include <cstdio>
#include <cstring>
#include <iostream>
using namespace std;
const int maxn=110;
char str[maxn];
int main()
{
    int T,cas=1;
    scanf("%d",&T);
    while(T--)
    {
        printf("Case #%d: ",cas++);
        scanf("%s",str);
        int ans=0,n=strlen(str);
        str[n]=1,str[n+1]=0;
        for(int i=1;str[i];i++)
            if(str[i]!=str[i-1])
                ++ans;
        if(str[n-1]=='+')    --ans;
        printf("%d\n",ans);
    }
    return 0;
}
