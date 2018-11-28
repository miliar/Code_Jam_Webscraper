#include <iostream>
#include <iomanip>
using namespace std;

double c, f, x, t;
double r;

void real_main()
{
    cin >> c >> f >> x;
    r = 2.0; t = 0.0;
    do {
        double conserve = x/r;
        double tryn = c/r + x/(r+f);
        if (tryn >= conserve)
        {
            t += conserve;
            break;
        }
        else
        {
            t += c/r;
            r += f;
        }
    } while (1);
    cout<<setprecision(7)<<fixed<<t<<endl;
}

int main()
{
    int T; cin>>T;
    for (int i = 1; i<=T; i++)
    {
        cout<<"Case #"<<i<<": ";
        real_main();
    }
    return 0;
}
