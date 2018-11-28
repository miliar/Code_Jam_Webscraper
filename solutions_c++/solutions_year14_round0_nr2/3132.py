#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
using namespace std;

#define foreach(u, o) \
    for (typeof((o).begin()) u = (o).begin(); u != (o).end(); ++u)
const int INF = 2147483647;
const double EPS = 1e-9;
const double pi = acos(-1);
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef vector<vi> vvi;
typedef vector<vii> vvii;
template <class T> T mod(T a, T b) { return (a % b + b) % b; }
template <class T> int size(const T &x) { return x.size(); }

double C, F, X, G;

double buy_next()
{
    return C/G + X/(G+F);
}

int main()
{
    int T;
    double total;
    cin >> T;

    for(int t = 0; t < T; ++t){
        printf("Case #%d: ", t+1);
        total = 0.0;
        G = 2.0;
        cin >> C >> F >> X;
        while(buy_next() < (X/G)){
            total += C/G;
            G += F;
        }
        total += X/G;
        printf("%.7f\n", total);
    }
    return 0;
}
