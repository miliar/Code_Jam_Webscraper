#include <stdio.h>

main(){

int T;
double c, f, x;
double ing, time, oldtime, postime;

scanf("%d", &T);
for(int caso=1;caso<=T;caso++)
{
    scanf("%lf %lf %lf", &c, &f, &x);
    ing = 2.0;
    time = 0.0;
    postime = x;
    do
    {
        oldtime = postime;
        postime = time + x/ing;
        time += c/ing;
        ing += f;
    }
    while( oldtime > postime );
    printf("Case #%d: %.7lf\n", caso, oldtime);
}

return 0;
}

