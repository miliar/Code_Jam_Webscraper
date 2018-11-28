#include<cstdio>
#include<iostream>
using namespace std;
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int n,m,T;
    cin>>T;

    int cn = 0;
    while(T--)
    {
        double c,f,x;
        cin>>c>>f>>x;
        double sum = 0;
        double t = 2;
        double min = x/t;
        int ac=1;
        while(ac)
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
