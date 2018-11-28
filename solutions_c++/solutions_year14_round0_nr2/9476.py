#include<cstdio>
#include<vector>
#include<cstdlib>
using namespace std;

int main()
{
    double c,f,x,ans,per;
    int t,tcase=1;
    //freopen("in.txt","r",stdin);
    //freopen("Osman.out","w",stdout);
    scanf("%d",&t);
    while(t--)
    {
        scanf("%lf %lf %lf",&c,&f,&x);
        ans=0.0;
        per=2.0;
        while((x/per)>((c/per)+(x/(per+f))))
        {
           ans+=(c/per);
           per+=f;
           //printf("%lf %lf %lf\n",x/per,(c/per),(x/(per+f)));
           //system("pause");
        }
        ans+=(x/per);
        printf("Case #%d: %0.7lf\n",tcase++,ans);
    }
    return 0;
}
