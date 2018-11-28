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


int main()
{
    ofstream cout ("output.txt");
    ifstream cin ("input.txt");

    int T;
    cin>>T;

    FOR(i,1,T+1)
    {

        string c,A;
        cin>>c>>A;

        int N = sz(A);
        int cur = 0;
        int more = 0;

        FOR(i,0,N)
        {
            if(cur < i)
            { more += i - cur; cur = i; }

            cur += A[i] - '0';
        }

        cout<<"Case #"<<i<<": "<<more<<endl;
    }

    return 0;
}
// END KAWIGIEDIT TESTING

//Powered by KawigiEdit 2.1.4 (beta) modified by pivanof!
