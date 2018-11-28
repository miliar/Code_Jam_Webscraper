#include <cstdio>
#include <cstring>
#include <algorithm>
#include <iostream>
#include <ctime>
#include <cmath>
using namespace std;
char s[102];
int n;
int ans;
int T;
int main()
{
//    freopen("B.in","r",stdin);
//    freopen("B.out","w",stdout);
    
    scanf("%d",&T);
    for(int i=1;i<=T;++i)
    {
        memset(s,0,sizeof(s));
        scanf("%s",s);
        char last_t = '&';
        int ans = 0;
        for(int j=0;j<strlen(s);++j)
        {
            if(s[j]!=last_t)
            {
                ++ans;
                last_t = s[j];
            }
        }
        if(last_t == '+')--ans;
        printf("Case #%d: %d\n",i,ans);
    }
    return 0;
}