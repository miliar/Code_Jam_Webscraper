#include <iostream>

using namespace std;
void solve()
{
        for (i=1; i<=n; i++)
            scanf("%lf%lf",&d[i].x,&d[i].y);
        srand((unsigned)time(0));
        p=12;
        l=10;
        for (i=1; i<=p; i++)
        {
            s[i].x=(rand()%101)/100.0*x;
            s[i].y=(rand()%101)/100.0*y;
            temp=maxn;
            for (j=1; j<=n; j++)
            {
                if (sqrt((s[i].x-d[j].x)*(s[i].x-d[j].x)+(s[i].y-d[j].y)*(s[i].y-d[j].y))<temp)
                    temp=sqrt((s[i].x-d[j].x)*(s[i].x-d[j].x)+(s[i].y-d[j].y)*(s[i].y-d[j].y));
            }
            data[i]=temp;
        }
        T_min=x+y;
        while (T_min>det+lim)
        {
            for (i=1; i<=p; i++)
            {
                j=0;
                ang=(rand()/(double)(RAND_MAX))*(6.2832)-3.1416;
                len=(rand()%101/100.0)*T_min;
                xd=len*cos(ang);
                yd=len*sin(ang);
                while (j<l)
                {
                    j++;
                    xt=s[i].x+xd;
                    yt=s[i].y+yd;
                    if (xt<(0-lim)||xt>(x+lim)||yt<(0-lim)||yt>(y+lim)) continue;
                    temp=maxn;
                    for (k=1; k<=n; k++)
                    {
                        if (sqrt((xt-d[k].x)*(xt-d[k].x)+(yt-d[k].y)*(yt-d[k].y))<temp)
                            temp=sqrt((xt-d[k].x)*(xt-d[k].x)+(yt-d[k].y)*(yt-d[k].y));
                    }
                    if (temp>data[i]||((rand()/(double)(RAND_MAX))<c*exp((temp-data[i])/T_min)))
                    {
                        s[i].x=xt;
                        s[i].y=yt;
                        data[i]=temp;
                        j=0;
                    }
                    else
                    {
                        ang=(rand()/(double)(RAND_MAX))*(6.2832)-3.1416;
                        len=(rand()%101/100.0)*T_min;
                        xd=len*cos(ang);
                        yd=len*sin(ang);
                    }
                }
            }
            T_min*=0.9;
        }
        double ans=data[1];
        int flag=1;
        for (i=1; i<=p; i++)
            if (data[i]>ans)
            {
                ans=data[i];
                flag=i;
            }
        printf("The safest point is (%.1f, %.1f).\n",s[flag].x,s[flag].y);

}
int main()
{
    scanf("%d", &T);
    for (int cas = 1; cas <= T; ++cas)
    {
        scanf("%d%lf%lf", &n, &v, &x);
        for (int i = 1; i <= n; ++i)
        {
            scanf("%lf%lf", &r[i], &c[i]);
        }
        solve();
        printf("Case #%d: %.7f\n", cas, ans);
    }
    return 0;
}
