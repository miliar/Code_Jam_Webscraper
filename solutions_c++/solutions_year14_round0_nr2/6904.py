# include <iostream>
# include <iomanip>
using namespace std;

int main()
{
    int n;
    cin>>n;
    for (int i=1;i<=n;i++)
    {


    long double c , rate=2 ,  time=0 , f , x;
    cin>>c>>f>>x;
    if (c/rate+x/(rate+f)>x/rate)
    {
        time+=x/rate;
        goto A;
    }
    else
    {

        time+=c/rate;
        while(1)
        {

            rate+=f;

            if (c/rate+x/(rate+f)>x/rate)
            {
                time+=x/rate;
                break;
            }
            time+=c/rate;
        }

    }
    A :
    cout<<"\nCase #"<<i<<": "<<setprecision(7)<<time;
    }

}
