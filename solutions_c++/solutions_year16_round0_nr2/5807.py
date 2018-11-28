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

char s[M];

int flips(int pos)
{
    if (pos == -1)
	return 0;
    if (s[pos] == '+')
	return flips(pos - 1);

    for (int i = 0; i <= pos; ++i) {
	char flipped = (s[i] == '+' ? '-' : '+');
	s[i] = flipped;
    }
    return 1 + flips(pos - 1);

}

int main()
{
    int tc;
    scanf("%d", &tc);
    for (int t = 1; t <= tc; ++t) {
	scanf("%s", s);
	int len = strlen(s);
	printf("Case #%d: %d\n", t, flips(len - 1));
    }
    return 0;
}
