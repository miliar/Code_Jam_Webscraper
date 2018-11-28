#include <iostream>
#include <stdio.h>
#include <math.h>
using namespace std;

int main()
{
    int t,x=1;
    scanf("%i",&t);
    while(t--)
    {
        int n,a[10];
        scanf("%i",&n);
        for(int i=0;i<10;i++)
            a[i]=0;
        int l=n,f;
        for(int i=1;i<1000;i++)
        {
            int m=l;
            f=1;
            while(m!=0)
            {
                a[m%10]=1;
                m/=10;
            }
            for(int i=0;i<10;i++)
            {
                if(a[i]==0)
                {
                    f=0;
                    break;
                }
            }
            if(f==1)
                break;
            else
                l+=n;
        }
        if(f==1)
            printf("Case #%i: %i\n",x,l);
        else
            printf("Case #%i: INSOMNIA\n",x);
            x++;
    }
	return 0;
}
