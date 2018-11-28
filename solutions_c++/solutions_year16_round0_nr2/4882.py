#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <climits>
#include <cfloat>
#include <cmath>
#include <algorithm>
#include <vector>
#include <stack>
#include <set>
#include <queue>
#include <deque>
#include <string>
#include <map>
#include <functional>
#include <cassert>
#include <ctime>
using namespace std;
typedef long long ll;
typedef pair<int,int> pr;

int main()
{
#ifdef MICRO_LOCAL
	freopen("in.put", "r", stdin);
	clock_t timer_start = clock();
#endif
/*------------------------------------------------------------------------------------*/
    int T;
    scanf("%d", &T);
    for (int tc=1; tc<=T; tc++) {
        char s[111],last;
        int len,ans=0;
        scanf("%s", s);
        len = strlen(s);
        if (s[0] == '-') {
            last = '-';
        //    ans++;
        }
        else {
            last = '+';
        }

        for (int i=1; i<len; i++) {
            if (s[i] != last) {
                last = s[i];
                ans++;
            }
        }
        if (last == '-') ans++;
        printf("Case #%d: %d\n", tc, ans);
    }
/*------------------------------------------------------------------------------------*/
#ifdef MICRO_LOCAL
	printf("\nElapsed time : %.2lfms\n", ((double)clock() - (double)timer_start)/1000.0);
#endif
	return 0;
}
