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


LL solve(LL n)
{
    int seen_count = 0;
    int seen[12];
    SET(seen, 0);

    LL running_n = 0;
    do {
	running_n += n;
	LL dup_n = running_n;

	while (dup_n > 0) {
	    int digit = dup_n % 10;
	    dup_n /= 10;
	    if (seen[digit] == 0) {
		seen[digit] = 1;
		seen_count++;
	    }
	}
    }
    while (seen_count < 10);


    return running_n;

}

int main()
{
    int tc;
    scanf("%d", &tc);

    for (int t = 1; t <= tc; ++t) {
	int n;
	scanf("%d", &n);
	printf("Case #%d: ", t);
	if (n == 0) {
	    puts("INSOMNIA");
	} else {
	    printf("%lld\n", solve(n));
	}

    }
    return 0;
}
