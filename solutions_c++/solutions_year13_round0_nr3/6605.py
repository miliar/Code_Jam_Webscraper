#include <iostream>
#include <cstring>
#include <string>
#include <cstdio>
# define in(var1) scanf("%d",&var1)
using namespace std;
int main()
{
    int T,var1,var2;
    in(T);
    int cas=1;
    while(T--)
    {
        in(var1);
        in(var2);
        int ans=0;
        if(var1==1)
        ans++;
        if(var1<=4 && var2>=4)
        ans++;
        if(var1<=9 && var2>=9)
        ans++;
        if(var1<=121 && var2>=121)
        ans++;
        if(var1<=484 && var2>=484)
        ans++;
        printf("Case #%d: %d\n",cas++,ans);
    }
    return 0;
}
