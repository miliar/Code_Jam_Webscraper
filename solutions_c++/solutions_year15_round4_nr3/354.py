#include <iostream>
#include <sstream>
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
template<class Key> void printImpl(const set<Key> & data) { typename set<Key>::const_iterator it; for (it = data.begin(); it != data.end(); ++it) { cout << *it << endl; } }
template <class T> void printImpl(const T & data) { cout << data << endl; }

//#define DEBUGPRINT
#ifdef DEBUGPRINT
#define print(x) cout << #x" = "; printImpl(x);
#else
#define print(x) ;
#endif

int calc(const vi & d)
{
    int res = 0;
    REP(i,d.size())
    {
        if (d[i] == 3) res++;
    }
    return res;
}

int main()
{
    int caseCount;
    cin >> caseCount;
    
    for (int csIx = 1; csIx <= caseCount; ++csIx)
    {
        int N;
        cin >> N;
        char ddd[20000];
        cin.getline(ddd, 20000);

        vector< vector<string> > lines;

        REP(i,N)
        {
            char strC[20000];
            cin.getline(strC, 20000);
            string str(strC);

            istringstream iss(str);
            vector<string> parsed;
            copy(istream_iterator<string>(iss),
                 istream_iterator<string>(),
                 back_inserter(parsed));

            lines.push_back(parsed);
        }

        map<string, int> wordsToInt;
        int ix = 0;
        REP(i, lines.size())
        {
            REP(j, lines[i].size())
            {
                const string & w = lines[i][j];
                if (wordsToInt.find(w) == wordsToInt.end())
                {
                    wordsToInt[w] = ix;
                    ix++;
                }
            }
        }

        vi RES(ix);

        vector< vector<int> > linesInt(lines.size());
        REP(i, lines.size())
        {
            REP(j, lines[i].size())
            {
                linesInt[i].push_back(wordsToInt[lines[i][j]]);
            }
        }

        vi DICT(ix);
        REP(i, linesInt[0].size())
        {
            DICT[linesInt[0][i]] |= 1;
        }
        REP(i, linesInt[1].size())
        {
            DICT[linesInt[1][i]] |= 2;
        }

        int res = -1;
        for (int t = 0; t < (1 << (N-2)); ++t)
        {
            print(t);
            print(N);

            vi curDict(DICT);

            for (int i = 0; i < N - 2; ++i)
            {
                const vector<int> & sss = linesInt[2 + i];
                if (t & (1 << i))
                {
                    REP(k, sss.size())
                    {
                        curDict[sss[k]] |= 1;
                    }
                }
                else
                {
                    REP(k, sss.size())
                    {
                        curDict[sss[k]] |= 2;
                    }
                }
            }

//            print(eSet);
//            print(fSet);
            int currRes = calc(curDict);
            if (res == -1 || currRes < res)
            {
                res = currRes;
            }
        }


        cout << "Case #" << csIx << ": " << res << endl;
    }
    
    return 0;
}
