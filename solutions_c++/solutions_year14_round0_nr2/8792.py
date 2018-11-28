#include<iostream>
#include<stdio.h>
using namespace std;

int main()
{
    int t;
    double c,f,x;
    cin>>t;
    double factor=2;
    double time=0;
    int testcase=1;
    while(t--)
    {
factor=2.0;
        time=0;
        cin>>c>>f>>x;
        while(true)
			{
				if(x/factor< c/factor+x/(factor+f))
				{
					time+=x/factor;
					break;
				}
				else
				{
					time+=c/factor;
					factor+=f;
				}
			}

        printf("Case #%d: %.7f\n",testcase++,time);

    }

    return 0;
}
