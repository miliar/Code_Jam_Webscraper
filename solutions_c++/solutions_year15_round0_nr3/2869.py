#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include "fstream"

#define sz(X) ((int)X.size())
#define FOR(i,x,y) for(int i=x; i<y; ++i)

using namespace std;
int A[4][4] =
{
    {1,2,3,4},
    {2,-1,4,-3},
    {3,-4,-1,2},
    {4,3,-2,-1}
};

int f(char c)
{
    switch (c) {
        case '1':
            return 1;
            break;
        case 'i':
            return 2;
            break;
        case 'j':
            return 3;
            break;
        case 'k':
            return 4;
            break;
    }
}
int main()
{
    ofstream cout ("output.txt");
    ifstream cin ("input.txt");

    int T;
    cin>>T;

    FOR(i,1,T+1)
    {
        int L,X; string S;
        cin>>L>>X>>S;

        int a = 1;
        int l=0;

        for(;l<L*X;++l)
        {
            if(a == f('i')) break;

            int sign = 1;
            if(a<0) sign = -1, a=-a;

            a = A[a-1][f(S[l%L])-1] * sign;
        }

        a = 1;
        for(;l<L*X;++l)
        {
            if(a == f('j')) break;

            int sign = 1;
            if(a<0) sign = -1, a=-a;

            a = A[a-1][f(S[l%L])-1] * sign;
        }

        a = 1;
        for(;l<L*X;++l)
        {
            int sign = 1;
            if(a<0) sign = -1, a=-a;

            a = A[a-1][f(S[l%L])-1] * sign;
        }


        cout<<"Case #"<<i<<": ";
        if(a == 4) cout<<"YES\n";
        else       cout<<"NO\n";


    }

    return 0;
}
// END KAWIGIEDIT TESTING

//Powered by KawigiEdit 2.1.4 (beta) modified by pivanof!
