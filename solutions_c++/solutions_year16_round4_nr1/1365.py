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

bool checkifwinner(char winner, int N, int R, int P, int S, string &result)
{
    vector<char> pairs;
    pairs.push_back(winner);
    for (int i=0; i<N; i++)
    {
        vector<char> p;
        for (int i=0; i<pairs.size(); i++)
        {
            string s = fromprs[pairs[i]];
            p.push_back(s[0]);
            p.push_back(s[1]);
        }
        pairs=p;
    }
    int np=0;
    int nr=0;
    int ns=0;
    for (int i=0; i<pairs.size(); i++)
    {
        if (pairs[i]=='P') np++;
        else if (pairs[i]=='R') nr++;
        else if (pairs[i]=='S') ns++;
    }

    //cout << "nr,np,ns" << nr << np << ns << endl;
    if (np==P && nr==R && ns==S)
    {
        //cout << "equal" << endl;
        vector<string> vstr;
        for (int i=0; i<pairs.size(); i++)
        {
            vstr.push_back(tostring(pairs[i]));
            //cout << pairs[i];
        }
        //cout << endl;
        for (int i=0;i<N;i++)
        {
            vector<string> vtmp;
            for (int i=0;i<vstr.size();i+=2)
            {
                if (vstr[i]<vstr[i+1])
                    vtmp.push_back(vstr[i]+vstr[i+1]);
                else
                    vtmp.push_back(vstr[i+1]+vstr[i]);
            }
            vstr = vtmp;
        }
        result = vstr[0];
        //cout << result << endl;
        return true;
    }
    else
        return false;
}
//==================================
void solve()
{
    int numCases = 1;
    cin >> numCases;
    fromprs['P']="PR";
    fromprs['R']="RS";
    fromprs['S']="PS";

    for ( int ncase=1; ncase <= numCases; ncase++ )
    {
        //===== start case
        int N,R,P,S;
        cin >> N >> R >> P >> S;

        vector<char> vc;
        for (int i=0; i<R; i++)
            vc.push_back('R');
        for (int i=0; i<P; i++)
            vc.push_back('P');
        for (int i=0; i<S; i++)
            vc.push_back('S');

        sort(vc.begin(),vc.end());

        cout << "Case #" << ncase << ": ";

        if (N==1)
        {
            if (vc[0]==vc[1])
                cout << "IMPOSSIBLE" << endl;
            else
            {
                cout << vc[0];
                cout << vc[1] << endl;
            }
        }
        else
        {
            //winner P
            string result="";
            bool valid = checkifwinner('P',N,R,P,S,result);
            if (!valid)
                valid = checkifwinner('R',N,R,P,S,result);
            if (!valid)
                valid = checkifwinner('S',N,R,P,S,result);
            if (!valid)
                cout << "IMPOSSIBLE" << endl;
            else
                cout << result << endl;
        }

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
