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

int check(const vector<int> & A, int m, int maxIx)
{
    vi B = A;
    
    int res = 0;
    if (m < maxIx)
    {
        for (int i = maxIx; i > m; --i)
        {
            swap(B[i], B[i-1]);
            res++;
        }
    }
    else if (m > maxIx)
    {
        for (int i = maxIx; i < m; ++i)
        {
            swap(B[i],B[i+1]);
            res++;
        }
    }
    
    for (int i = 0; i < m; ++i)
    {
        for (int j = i + 1; j < m; ++j)
        {
            if (B[i] > B[j])
            {
                res++;
            }
        }
    }
    
    for (int i = m + 1; i < B.size(); ++i)
    {
        for (int j = i + 1; j < B.size(); ++j)
        {
            if (B[i] < B[j])
                res++;
        }
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
        vi A(N);
        REP(i,N) cin >> A[i];

        int res = 0;
        REP(i,N)
        {
            int minIx = -1;
            for (int j = 0; j < N - i; ++j)
            {
                if (minIx == -1 || A[j] < A[minIx])
                {
                    minIx = j;
                }
            }
            if (minIx < N - 1 - i - minIx)
            {
                res += minIx;
            }
            else
            {
                res += N - 1 - i - minIx;
            }
            for (int t = minIx; t < N - i - 1; ++t)
            {
                swap(A[t], A[t+1]);
            }
        }
        
        cout << "Case #" << csIx << ": " << res << endl;
    }
    
    return 0;
}
