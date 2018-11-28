#include <iostream>
#include <algorithm>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <queue>
#include <cmath>
#include <stack>
#include <map>

#pragma comment(linker, "/STACK:1024000000");
#define EPS (1e-8)
#define LL long long
#define ULL unsigned long long LL
#define _LL __int64
#define _INF 0x3f3f3f3f
#define Mod 1000000007
#define LM(a,b) (((ULL)(a))<<(b))
#define RM(a,b) (((ULL)(a))>>(b))

using namespace std;

char s1[110],s2[110];

int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);

    int T,icase = 1;

    int ans;

    scanf("%d",&T);
    int n,i,j;
    while(T--)
    {
        scanf("%d",&n);

        scanf("%s",s1);
        scanf("%s",s2);

        ans = 0;

        int l1 = strlen(s1);
        int l2 = strlen(s2);

        printf("Case #%d: ",icase++);

        if(l1 > l2)
        {
            swap(s1,s2);
        }

        i = 0,j = 0;
        int pi,pj;
        while(s1[i] != '\0' && s2[j] != '\0')
        {
            pi = i;
            if(i)
                ++i;
            for(;s1[i] != '\0'; ++i)
            {
                if(i != 0 && s1[i] != s1[i-1])
                    break;
            }

            pj = j;
            if(j)
                ++j;
            for(;s2[j] != '\0'; ++j)
            {
                if(j != 0 && s2[j] != s2[j-1])
                    break;
            }

            if(s1[pi] != s2[pj])
            {
                ans = -1;
                break;
            }
            else
            {
                ans += abs((j-pj+1)-(i-pi+1));
            }
        }

        if(ans == -1 || s1[i] != '\0' || s2[j] != '\0')
        {
            printf("Fegla Won\n");
        }
        else
        {
            printf("%d\n",ans);
        }

    }
    return 0;
}



