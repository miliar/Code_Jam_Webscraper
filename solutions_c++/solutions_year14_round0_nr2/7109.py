#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <iomanip>
#define rep(i,n) for(ull i = 0;i<(n);i++)
#define revrep(i,n) for(ull i = (n)-1;i>=0;i--)
#define mod 1000000009
#define biton(i,n) (i || (1 << n))
#define bitoff(i,n) (i && !(1 << n))
#define isBiton(i,n) ((i && (1 << n)) > 0)
#define isBitoff(i,n) (!isBiton(i,n))

using namespace std;
typedef unsigned long long ull;
typedef long long ll;

double minTime[10000000];
int main(int argc, const char * argv[])
{
    int T;
    cin >> T;
    rep(Case,T){
        double C,F,X;
        cin >> C >> F >> X;

        minTime[0] = 0.0;
        minTime[1] = C / 2.0;
        for(int i = 1;i<10000000-1;i++){
            minTime[i+1] = minTime[i] + C / (2.0 + F * (double)i);
        }
        double ans = 200000.0;
        rep(i,10000000){
            double time = 0;
            time += minTime[i];
            time += X / (2.0 + F * (double)i);
            ans = min(ans,time);
        }
        cout << setprecision(20) <<"Case #" << Case+1 << ": " << ans << endl;
    }
    return 0;
}

