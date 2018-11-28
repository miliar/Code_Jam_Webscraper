#include <cstdio>

double c,f,x, speed[110000], time[110000];

int main()
{
    freopen("in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int T;
    scanf("%d",&T);

    for(int cas = 1; cas <= T; cas ++)
    {

        scanf("%lf%lf%lf", &c, &f, &x);
        double bound = 100000.0 ;
        for(int i=0;i<=bound; i++)
        {
            speed[i] = 2 + i * f;
        }
        time[0] = 0;
        double ans = x/2;
        for(int i=1;i<=bound;i++)
        {
            time[i] = time[i-1] + c / speed[i-1];
            //printf("time: %lf\n", time[i]);
            double tmp = time[i] + x / speed[i];
            //printf("tmp:%lf\n", tmp);
            if(tmp < ans)
            {
                ans = tmp;
                //printf("number : %d\n", i);
                //getchar();
            }
        }
        printf("Case #%d: %.7lf\n", cas, ans);
    }
    return 0;
}
