#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <cassert>
#include <ctime>
#include <deque>

using namespace std;

#define forn(i, n) for (int i = 0; i < int(n); i ++)
#define ford(i, n) for (int i = int(n) - 1; i >= 0; i --)
#define mp make_pair
#define pb push_back
#define fs first
#define sc second
#define pi 3.1415926535897932384626433832795l

typedef long long ll;
typedef long double ld;

int main(){
#ifdef SG
    freopen ("input.txt","rt",stdin);
  freopen ("output.txt","wt",stdout);
#endif  
    int t;
    cin >> t;
    forn(qqq, t){
        double c, f, x;
        cin >> c >> f >> x;
        cout << "Case #" << qqq + 1 << ": ";
        double ans = 1000000000;
        double tekf = 2, tekt = 0;

        forn(qqq, 1000000){
            ans = min(ans, x / tekf + tekt);         
            tekt += c / tekf;
            tekf += f;
        }
        printf ("%0.7lf\n", ans);

    }
        


    return 0;
}
