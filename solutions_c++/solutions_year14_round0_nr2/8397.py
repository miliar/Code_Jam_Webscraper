#include <iostream>
#include <set>
#include <vector>
#include <cstdio>
#include <iomanip>

using namespace std;

long double bonusFarm,priceFarm, bestAns, objCookies;

bool isPossible(long double objTime)
{
    long double time = 0;
    long double nbCookies = 0;
    long double rate = 2;

    while (time < objTime)//nbCookies < objCookies)
    {
        if (time + objCookies/rate < objTime)
            return true;
        else
        {
            time += priceFarm/rate;
            rate += bonusFarm;
        }
    }

    return false;
}


const long double deux = 2;


int main()
{
    freopen("t.in", "r", stdin);
    //freopen("t.out", "w", stdout);

    const long double prec = 1e-12;
    int nbT;
    cin >> nbT;
    long double deb, fin, mil;
    for (int t = 1; t <= nbT; t++)
    {
        cin >> priceFarm >> bonusFarm >> objCookies;

        fin = objCookies/deux;
        deb = 0;
        while (fin - deb >= prec)
        {
            mil = (fin+deb)/2;
            if (isPossible(mil))
                fin = mil;
            else
                deb = mil;
        }




        cout << "Case #" << t << ": " << std::fixed << std::setprecision(7) << (fin+deb)/deux << endl;

    }
    return 0;
}
