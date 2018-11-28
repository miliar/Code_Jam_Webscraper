/*
**  Coder : Amit Tiwari
** Handle : pipipzz
*/
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
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
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

#define pb push_back
#define all(v) v.begin(),v.end()
#define rep(i,n) for(int i=0;i<(int)(n);i++)
#define rep2(i,m,n) for(int i=m;i<(int)(n);i++)
#define For(it,c) for(__typeof(c.begin()) it=c.begin();it!=c.end();++it)
#define mem(a,b) memset(a,b,sizeof(a))
#define mp make_pair
#define INF (int)1e9
#define eps 1.0e-11
const double pi = acos(-1.0);

typedef stringstream ss;
typedef pair<int, int> pii;
typedef vector<pii> vpii;
typedef vector<string> vs;
typedef vector<int> vi;
typedef vector<double> vd;
typedef vector<vector<int> > vii;
typedef long long ll;
typedef long double ld;
typedef unsigned long long ull;

int A[5][5], B[5][5];

int main()
{
    int t;
    cin >> t;
    for(int x=1; x<=t; x++)
    {
        int first;
        cin >> first;
        first--;
        rep(i, 4)
        {
            rep(j, 4)
            {
                cin >> A[i][j];
            }
        }
        int second;
        cin >> second;
        second--;
        rep(i, 4)
        {
            rep(j, 4)
            {
                cin >> B[i][j];
            }
        }
        int counter = 0, match;
        for(int i=0; i<4; i++)
        {
            int curr = A[first][i];
            for(int j=0; j<4; j++)
            {
                if(curr == B[second][j])
                {
                    counter++;
                    match = curr;
                    break;
                }
            }
        }
        if(counter == 0)
        {
            cout << "Case #" << x << ": " << "Volunteer cheated!" << endl;
        }
        else if(counter == 1)
        {
            cout << "Case #" << x << ": " << match << endl;
        }
        else
        {
            cout << "Case #" << x << ": " << "Bad magician!" << endl;
        }
    }
    return 0;
}
