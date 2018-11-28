#include <cstdlib>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <string>
#include <queue>

using namespace std;
int T;
int tab[101];

bool pal(int nb)
{
    int k = 0;
    while(nb>0)
    {
        tab[k++]=nb%10;
        nb/=10;
    }

    for(int i = 0; i <= k/2; i++)
        if(tab[i]!=tab[k-i-1]) return false;
    return true;
}

int main()
{
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("C-small-attempt0.out", "w", stdout);

    scanf("%d", &T);

    for(int t = 0; t < T; t++)
    {
        int a,b;
        scanf("%d%d", &a,&b);
        int tt=0;

        for(int i = 1; i <= b; i++)
        {
            if(i*i >= a && i*i <= b && pal(i) && pal(i*i))
               tt++;
        }

        printf("Case #%d: %d\n", t+1, tt);
    }

    return 0;
}
