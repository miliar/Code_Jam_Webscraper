#include <bitset>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <algorithm>
#include <numeric>
#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <list>
#include <queue>
#include <deque>
#include <vector>
#include <map>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <stack>
#include <limits>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef vector<string> vs;
typedef vector<int> vi;
typedef vector<long long> vll;

template <typename T>
string tostring ( T value )
{
    ostringstream ss;
    ss << value;
    return ss.str();
}

template <typename T>
T strtonum ( const string &Text )
{
    istringstream ss(Text);
    T result;
    return ss >> result ? result : 0;
}
//----------------------------------

map<char,string> fromprs;

//==================================
void solve()
{
    int numCases = 1;
    cin >> numCases;

    for ( int ncase=1; ncase <= numCases; ncase++ )
    {
        //===== start case
        string s;
        int K;
        cin >> s >> K;
        vector<char> v(s.begin(),s.end());
        int ns = s.length();
        int ans=0;
        for (int i=0; i+K-1<ns; i++)
        {
            if (v[i]=='+')
                continue;
            ans++;
            for (int j=i; j<i+K; j++)
            {
                if (v[j]=='-')
                    v[j]='+';
                else
                    v[j]='-';
            }
        }
        bool possible=true;
        for (int i=0; i<ns; i++)
        {
            if (v[i]=='-')
                possible=false;
        }

        cout << "Case #" << ncase << ": ";
        if (possible)
            cout << ans << endl;
        else
            cout << "IMPOSSIBLE" << endl;

        //===== end case
        //===== end case

    }
}

int main()
{
#ifdef CCQTEST
#include "HRCPP1.h"
#endif
    solve();
#ifdef CCQTEST
#include "HRCPP2.h"
#endif
    return 0;
}
