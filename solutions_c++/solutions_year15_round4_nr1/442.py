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

//#define DEBUGPRINT
#ifdef DEBUGPRINT
#define print(x) cout << #x" = "; printImpl(x);
#else
#define print(x) ;
#endif

int main()
{
    int caseCount;
    cin >> caseCount;
    
    for (int csIx = 1; csIx <= caseCount; ++csIx)
    {
        int R, C;
        cin >> R >> C;
        vector< vi > data(R, vi(C));
        REP(i,R)
        {
            REP(j,C)
            {
                char c;
                cin >> c;
                if (c == '^') data[i][j] = 1;
                if (c == '>') data[i][j] = 2;
                if (c == 'v') data[i][j] = 3;
                if (c == '<') data[i][j] = 4;
            }
        }

        int res = 0;
        bool impossible = false;
        REP(i,R)
        {
            REP(j,C)
            {
                print(i);
                print(j);
                if (data[i][j] == 0) continue;

                int c1 = 0, c2 = 0, c3 = 0, c4 = 0;
                for (int t = j + 1; t < C; ++t)
                {
                    if (data[i][t]) c2++;
                }
                for (int t = 0; t < j; ++t)
                {
                    if (data[i][t]) c4++;
                }

                for (int t = 0; t < i; ++t)
                {
                    if (data[t][j]) c1++;
                }
                for (int t = i + 1; t < R; ++t)
                {
                    if (data[t][j]) c3++;
                }

                if (c4 + c1 + c2 + c3 == 0)
                {
                    impossible = true;
                    break;
                }

                if (data[i][j] == 1 && c1 == 0) res++;
                if (data[i][j] == 2 && c2 == 0) res++;
                if (data[i][j] == 3 && c3 == 0) res++;
                if (data[i][j] == 4 && c4 == 0) res++;
            }

            if (impossible) break;
        }

        if (impossible)
            cout << "Case #" << csIx << ": IMPOSSIBLE" << endl;
        else
            cout << "Case #" << csIx << ": " << res << endl;
    }
    
    return 0;
}
