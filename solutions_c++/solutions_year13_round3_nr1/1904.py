#include <inttypes.h>
#include <sys/types.h>
#include <algorithm>
#include <bitset>
#include <cassert>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <iterator>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>

using namespace std;

#define ST first
#define ND second
#define MP make_pair
#define PB push_back

#define fabsl __builtin_fabsl
#define atan2l __builtin_atan2l
#define cosl __builtin_cosl
#define sinl __builtin_sinl
#define sqrtl __builtin_sqrtl

template<class T>
void splitstr(const string &s, vector<T> &out)
{
    istringstream in(s);
    out.clear();
    copy(istream_iterator<T>(in), istream_iterator<T>(), back_inserter(out));
}

typedef uint64_t LL;
typedef long double LD;
typedef uint64_t D;
typedef pair<int, int> PII;
typedef vector<string> VS;
typedef vector<int> VI;
typedef vector<PII> VII;
typedef vector<VI> VVI;

#define REP(i,n) for(int i=0;i<(n);i++)
#define FOR(i,a,b) for(VAR(i,a);i<=(b);++i)
#define FORD(i,a,b) for(VAR(i,a);i>=(b);--i)
#define FORE(a,b) for(VAR(a,(b).begin());a!=(b).end();++a)
#define VAR(a,b) __typeof(b) a=(b)
#define SIZE(a) ((int)((a).size()))
#define ALL(x) (x).begin(),(x).end()
#define CLR(x,a) memset(x,a,sizeof(x))
#define ZERO(x) memset(x,0,sizeof(x))
#define MAX(a,b) ((a)>(b)?(a):(b))
#define MIN(a,b) ((a)<(b)?(a):(b))
#define ABS(a,b) ((a)>(b)?(a-b):(b-a))

#ifndef DEBUG
#define DEBUG 0
#endif

bool is_vowel(char c)
{
    return (c == 'a' || c == 'e' || c == 'i' ||
    c == 'o' || c == 'u');
}

int main ()
{
    int T;
    cin >> T;
    for (int tt = 0; tt < T; tt++) {
        int n;
        char name[1000000+2];
        char aux[1000000+2];
        cin >> name >> n;
        int64_t sol = 0;
        int len = strlen(name);
        //cout << name << " " << n << endl;
        int lastpos = 0;
        REP(i, len)
        {
            int countcon = 0;
            for (int j = i; j < len; j++)
            {
                if (!is_vowel(name[j]))
                {
                    countcon++;
                    if (countcon == n)
                        break;
                }
                else break;
            }
            if (countcon < n)
                continue;

            int pos = i - lastpos;
            //cout << i << " " << pos << " " << len-pos-n+1 << endl;
            sol += ((int64_t)(pos + 1))*((int64_t)(len-i-n+1));
            lastpos = i + 1;


                /*
                ZERO(aux);
                memcpy(aux, name + i, j);
                if (j != strlen(aux))
                {
                    cout << aux << endl;
                    return 1;
                }

                int countcon = 0;
                REP(k, j)
                {
                    if (!is_vowel(aux[k]))
                    {
                        countcon++;
                        if (countcon == n)
                        {
                            sol++;
                            //cout << aux << endl;
                            goto next;
                        }
                    }
                    else
                    {
                        countcon = 0;
                    }
                }
next:
                if (false) cout << aux << endl;
                //continue;
                */

        }

        //cout.precision(0);
        cout << "Case #" << tt+1 << ": " << sol << endl;
    }
    return 0;
}


