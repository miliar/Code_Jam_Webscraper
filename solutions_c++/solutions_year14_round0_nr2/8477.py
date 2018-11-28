#include<cstdio>
using namespace std;
int main()
{
    int i,j,k,t,cs=1;

   // freopen("C:\\Users\\Anunay\\Desktop\\input.txt","r",stdin);
 //   freopen("C:\\Users\\Anunay\\Desktop\\output.txt","w",stdout);
    double x,c,f,sum,rate,val,z,y;
    scanf("%d",&t);
    while(t--)
    {
        rate=2;
       // printf("%lf\n",rate);
        sum=0;
        scanf("%lf %lf %lf",&c,&f,&x);
        val=x/rate;
       // printf("\t%lf %lf\n",val,rate);
        z=c/rate;
        y=(x/(rate+f));
        while(val>z+y)
        {
       //     printf("here\n");
            sum+=z;
            rate+=f;
            z=c/rate;
            y=(x/(rate+f));
            val=x/rate;
        }
        sum+=val;
        printf("Case #%d: %.7lf\n",cs,sum);
        cs++;
    }
}
