#include<cstdio>
int flag = 0;
int main()
{
    int i, j, tn, n;
    freopen("gca.in", "r", stdin);
    freopen("gca.out", "w", stdout);
    scanf("%d",&tn);
    for(int tt = 1;tt<=tn;tt++){
        scanf("%d",&n);
        printf("Case #%d: ", tt);
        if(n == 0)
        {
            printf("INSOMNIA\n");
            continue;
        }
        int now = 0;
        flag = 0;
        while(flag != (1<<10) - 1){
            now += n;
            int a = now;
            while(a){
                int last = a%10;
                flag |= (1<<last);
                a/=10;
            }
        }
        printf("%d\n", now);
    }
    return 0;
}
