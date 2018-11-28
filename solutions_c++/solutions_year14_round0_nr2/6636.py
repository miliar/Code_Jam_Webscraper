#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include<algorithm>
using namespace std;

int t;
double c, f, x;



int main()
{
    freopen("B--large.in","r",stdin);
    freopen("B--large_out.txt","w",stdout);
    
    int i,j;
    scanf("%d",&t);
    
    for(int tt = 1; tt <= t; tt++)
    {
        printf("Case #%d: ", tt);
        double total = 0.0;
        double speed = 2.0;
        scanf("%lf %lf %lf", &c, &f, &x);
        while((x/(speed+f)) < ((x-c)/speed))
        {
            total += c/speed;
            speed += f;
        }
        total += x/speed;
        printf("%.7lf\n", total);
    }
    //system("pause");
    return 0;
}
