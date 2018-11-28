#include <iostream>
#include<fstream>
#define READ(s) freopen(s, "r", stdin)
#define WRITE(s) freopen(s, "w", stdout)
using namespace std;

int main()
{
    READ("B-large.in");
    WRITE("B-large.out");
    int t;
    cin>>t;
    for(int i=0; i<t; i++)
    {
        double c,f,x,n1=0;
        double finl=0;
        cin>>c>>f>>x;
        while(1)
        {
            if(x<=c)
            {
                finl=x/2;
                break;
            }
            if((double)(c/(2+(n1*f)))+ (x/(2+((n1+1)*f))) < (double)x/(2+((n1)*f)))
            {
                finl+=(double) c/(2+(n1*f));
                n1++;
            }
            else
            {
                finl+=(double) x/(2+(n1*f));
                break;
            }
        }
        printf("Case #%d: %.7f\n",i+1,finl);
    }
    return 0;
}
