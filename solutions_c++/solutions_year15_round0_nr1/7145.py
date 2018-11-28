// CONTEST TEMPLATE

// includes
#include <cassert>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <iostream>
#include <limits>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <utility>
#include <vector>

#define ARRAY_LENGTH(a) (sizeof((a)) / sizeof((a[0])))
typedef unsigned long long ull;
typedef long long          ll;

using namespace std;


template <typename T>
void printArray(const T arr[], size_t n)
{
    for (int i=0; i<n; ++i)
        cout << arr[i] << " ";
    cout << endl;
}


//--------------------------------------------------------------------------------------------------
// SOLUTION BELOW

int T;
string S;
int Smax;

int calc()
{
    int nbStanding = 0;
    int nbInvites  = 0;
    for (int i=0; i<=Smax; ++i)
    {
        // we need to invite extra people
        if (nbStanding < i) 
        {
            int toInvite = (i - nbStanding);
            nbInvites  += toInvite;
            nbStanding += toInvite;
        }
        nbStanding += S[i] - '0';
    }

    return nbInvites;
}

int main()
{
    cin >> T;
    for (int k=1; k<=T; ++k)
    {
        cin >> Smax;
        cin >> S;
        printf("Case #%d: %d\n", k, calc());
    }

    return 0;
} 
