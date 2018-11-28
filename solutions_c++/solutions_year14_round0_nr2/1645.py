#include <cstdio>
#include <iostream>

using namespace std;

int casos;
double c, f, x, v, res, paso;


int main()
{
    freopen("venga.in","r",stdin);
    freopen("res.txt","w",stdout);
    scanf("%d",&casos);
    for(int i=1; i<=casos; i++){
        scanf("%lf%lf%lf",&c,&f,&x);
        v=2;
        res=50001;
        paso=0;
        for(int e=0; e<=100002; e++){
            if(paso+x/v<res)
                res=paso+x/v;
            paso=paso+c/v;
            v=v+f;
        }
        printf("Case #%d: %.7lf\n",i,res);
    }
    return 0;
}
