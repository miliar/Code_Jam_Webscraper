#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <string>
#include <sstream>
#include <cmath>
#include <algorithm>
#include <cstring>

using namespace std;

bool check(int a)
{
    int t,inva = 0;
    t = a;
    while(t)
    {
        inva *= 10;
        inva += t%10;
        t /= 10;
    }
    if (inva == a) return true;
    return false;
}

int main()
{
//    freopen("C-small-attempt0.in","r",stdin);
//    freopen("C-small-attempt0.out","w",stdout);
    bool is[1100];
    memset(is, false, sizeof(is));
    for (int i=1;i<=33;++i)
    {
        if (check(i) && check(i*i))
        {
            is[i*i] = true;
        }
    }

    int t,a,b;
    scanf("%d",&t);
    for (int cases=1;cases<=t;++cases)
    {
        int ans = 0;
        printf("Case #%d: ",cases);
        scanf("%d%d",&a,&b);
        for (int i=a;i<=b;++i) if(is[i]) ans++;
        printf("%d\n",ans);
    }
    return 0;
}
