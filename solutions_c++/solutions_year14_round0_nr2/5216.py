#include<iostream>
#include<stdio.h>
using namespace std;

int main()
{
    int t,l=0;
    cin>>t;
    while(t--)
    {
        l++;
        float c,f,x,i=2.0;
        cin>>c>>f>>x;
        float time=0,t1,t2;
        while(1)
        {
            t1=x/i;
            t2=(c/i)+(x/(i+f));
            if(t1>t2)
            {
                time+=c/i;
                i+=f;

            }
            else
             {
                 time+=t1;
                 break;
             }
        }
        printf("Case #%d: %.7f\n",l,time);

    }
    return 0;
}
