#include <bits/stdc++.h>
#define _ ios_base::sync_with_stdio(0);cin.tie(0);
using namespace std;

int T, cases, smax, frnds, sCount;
char a[1500];

int digi(char c)
{
    return c-48;
}

int main(){
    //freopen("A-large.in","r",stdin);
    //freopen("A-large.out","w",stdout);
    scanf("%d", &T);
    while(T--)
    {
        scanf("%d", &smax);
        scanf("%s", a);

        sCount = digi(a[0]);
        frnds = 0;

        for(int i = 1; i<= smax; i++)
        {
            int tmp = 0;
            if(i > sCount)
                tmp += i - sCount;

            frnds += tmp;

            sCount += digi(a[i]) + tmp;
        }

        printf("Case #%d: %d\n", ++cases, frnds);
    }
    return 0;
}
