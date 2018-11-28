#include<cstdio>
#include<iostream>
using namespace std;
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int n,m,T;
    cin>>T;
    double c,f,x;
    int cn = 0;
    while(T--)
    {
        cin>>c>>f>>x;
        double sum = 0;
        double t = 2;
        double min = x/t;
        while(1)
        {

            sum += c / t;
            t += f;
            sum += x / t;
            if(sum<min)
            min = sum;
            else
            break;
            sum -= x/t;
        }
        printf("Case #%d: %.7lf\n",++cn,min);

    }
}
