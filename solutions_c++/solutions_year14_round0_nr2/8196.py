#include <iostream>
#include <cmath>
#include <boost/math/special_functions/digamma.hpp>


using namespace std;
double phi( double x)
{
    return boost::math::digamma(x);
    //return (log(x) - 1/(2*x) - 1/(12*x*x) + 1/(120*pow(x,4)) - 1/(252*pow(x,6)) + 1/(240*pow(x,8)) -5/(660*pow(x,10)) + 691/(32760*pow(x,12)) - 1/(12*pow(x,14)));

}
void Calculate(int caseno)
{
    double C,F,X;
    cin >> C;
    cin >> F;
    cin >> X;


    double sum = 0;
    double time = 0.0;
    if ( C >= X)
    {
            time = X/2.0;
    }
    else
    {

        //slow way
    int N = floor((-2*C + F*X)/(F*C)); 
    assert(N <= X/C);
#ifdef slow
        for ( int i = 0; i <= N; ++i)
        {
            sum += 1/((F*i) + 2 );
        }
#else
        if (N >= 1)
        {
            sum = ((phi(N + (2.0/F) + 1) - phi(2.0/F))/F);
        

            time = sum*C; 
            time += ((X-C)/(F*N + 2));
        }
        else
        {
            time = X/2.0;
        }
#endif

    }

    cout << "Case #" << caseno <<": ";
    cout << std::fixed;
    cout.precision(7);
    cout << time << std::fixed << std::endl;

    assert(time <= X/2);
    //cout << "\nphi(1) = " << phi(1);
}

int main()
{
    int T; 

    cin >> T;

    for (int i = 0; i < T; ++i)
    {
        Calculate(i+1);
    }
}


