#include <cstdio>

using namespace std;

int main()
{

    int T;
    double C,F,X;
    scanf("%d",&T);

    int z;
    double temp,O,f;

    for (z=0;z<T;z++)
    {
        O=0.0;
        f=2.0;
        scanf("%lf%lf%lf",&C,&F,&X);
        temp=(C/f)+X/(F+f);
        while (temp<(X/f))
        {

            O+=(C/f);
            f+=F;
            temp=(C/f)+X/(F+f);
        }
        O+=(X/f);
        printf("Case #%d: %lf\n",z+1,O);
    }
    return 0;
}
