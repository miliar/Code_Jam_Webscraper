#include <cstdio>
#include <cstdlib>
int main()
{
    int a;
    double C,F,X;
    double CPS,timet;
    freopen("A:\\B-large.in", "r", stdin);
    freopen("A:\\output.txt", "w", stdout);
    scanf("%d", &a);
    for(int i=0; i<a; i++){
        scanf("%lf%lf%lf",&C,&F,&X);
        CPS = 2.0;
        timet = 0;
        while(1){
            if ((X / CPS) > ((X) / (CPS + F) + (C / CPS))){
                timet += C / CPS;
                CPS += F;
            } else {
                timet += X / CPS;
                break;
            }
        }

        printf("Case #%d: %.7lf\n", i+1, timet);
    }
}
