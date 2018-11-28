#include <iostream>
#include <cmath>
#include <fstream>
#include <vector>
#include <iomanip>
#include <cstdlib>
#include <algorithm>
#include <bitset>
#include <set>
#include <time.h>
#include <map>
#include <deque>
using namespace std;

#define ll long long
#define ld long double
#define mk make_pair
#define pb push_back

int t, z, a[20], b[20], k, i, j, m, many, kart;

int main ()
{
    ifstream cin("1.txt");
    ofstream cout("output.txt");
    cin >> t;
    for (z=1; z<=t; z++)
    {
        cin >> k;
        for (i=1; i<=16; i++) a[i] = 0;
        for (j=1; j<=16; j++) b[j] = 0;
        for (i=1; i<=4; i++)
            for (j=1; j<=4; j++)
            {
                cin >> m;
                if (i==k) a[m]++;
            }
        cin >> k;
        for (i=1; i<=4; i++)
            for (j=1; j<=4; j++)
            {
                cin >> m;
                if (i==k) b[m]++;
            }
        many = 0 ;
        for (i=1; i<=16; i++)
            if (a[i]==1 && b[i]==1)
            {
                many++;
                kart = i;
            }
        cout << "Case #" << z << ": ";
        if (many==1) cout << kart << endl;
        if (many==0) cout << "Volunteer cheated!" << endl;
        if (many>1) cout << "Bad magician!" << endl;
    }
    return 0;
}