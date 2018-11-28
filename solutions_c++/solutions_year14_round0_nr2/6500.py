#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <iostream>
#include <climits>
#include <algorithm>
using namespace std;
#define llt long long int
int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    llt t;
    scanf("%lld",&t);
    for(llt k=1;k<=t;k++)
    {
        double c,f,x;
        cin>>c>>f>>x;
        double time=0;
        double rate=2;
        cout<<"Case #"<<k<<": ";
        if(x<=c)
        {
            time+=x/rate;
            printf("%0.7lf\n",time);
            //cout<<time<<endl;
            continue;
        }
        //time+=c/rate;
        while(1)
        {
            double temp=x/rate;
            double bn=c/rate;
           // cout<<c/rate<<" ";
            if(bn+x/(rate+f)<temp)
            {
                rate+=f;
                time+=bn;
               // cout<<time<<endl;
            }
            else
            {
                time+=x/rate;
                printf("%0.7lf\n",time);
                break;
            }
        }
    }
    return 0;
}
