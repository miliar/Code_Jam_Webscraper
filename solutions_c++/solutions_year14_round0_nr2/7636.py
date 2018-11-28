#include<cstdio>
#include<iostream>
#include<vector>
#include<algorithm>
#include<map>
#include<cstring>
#include<string>
#include <sstream>
#include<set>
#include<stack>
#include<queue>
#include<cctype>
#include<math.h>
#include<cstdlib>

#define I64 long long int
#define pii pair<int, int>
#define SIZE 1000
#define MAX 20000
#define VI vector <int>
#define VS vector <string>
#define MSI map <string, int>
#define MIS map <int, string>
#define MSS map <string, string>
#define pb push_back
#define pob pop_back
#define mp make_pair
#define IT iterator
#define SET(a, b) memset( a, b, sizeof (a) )

using namespace std;

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("outLarge.txt", "w", stdout);

    int tc, Case=1;
    double c, f, x;

    cin >> tc;

    while( tc-- ){

        cin >> c >> f >> x;

        double cookyps = 2.0;
        double totalTime = 0.0;

        while( true ){

            double reachX = x/cookyps;

            double temptime = (c/cookyps);
            double t = temptime;
            cookyps += f;
            temptime += (x/cookyps);

            if( temptime<reachX )totalTime += t;
            else{
                totalTime += reachX;
                break;
            }
        }

        printf("Case #%d: %.7lf\n", Case++, totalTime);
    }

    return 0;
}

