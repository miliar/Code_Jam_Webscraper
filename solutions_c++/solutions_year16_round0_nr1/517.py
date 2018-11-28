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



int main()
{	int totalCasos;
	cin >> totalCasos;
	forn(caso,totalCasos)
	{
        tint N; cin >> N;
        ostringstream res;
        if (N == 0) res << "INSOMNIA";
        else
        {
            unsigned digits = 0;
            tint origN = N;
            while (true)
            {
                tint X = N;
                while (X != 0)
                {
                    digits |= (1<<(X%10));
                    X /= 10;
                }
                if (digits == 0x3FF) break;
                N += origN;
            }
            res << N;
        }
		cout << "Case #" << caso + 1 << ": " << res.str() << endl;
		cerr << "Case #" << caso + 1 << ": " << res.str() << endl;
	}
	return 0;
}
