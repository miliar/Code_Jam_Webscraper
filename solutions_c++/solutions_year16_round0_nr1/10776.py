#include <cstdio>
#include <cstring>
#include <cstdlib>

int main()
{
    int n;

    //freopen("D:\\ClionProjects\\msprogramming2015\\input.txt", "r", stdin);
    //freopen("D:\\ClionProjects\\msprogramming2015\\output.txt", "w", stdout);
    scanf("%d", &n);
    for(int cur=1; cur<=n; cur++)
    {
        int sheeps;
        scanf("%d", &sheeps);

        if(sheeps == 0)
        {
            printf("Case #%d: INSOMNIA\n", cur);
            continue;
        }

        int a[10];
        memset(a, 0, sizeof(a));
        int ans = sheeps;
        while(1)
        {
            int dsheeps = ans;
            while(dsheeps > 0)
            {
                a[dsheeps%10] = 1;
                dsheeps /= 10;
            }
            bool flag = true;
            for(int i=0; i<=9; i++)
            {
                if(a[i] == 0 )
                {
                    flag = false;
                    break;
                }
            }
            if(flag)
            {
                break;
            }
            ans += sheeps;
        }
        printf("Case #%d: %d\n", cur, ans);
    }

    //fclose(stdin);
    //fclose(stdout);

    return 0;
}