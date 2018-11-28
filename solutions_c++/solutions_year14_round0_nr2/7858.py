#include<iostream>
#include <iomanip>

using namespace std;

int main()
{
    int T,tt;
    double C,F,X;
    double t1,t2,cur_rate,t_pass;
    long long n_farm;

    cin >> T;
    cout << fixed << setprecision(7);
    for(tt=1;tt<=T;tt++)
    {

        cin >> C >> F >> X;

        cout << "Case #" << tt << ": " ;

        cur_rate = 2.0;
        t_pass = 0.0;
        n_farm = 0;
        while(1)
        {
            t1 = (C/(2+(n_farm*F))) + X/((2+(n_farm+1)*F)) ;
            t2 = X/((2+(n_farm)*F)) ;

            if (t1 < t2)
            {
                t_pass += C/(2+(n_farm*F));
                n_farm++;
            }
            else
            {
                cout << t_pass + t2;
                break;
            }

        }
        cout << '\n' ;

    }
    return 0;
}
