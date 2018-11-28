#include <iostream>
#include <cstdio>

using namespace std;

int main()
{

    int k;
    cin>>k;
    for(int cc = 0; cc < k; cc++)
    {
        double c, f, x;
        cin>>c>>f>>x;
        double t = 0.0;
        double rate = 2.0;
        while(true)
        {
            if (x/rate <= (c/rate + x/(rate+f)))
            {
                t += x/rate;
                break;
            }
            else
            {
                t += c/rate;
                rate += f;
            }
        }
        cout<<"Case #"<<cc+1<<": ";
        printf("%.7f", t);
        cout<<endl;
    }
    return 0;
}
