#include <cstdio>
#include <vector>
#include <cstring>
using namespace std;
#define pb push_back
#define clr(a) memset(a,0,sizeof(a))
int main()
{
    int t, fre[17], n, x, cnt, ans;
    scanf("%d",&t);
    for(int i = 1; i <= t; i++)
    {
        clr(fre);
        for(int l = 0; l < 2; l++)
        {
            scanf("%d", &n);
            for(int j = 1; j <= 4; j++)
            {
                for(int k = 0; k < 4; k++)
                {
                    scanf("%d", &x);
                    if(j == n)
                        fre[x]++;
                }
            }
        }
        cnt = 0;
        ans = 0;
        for(int j = 0; j < 17;j++)
        {
            if(fre[j] > 1)
            {
                ans = j;
                cnt++;
            }
        }
        printf("Case #%d: ", i);
        if(cnt == 1)
            printf("%d\n", ans);
        else if(cnt == 0)
           printf("Volunteer cheated!\n");
        else
            printf("Bad magician!\n");


    }
    return 0;
}
