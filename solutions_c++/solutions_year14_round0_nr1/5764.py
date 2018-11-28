#include <iostream>
#include <cstdio>
using namespace std;
int a[20];
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int t;
    cin >> t;
    for(int cases = 1; cases <= t; cases++)
    {
        printf("Case #%d: ", cases);
        int n;
        scanf("%d", &n);
        for(int i = 1; i <= 4; i++)
        {
            for(int j = 1; j <= 4; j++)
                if(i == n)scanf("%d", &a[j]);
                else scanf("%*d");
        }
        scanf("%d", &n);
        int ans = 0, anss;
        for(int i = 1; i <= 4; i++)
        {
            int t;
            for(int j = 1; j <= 4; j++)
                if(i == n)
                {
                    scanf("%d", &t);
                    for(int j = 1; j <= 4; j++)
                        if(a[j] == t)
                        {
                            ans++;
                            anss = t;
                        }
                }
                else scanf("%*d");
        }
        if(ans == 0) puts("Volunteer cheated!");
        else if(ans > 1) puts("Bad magician!");
        else printf("%d\n", anss);
    }
    return 0;
}
