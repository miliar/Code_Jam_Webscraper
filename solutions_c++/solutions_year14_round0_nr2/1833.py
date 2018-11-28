#include <iostream>
#include <iomanip>
#include <string>
#include <vector>
#include <queue>
using namespace std;

double B, F, X;
double test()
{
    double co = 2;
    double ct = 0;
    while(true)
    {
        double wT = X/co; //wait util reach
        double nextAddT = B/co; //wait util to buy next
        if(nextAddT+(X/(co+F))>=wT) return ct+wT;
        co += F;
        ct += nextAddT;
        //return test(0, co+F, ct+nextAddT);
    }
}

void main()
{
    cout.setf(ios::fixed);
    cout.precision(7);
    //cout << 3.12345 << endl;

    int T;
    cin >> T;
    for(int C=0; C<T; ++C)
    {
        //double B, F, X;
        cin >> B >> F >> X;
        cout << "Case #" << C+1 << ": ";
        cout  << test() << endl;
        
    }

}