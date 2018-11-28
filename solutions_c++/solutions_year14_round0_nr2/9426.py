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

int t, z, i, j;
ld c, f, x, l, r, mid;

void doit (ld dox, ld timer)
{
    if (timer>l) return;
    l = min (l, x/dox+timer);
    doit (dox+f, timer+c/dox);
}

int main ()
{
    ios_base::sync_with_stdio(false);
    ifstream cin("1.txt");
    ofstream cout("output.txt");
    cin >> t;
    for (z=1; z<=t; z++)
    {
        cin >> c >> f >> x;
        l=pow(10,18);
        doit(2, 0);
        cout << "Case #" << z << ": ";
        cout << fixed;
        cout << setprecision(7);
        cout << l << endl;
    }
    return 0;
}