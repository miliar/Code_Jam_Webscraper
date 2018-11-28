#include <iostream>
#include <algorithm>
#include <vector>
#include <deque>
#include <map>
#include <fstream>
#include <sstream>
#include <math.h>
#include <stack>
#include <string.h>
using namespace std;

#define FOR(i, a, b) for(int i=a; i<b; i++)
#define FORE(i, a, b) for(int i=a; i<=b; i++)
#define ll long long
#define mp make_pair
#define pii pair<int, int>
#define pll pair<long, long>
#define PI 3.14159265359
#define mod 1000000007

#define maxN 2500

double t;
double cost, add_cps, x;

int main()
{
    ifstream ifs("a.in");
    FILE *fp = fopen("a.out", "w");
    int T;
    ifs >> T;
    FOR(awt, 0, T) {
        ifs >> cost >> add_cps >> x;
        t = 0;
        double cookies_per_second = 2;
        while(1) {
            double t1 = x/cookies_per_second;
            double t2 = cost/cookies_per_second + x/(cookies_per_second+add_cps);
            if(t1 <= t2) {
                fprintf(fp, "Case #%d: %.10f\n", awt+1, t + x/cookies_per_second);
                break;
            }   else    {
                t+=cost/cookies_per_second;
                cookies_per_second+=add_cps;
            }


        }





    }
}
