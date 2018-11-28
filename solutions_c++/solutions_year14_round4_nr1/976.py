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
using namespace std;

//cout.precision(6);
//cout.setf( std::ios::fixed, std:: ios::floatfield ); // floatfield set to fixed

const long long MOD = 1000000007l;

#define REP(i,N) for (int i = 0; i < (N); ++i)
#define pb push_back

typedef vector<int> vi;
typedef unsigned int ui;
typedef long long ll;

template<class T>
void printImpl(const vector<T> & coll)
{
    copy(coll.begin(), coll.end(), ostream_iterator<typename T:: value_type>(cout, " "));
    cout << endl;
}

template<class T, int N>
void printImpl(T (&coll)[N])
{
    copy(coll, coll + N, ostream_iterator<T>(cout, " "));
    cout << endl;
}

template<class Key, class Value>
void printImpl(const map<Key, Value> & data)
{
    typename map<Key, Value>::const_iterator it;
    for (it = data.begin(); it != data.end(); ++it)
    {
        cout << it->first << ":" << it->second << endl;
    }
}

template <class T>
void printImpl(const T & data)
{
    cout << data << endl;
}

#define DEBUGPRINT
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
        int N, X;
        cin >> N >> X;
        vi S(N);
        REP(i,N) cin >> S[i];
        vi vis(N);
        
        int res = 0;
        REP(i,N)
        {
            if (vis[i])
                continue;
            
            vis[i] = 1;
            res++;
            bool foundPair = false;
            int pairIx = -1;
            int pair = -1;
            REP(j,N)
            {
                if (i == j)
                    continue;
                if (vis[j])
                    continue;
                
                if (S[j] > pair && S[i] + S[j] <= X)
                {
                    foundPair = true;
                    pairIx = j;
                    pair = S[j];
                }
            }
            if (foundPair)
                vis[pairIx] = 1;
        }
        cout << "Case #" << csIx << ": " << res << endl;
    }
    
    return 0;
}
