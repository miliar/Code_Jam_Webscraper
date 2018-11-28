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
#include <cstring>

typedef long long ll;

using namespace std;
long long A,N,a[1000010],T;
map < vector<long long>, int> best;
long long solve (int sofar ,int ind)
{
    if (ind == N)
        return 0;
    vector <long long> B(2);
    B[0]=sofar;
    B[1]=ind;
    if (best.count(B))
        return best[B];

    if (sofar > a[ind])
        return best[B] = solve (sofar+a[ind],ind+1);
    else
    {
        if (sofar!=1)
            return best[B] =1+min (solve (sofar+sofar-1, ind), solve (sofar, ind+1));
        else
            return best[B] = 1+solve (sofar, ind+1);
    }
}
int main ()
{
    freopen("A-large.in","r",stdin);
    freopen("2.out","w",stdout);
    cin >> T;
    long long t = 1;
    while (T--)
    {
        cin >> A >> N;
        for (int i=0; i<N; i++)
            cin >> a[i];
        sort(a,a+N);
        cout << "Case #" << t++ << ": " << solve (A,0) << endl;
        best.clear();
    }

    return 0;
}
