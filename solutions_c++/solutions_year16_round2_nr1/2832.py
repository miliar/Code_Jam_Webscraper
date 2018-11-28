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
typedef vector<string> vecs;
typedef vector<int> veci;
typedef vector<long long> vecll;

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
#define MOD 1000000007
void calckmp(vector<int> &kmp, const string &S)
{
    kmp[0] = 0;
    int N = S.size();
    for (int i = 1; i < N; i++)
    {
        int l = kmp[i - 1];
        while (l > 0 && S[i]!= S[l])
        {
            l = kmp[l-1];
        }
        if (S[i] == S[l])
        {
            kmp[i] = l + 1;
        }
        else
        {
            kmp[i] = 0;
        }
    }
}
//----------------------------------
void solve()
{
    int numCases = 1;
    cin >> numCases;
    string sdigit[] = { "ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE" };

    for ( int ncase=1; ncase <= numCases; ncase++ )
    {
        //===== start case
        string s;
        cin >> s;
        string sorted=s;
        //sort(s.begin(), s.end());
        int numc[26];
        for (int i=0; i<26;i++)
            numc[i]=0;
        for (int i=0; i<s.size(); i++) {
            numc[s[i]-'A']++;
        }
        //for (int i=0; i<26;i++) cout << i << ":" << numc[i] << endl;

        int numd[10];
        for (int i=0; i<10; i++) {
            numd[i]=0;
        }

        //0z,2w,3h,4u,5f,6x,7s,8g,9i,1o
        int d;
        numd[0] = numc['Z'-'A'];
        d=0;
        for (int i=0;i<sdigit[d].size(); i++) {
            numc[sdigit[d][i]-'A'] -= numd[d];
        }
        numd[2] = numc['W'-'A'];
        d=2;
        for (int i=0;i<sdigit[d].size(); i++) {
            numc[sdigit[d][i]-'A'] -= numd[d];
        }
        numd[4] = numc['U'-'A'];
        d=4;
        for (int i=0;i<sdigit[d].size(); i++) {
            numc[sdigit[d][i]-'A'] -= numd[d];
        }
        numd[5] = numc['F'-'A'];
        d=5;
        for (int i=0;i<sdigit[d].size(); i++) {
            numc[sdigit[d][i]-'A'] -= numd[d];
        }
        numd[6] = numc['X'-'A'];
        d=6;
        for (int i=0;i<sdigit[d].size(); i++) {
            numc[sdigit[d][i]-'A'] -= numd[d];
        }
        numd[7] = numc['S'-'A'];
        d=7;
        for (int i=0;i<sdigit[d].size(); i++) {
            numc[sdigit[d][i]-'A'] -= numd[d];
        }
        numd[8] = numc['G'-'A'];
        d=8;
        for (int i=0;i<sdigit[d].size(); i++) {
            numc[sdigit[d][i]-'A'] -= numd[d];
        }
        numd[3] = numc['H'-'A'];
        d=3;
        for (int i=0;i<sdigit[d].size(); i++) {
            numc[sdigit[d][i]-'A'] -= numd[d];
        }
        numd[9] = numc['I'-'A'];
        d=9;
        for (int i=0;i<sdigit[d].size(); i++) {
            numc[sdigit[d][i]-'A'] -= numd[d];
        }
        numd[1] = numc['O'-'A'];

        string num="";
        for (int i=0; i<=9; i++)
        {
            for (int j=0; j<numd[i]; j++)
                num += tostring(i);
        }
        cout << "Case #" << ncase << ": ";
        cout << num << endl;
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
