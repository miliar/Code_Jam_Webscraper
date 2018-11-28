#include <iostream>
#include <iomanip>

using namespace std;

double solve(double C, double F, double X)
{

    if(C > X)
        return X/2.0;

    double I=2, T=0;
    while(1)
    {
        T += C/I;
        if((X-C)/I < C/F) return (X-C)/I + T;
        I += F;
    }
}

int main()
{
    int nb;
    cin >> nb;
    cout.precision(10);
    for(int i=0 ; i<nb ; i++)
    {
        double C,F,X;
        cin >> C;cin >> F; cin >> X;
        cout << "Case #"<<i+1<<": "<<solve(C,F,X)<<endl;
    }
    return 0;
}
