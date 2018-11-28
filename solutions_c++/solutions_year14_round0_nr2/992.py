#include <iostream>
#include <queue>
#include <cmath>
#include <iterator>
#include <algorithm>
#include <fstream>
#include <set>
#include <sstream>
#include <iomanip>
using namespace std;


double calcul(double C,double F,double X,int N)
{
    double t = 0;
    double prod = 2;
    for(int c=0;c<N;c++)
    {
        double delay = C/prod;
        t += delay;
        prod += F;
    }

    double delay = X/prod;
    return t + delay;
}

double ternary_search(double C,double F,double X)
{
    double N = 0;
    double vitact = 2;
    double t = 0;
    double best = 1000000000000;
    for(int c=0;c<2*1e5;c++)
    {
        double tmp = t + X/vitact;
        if(tmp<best)
        {
            N = c;
            best = tmp;
        }
        t+=C/vitact;
        vitact+=F;
    }
    return best;
}



int main()
{
    ios_base::sync_with_stdio(false);
    ifstream in("input.txt");
    ofstream out("output.txt");
    #define cin in
    #define cout out
    int nb_cas;
    cin>>nb_cas;
    for(int cas=1;cas<=nb_cas;cas++)
    {
        cout<<"Case #"<<cas<<": ";
        double C,F,X;
        cin>>C>>F>>X;


        double res=ternary_search(C,F,X);



        cout<<fixed<<setprecision(8)<<res<<endl;
    }
}
