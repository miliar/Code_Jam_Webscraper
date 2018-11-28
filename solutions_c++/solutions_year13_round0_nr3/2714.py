#include <stdio.h>
#include <string.h>
#include <iostream>

using namespace std;

bool huiwen(int x)
{
    char tmp[10];
    sprintf(tmp,"%d",x);
    int len = strlen(tmp);
    for(int i=0;i<len/2;i++)
        if(tmp[i] != tmp[len-1-i])
            return false;
    //puts(tmp);
    return true;
}

int cnt(int x)
{
    int ans = 0;
    for(int i=1;i*i<=x;i++)
        if(huiwen(i) && huiwen(i*i))
            ++ans;
    return ans;
}

int main()
{
//    freopen("C0.in","r",stdin);
//    freopen("C0.txt","w",stdout);
    int T,ncase = 0;
    scanf("%d",&T);
    while(T--)
    {
        int a,b;
        scanf("%d%d",&a,&b);
        printf("Case #%d: %d\n",++ncase,cnt(b)-cnt(a-1));
    }
    return 0;
}
