#include <iostream>
#include <iterator>
#include <fstream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <queue>
#include <stack>
#include <string.h>
#include <stdio.h>
#include <iomanip>
using namespace std;

//cout.precision(6);
//cout.setf( std::ios::fixed, std:: ios::floatfield ); // floatfield set to fixed

const long long MOD = 1000000007LL;

#define REP(i,N) for (int i = 0; i < (N); ++i)

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef unsigned int ui;
typedef long long ll;
typedef vector<ll> vll;

template<class T> void printImpl(const vector<T> & coll) { copy(coll.begin(), coll.end(), ostream_iterator<T>(cout, " ")); cout << endl; }
template<class T, int N> void printImpl(T (&coll)[N]) { copy(coll, coll + N, ostream_iterator<T>(cout, " ")); cout << endl; }
template<class Key, class Value> void printImpl(const map<Key, Value> & data) { typename map<Key, Value>::const_iterator it; for (it = data.begin(); it != data.end(); ++it) { cout << it->first << ":" << it->second << endl; } }
template <class T> void printImpl(const T & data) { cout << data << endl; }

#define DEBUGPRINT
#ifdef DEBUGPRINT
#define print(x) cout << #x" = "; printImpl(x);
#else
#define print(x) ;
#endif

const double eps = 1e-9;

double abs(double x)
{
    if (x < 0) return -x;
    return x;
}

int main()
{
    int caseCount;
    cin >> caseCount;
    cout.precision(9);
    cout.setf( std::ios::fixed, std:: ios::floatfield ); // floatfield set to fixed

    for (int csIx = 1; csIx <= caseCount; ++csIx)
    {
        int N;
        cin >> N;
        double V, X;
        cin >> V >> X;

        vector<double> R(N), C(N);
        REP(i,N)
        {
            cin >> R[i] >> C[i];
        }

        if (N == 1)
        {
            if (abs(C[0] - X) > eps)
            {
                cout << "Case #" << csIx << ": IMPOSSIBLE" << endl;
            }
            else
            {
                cout << "Case #" << csIx << ": " << V / R[0] << endl;
            }
        }

        if (N == 2)
        {
            if (X + eps < min(C[0], C[1]))
            {
                cout << "Case #" << csIx << ": IMPOSSIBLE" << endl;
            }
            else if (X - eps > max(C[0], C[1]))
            {
                cout << "Case #" << csIx << ": IMPOSSIBLE" << endl;
            }
            else if (abs(C[0] - C[1]) < eps)
            {
                cout << "Case #" << csIx << ": " << V / (R[0] + R[1]) << endl;
            }
            else
            {
                double v0 = V * (X - C[1]) / (C[0] - C[1]);
                double v1 = V - v0;
                cout << "Case #" << csIx << ": " << max(v0 / R[0], v1 / R[1]) << endl;
            }
        }
    }
    
    return 0;
}
