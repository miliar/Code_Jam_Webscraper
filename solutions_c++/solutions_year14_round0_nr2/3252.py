#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <climits>
#include <queue>
#include <algorithm>
#include <vector>
#include <list>
#include <set>
#include <stack>
#include <map>
#include <cstring>
#include <cmath>
using namespace std;

//trocar para 0 para desabilitar output
#if 1
#define DEBUG(x) cout << x << endl
#define PAUSE() cin.get(); cin.get()
#else
#define DEBUG(x)
#define PAUSE()
#endif

#define TRACE(x) DEBUG(#x << " = " << x)
#define DEBUGS() DEBUG("***************************")
#define MAX 1

double solve(double c, double f, double x){
    double actual = 2.0, ans = x/actual, time = 0;
    while (true){
        double value = time + c/actual + x/(actual+f);
        if (value < ans){
            ans = value;
            time += c/actual;
            actual += f;
        }
        else break;
    }
    return ans;
}

int main(){
    int t, cases = 0;
    cin >> t;
    while (t--){
        double c, f, x;
        cin >> c >> f >> x;
        double ans = solve(c, f, x);
        cout.precision(7);
        cout << fixed << "Case #" << ++cases << ": " << ans << endl;
    }
    return 0;
}
