#include <stdio.h>
#include <algorithm>
using namespace std;

int main(void)
{
    int n,i,j,k;

    double c,f,x,s,t,temp,ans;

    FILE *in = fopen("input.txt","r");
    FILE *out = fopen("output.txt","w");

    fscanf(in,"%d",&n);

    for (k=1; k<=n; k++)
    {
            fscanf(in,"%lf %lf %lf",&c,&f,&x);

            s=2.0;
            t=0.0;
            ans=0.0;

            while (1)
            {
                    temp = c/s;
                    ans = x/s;
                    if (ans <= (x/(s+f)+temp))
                        break;

                    t += temp;
                    s += f;
            }

            ans+=t;
            fprintf(out,"Case #%d: %.7f\n",k,ans);
    }
}
