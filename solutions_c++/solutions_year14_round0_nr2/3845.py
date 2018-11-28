#include <iostream>
#include <stdio.h>

using namespace std;

int main()
{
    freopen("B-large.in","r",stdin);
     freopen("out.txt","w",stdout);

    int test,test_count=0;
    double incre,temp;
    double time,ans;
    scanf("%d",&test);
    while(test--)
    {
        test_count++;
        double c,f,x;
        scanf("%lf %lf %lf",&c,&f,&x);
        incre=2;
        ans=0.000;
        while(3)
        {
            temp=x/incre;
            time=c/incre;
            incre+=f;
            time+=x/incre;
            if(time<temp)
                ans+=c/(incre-f);
            else
                break;
        }
        ans+=x/(incre-f);
        printf("Case #%d: %.7lf\n",test_count,ans);
    }
    return 0;
}

