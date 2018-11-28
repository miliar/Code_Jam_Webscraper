#include <algorithm>
#include <functional>
#include <numeric>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <cassert>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <sstream>
using namespace std;

#define LL long long
#define LD long double
#define PR pair<int,int>

#define For(i,n) for (i=0; i<int(n); i++)
#define ForR(i,n) for (i=int(n)-1; i>=0; i--)
#define Sz(s) int((s).size())
#define All(s) (s).begin(),(s).end()
#define Fill(s,v) memset(s,v,sizeof(s))

LL r,t;
LL res;

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt","w",stdout);
    
    int num,i;
    cin >> num;
    for(i=0;i<num;i++)
    {
        cout << "Case #" << i+1 << ": ";
        cin >> r >> t;
        res = 0;
        LL temp = t;
        temp = temp - (2*r+4*1-3);
        while(temp>=0)
        {
            res++;
            temp = temp - (2*r+4*res+1);
        }
        cout << res << endl;
    }
    return 0;
    
}