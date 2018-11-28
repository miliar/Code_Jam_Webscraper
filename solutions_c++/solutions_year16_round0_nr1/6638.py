#include<bits/stdc++.h>
using namespace std;
int main()
{
  //  freopen("A-large.in", "r", stdin);
   // freopen("o.txt", "w", stdout);

    unsigned long long t, n, i, j, tt, f0, f1, f2, f3, f4, f5, f6, f7, f8, f9, c, tmp, x, v;
    scanf("%llu", &t);
    for(tt=1; tt<=t; tt++)
    {
        f0=f1=f2=f3=f4=f5=f6=f7=f8=f9=c=0;
        v=1;
        scanf("%llu", &n);
        if(n==0)
            printf("Case #%llu: INSOMNIA\n", tt);
        else{
        while(1)
        {
            x = n*v;
            while(x!=0)
            {
                tmp = x%10;
                if(tmp==0 && f0==0)
                {
                    c++;
                    f0=1;
                }
                if(tmp==1 && f1==0)
                {
                    c++;
                    f1=1;
                }
                if(tmp==2 && f2==0)
                {
                    c++;
                    f2=1;
                }
                if(tmp==3 && f3==0)
                {
                    c++;
                    f3=1;
                }
                if(tmp==4 && f4==0)
                {
                    c++;
                    f4=1;
                }
                if(tmp==5 && f5==0)
                {
                    c++;
                    f5=1;
                }
                if(tmp==6 && f6==0)
                {
                    c++;
                    f6=1;
                }
                if(tmp==7 && f7==0)
                {
                    c++;
                    f7=1;
                }
                if(tmp==8 && f8==0)
                {
                    c++;
                    f8=1;
                }
                if(tmp==9 && f9==0)
                {
                    c++;
                    f9=1;
                }
                x/=10;
            }
            if(c==10)
                break;
            else
                v++;
        }
        printf("Case #%llu: %llu\n", tt, n*v);
        }

    }
    return 0;
}
