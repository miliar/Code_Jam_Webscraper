#include <iostream>
#include <cstdio>
#include <vector>


using namespace std;

double solve(double c, double f, double x)
{
    double curr_rate=2.0;
    double curr_x=x;
    double curr_time=0.0;
    double curr_cookies=0;
    while( 1)
    {
        if(curr_cookies>=c)
            if((curr_x-curr_cookies)/curr_rate > (curr_x-curr_cookies+c)/(curr_rate+f))
            {
                //curr_time+=c/curr_rate;
                curr_rate+=f;
                curr_cookies-=c;
            }
            else
            {
                return curr_time+=(curr_x-curr_cookies)/curr_rate;
            }
        else
        {
            if(c>curr_x) return curr_time+=curr_x/curr_rate;
            else
                {
                    curr_time+=(c-curr_cookies)/curr_rate;
                    curr_cookies=c;
                }
        }

    }
}


int main()
{
    int T;double c,f,x;
    cin>>T;
    for(int i=1;i<=T;i++)
    {
        cin>>c>>f>>x;
        cout<<"Case #"<<i<<": ";
        printf("%.7lf\n",solve(c,f,x));
    }


    return 0;
}
