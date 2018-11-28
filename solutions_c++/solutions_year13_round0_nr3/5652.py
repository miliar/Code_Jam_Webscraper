#include <iostream>
#include <cstdio>
#include <string>
#include <sstream>
#include <vector>
#include <algorithm>

using namespace std;
char grid[4][4];
bool gagne[2];
int nbPts;
inline bool isPalyndrome(long long nb)
{
    ostringstream oss;
    oss << nb;
    string str = oss.str();
    bool cool = true;
    const int length = str.size();
    for (int i = 0; i < length/2 && cool; i++)
    {
        if (str[i] != str[length-i-1])
            cool = false;
    }
    return cool;
}



int main()
{
    freopen("small.in", "r", stdin);
    freopen("small.out", "w", stdout);
    int nbT;
    cin >> nbT;

    vector<long long> fairSquare;
    const long long maxRacine = 100;

    for (int nb = 1; nb <= maxRacine; nb++)
    {
        if (!isPalyndrome(nb))
            continue;
        long long carre = nb*nb;
        if (!isPalyndrome(carre))
            continue;

        fairSquare.push_back(carre);
    }



    for (int t = 1; t <= nbT; t++)
    {
        long long deb, fin;
        cin >> deb >> fin;


        cout << "Case #" << t << ": ";
        cout <<(upper_bound(fairSquare.begin(), fairSquare.end(), fin)-lower_bound(fairSquare.begin(), fairSquare.end(),deb));
        cout << "\n";

    }

    //for (int i = 0; i < fairSquare.size(); i++)
    //    cout << fairSquare[i] << endl;



    return 0;
}
