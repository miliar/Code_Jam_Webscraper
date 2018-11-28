#include <iostream>
#include <iomanip>

using namespace std;

double temps(double C, double F, double X, int n)
{
    double sortie = X/(2+(n+1)*F);

    for(int i=0;i<=n;++i)
    {
        sortie+=C/(2+i*F);
    }
    return sortie;
}

int main()
{
    int T;
    double C,X,F;

    cin>>T;

    for(int t=1;t<=T;t++)
    {
        cin>>C>>F>>X;

        double courant=temps(C,F,X,-1);
        double futur=temps(C,F,X,0);

        for(int n=1;futur<=courant;++n)
        {
            courant=futur;
            futur=temps(C,F,X,n);
        }

        cout<<"Case #"<<t<<": ";
        cout << fixed << setprecision(7) << courant << endl;

    }

    return 0;
}
