using namespace std;
#include <algorithm>
#include <iostream>
#include <iterator>
#include <numeric>
#include <sstream>
#include <fstream>
#include <cassert>
#include <climits>
#include <cstdlib>
#include <cstring>
#include <string>
#include <cstdio>
#include <vector>
#include <cmath>
#include <queue>
#include <deque>
#include <stack>
#include <iomanip>
#include <list>
#include <map>
#include <set>
 
#define foreach(x, v) for (typeof (v).begin() x=(v).begin(); x !=(v).end(); ++x)
#define forr(i, a, b) for (int i=(a); i<(b); ++i)
#define fore(i, a, b) for (int i=(a); i<=(b); ++i)
#define exists(e, v) find((v).begin(), (v).end(), (e))!=(v).end()
#define print(v) for (auto x=(v).begin(); x !=(v).end(); ++x) { cout << *x << " "; } cout << endl;  

const double EPS = 1e-7;

typedef vector<int> vi;
 
int main(){
    freopen("B-large.in","r", stdin);
    int T;
    cin >> T;
    fore(test, 1, T){
        double C, F, X;
        cin >> C >> F >> X;

        double t = 0.0;
        double c = 0;
        double rate = 2;

        while( C / rate + X / (rate + F) < X / rate ) {
            t += C / rate;
            rate += F;
        }
        
        std::cout << std::fixed;
        std::cout << std::setprecision(7);
        cout << "Case #" << test << ": " << t + X / rate<< endl;
    }
    return 0;
}

