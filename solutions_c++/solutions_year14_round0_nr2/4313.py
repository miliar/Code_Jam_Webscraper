#include<stdio.h>
#include<iostream>
using namespace std;
int main()
{
    int test,p;
    double c,f,x,t1,t2,t3,total,f1;
    cin>>test;
    p=test;
    while(test--)
    {
        cin>>c>>f>>x;
        total=0;
        t1=x/2;
        f1=2;
        t3=(x/(f+f1));
        t2=(c/2)+t3;
        if(t1>t2)
        {
            t2=t2-t3;
            total=t2;
            f1=2+f;
            while(1)
            {
                t1=(x/f1);
                t2=(c/f1)+(x/(f1+f));
                if(t1>t2)
                {
                    total=total+(c/f1);
                    f1=f+f1;
                }
                else
                {
                    total=total+(x/f1);
                    break;
                }

            }
        }
        else
        {
            total=total+(x/f1);
        }
        printf("Case #%d: %.7lf\n",p-test,total);
    }
    return 0;
}
