#include<cstdio>
int main()
{
    //freopen("B_large.txt","r",stdin);
   // freopen("B_large_out.txt","w",stdout);
    int t,co=0;
    double c,f,x,total,tamp,tamp1,div;
    scanf("%d",&t);
    while(t--)
    {
      scanf("%lf %lf %lf",&c,&f,&x);
      total=0.0;
      tamp=(c/2.0)+(x/(2.0+f));
      tamp1=x/2.0;
      div=2.0;
      while(tamp<tamp1)
      {
        total+=c/div;
        div=div+f;
        tamp=(c/div)+(x/(div+f));
        tamp1=x/div;

      }
      total+=tamp1;
      printf("Case #%d: %.7lf\n",++co,total);
    }
    return 0;
}

