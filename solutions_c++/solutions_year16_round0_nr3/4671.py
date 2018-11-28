// Author: Swarnaprakash
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <queue>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cctype>
#include <cassert>

using namespace std;

const int M = 105;
const int INF = 0x3f3f3f3f;
const bool debug = true;

#define SET(x,v)	memset(x,v,sizeof(x))
#define ALL(x) 		(x).begin() , (x).end()
#define SZ(x)		((int)((x).size()))
#define DB(x) 		if(debug) cout << #x << " : " << x <<endl;

typedef long long LL;
typedef vector < int >VI;
typedef vector < string > VS;
typedef vector < VI > VVI;
typedef pair < int, int >PII;
typedef pair < int, PII > PIII;

LL find_factor(LL n)
{
    if (n % 2 == 0)
	return 2;

    for (LL i = 3; (i * i) <= n; i += 2) {
	if (n % i == 0)
	    return i;
    }
    return -1;
}

LL find_factor(int mask, int base)
{
    LL n = 0;
    LL weight = 1;
    for (int i = 0; i < 16; ++i) {
	if (mask & (1 << i)) {
	    n += weight;
	}
	weight *= base;
    }

    return find_factor(n);
}

int main()
{
    puts("Case #1:");

    int printed = 0;
    for (int mask = 0; mask < (1 << 16); ++mask) {
	if (printed == 50) {
	    break;
	}

	if (!(mask & 1) || !(mask & (1 << 15)))
	    continue;

	LL factors[12];
	bool is_prime = false;
	for (int base = 2; base <= 10 && !is_prime; ++base) {
	    factors[base] = find_factor(mask, base);
	    is_prime = is_prime || (factors[base] == -1);
	}

	if (!is_prime) {
	    ++printed;
            for(int i = 15;i>=0;--i) {
                putchar ( (mask&(1<<i)) ? '1' : '0');
            }
            for(int base = 2 ;base <=10;++base) {
                printf(" %lld", factors[base]);
            }
            puts("");
	}
    }

    return 0;
}
