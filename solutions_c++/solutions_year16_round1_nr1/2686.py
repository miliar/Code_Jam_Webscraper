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

const int M = 1005;
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

int main()
{
    int tc;
    scanf("%d", &tc);
    for (int t = 1; t <= tc; ++t) {

	char str[M];
	scanf("%s", str);

	deque < char >res;
	int len = strlen(str);
	for (int i = 0; i < len; ++i) {
	    if (i == 0) {
		res.push_back(str[i]);
		continue;
	    }

	    if (str[i] >= res[0]) {
		res.push_front(str[i]);
	    } else {
		res.push_back(str[i]);
	    }
	}
	printf("Case #%d: ", t);
	for (int i = 0; i < len; ++i)
	    putchar(res[i]);
	puts("");
    }
    return 0;
}
