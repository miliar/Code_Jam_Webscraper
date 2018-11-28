#include <iostream>
#include <sstream>
#include <string>
#include <cstring>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <deque>
#include <cstdio>
#include <cassert>
#include <cstdlib>
#include <numeric>
#include <functional>
#include <algorithm>

using namespace std;

#define forn(i,n) for(int i=0;i<(int)(n);i++)
#define forsn(i,s,n) for(int i=(s);i<(int)(n);i++)
#define dforn(i,n) for(int i=(n)-1;i>=0;i--)
#define dforsn(i,s,n) for(int i=(n)-1;i>=(int)(s);i--)

#define forall(i,c) for(auto i = (c).begin(); i != (c).end(); i++)
#define dforall(i,c) for(auto i = (c).rbegin(); i != (c).rend(); i++)
#define all(c) (c).begin(),(c).end()

#define esta(x,c) ((c).find(x) != (c).end())
#define zMem(c) memset((c),0,sizeof(c))

typedef long long tint;
typedef long double tdbl;

typedef pair<int,int> pint;
typedef pair<tint,tint> ptint;

typedef vector<int> vint;
typedef vector<vint> vvint;
typedef vector<string> vstr;

double v[1000];

int main()
{
    int totalCasos;
	cin >> totalCasos;
	forn(caso,totalCasos)
	{
        int N,K;
        cin >> N >> K;
        forn(i,N)
            cin >> v[i];
        double ret = 0.0;
        forn(mask,1<<N)
        if (__builtin_popcount(mask) == K)
        {
            double s = 0.0;
            for (int submask = mask; submask ; submask = ((submask - 1) & mask))
            if (__builtin_popcount(submask) == K/2)
            {
                double prod = 1.0;
                forn(j,N)
                if ((submask >> j) & 1)
                    prod *= v[j];
                else if ((mask >> j) & 1)
                    prod *= 1.0 - v[j];
                s += prod;
            }
            ret = max(ret, s);
        }
        
        printf("Case #%d: %.16lf\n", caso+1, ret);
	}
	return 0;
}
