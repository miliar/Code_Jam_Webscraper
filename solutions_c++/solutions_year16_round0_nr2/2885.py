#include <bits/stdc++.h>
using namespace std;
char a[105];
int len,T;
int calc()
{
    int ans=0;
    a[len]='+';
    for(int i=len-1;i>=0;--i)
        ans+=(a[i]!=a[i+1]);
    return ans;
}
int main()
{
    scanf("%d",&T);
    for(int t=1;t<=T;++t)
    {
        printf("Case #%d: ",t);
        scanf(" %s",a);
        puts(a);
        len=strlen(a);
        printf("%d\n",calc());
    }
    return 0;
}
