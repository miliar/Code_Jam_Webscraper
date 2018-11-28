#include <iostream>
#include <stdio.h>
using namespace std;

int main()
{
    double T, C, F, X;
    double max_time, cur_time;
    double speed;
    cin >> T;

    for(int i=0; i<T; ++i)
    {
        speed = 2.0;
        cin >> C >> F >> X;

        max_time = X/speed;
        cur_time = 0.0;

        while(true)
        {
            if(C/speed + X/(speed + F) < max_time)
            {
                cur_time += C/speed;
                speed += F;
                max_time = X/speed;
            }
            else
            {
                cur_time += X/speed;
                break;
            }
        }

        cout << "Case #" << i+1 << ": ";
        //cout << setprecision(7) << round(cur_time * 10000000)/10000000.0 << endl;
        printf("%0.7f\n",cur_time);
    }
}
