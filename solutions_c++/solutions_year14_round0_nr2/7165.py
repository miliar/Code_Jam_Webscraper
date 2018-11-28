#include<cstdio>
#include<iostream>
using namespace std;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    scanf("%d",&t);
    for(int test=1;test<=t;test++)
    {
        double c,f,x;
        scanf("%lf%lf%lf",&c,&f,&x);
      //  cout<<c<<" "<<f<<" "<<x<<endl;
        double rate=2.0,ans=0.0;

        double IndirectToGoal=0;
        double DirectToGoal=x/rate;


        double ToFarm=c/rate;
        rate+=f;
        IndirectToGoal=ToFarm+(x/rate);

       // cout<<DirectToGoal<<endl;
       // cout<<IndirectToGoal<<endl;
        while(IndirectToGoal < DirectToGoal)
        {
            DirectToGoal=IndirectToGoal;

            ToFarm+=(c/rate);
            rate+=f;
            IndirectToGoal=ToFarm+(x/rate);
        }
        printf("Case #%d: %.7lf\n",test,DirectToGoal);

    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
