#include<cstdio>
#include<cstring>

using namespace std ;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int _ , ca = 1 ;
    int i , j , k ;
    double c,f,x,ini,ff,n,ans;
    scanf ("%d",&_);
    while(_--)
    {
        scanf ("%lf%lf%lf",&c,&f,&x);
        printf("Case #%d: ",ca++);
        if (x<=c)
        {
            printf("%lf\n",x/2);
            continue ;
        }
        ff = x / 2 ;
        ans = ff ;
        n = 0 ;
        for ( ini=2; n < ff ;)
        {
            n += c/ini ;
            ini += f ;
            if ( n + x/ini < ans)
                ans= n+x/ini ;
            else break ;
            //printf("%lf\n",n);
        }
        printf("%.7lf\n",ans);
    }
    return 0 ;
}
