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
    scanf("%d",&T);
    for (int test_case=1; test_case<=T; test_case++) {
        bool u[10]={0,};
        int n;
        scanf("%d", &n);
        printf("Case #%d: ", test_case);
        bool f = 1;
        for (int i=1; i<123; i++) {
            f = 1;
            int nn = n*i;
            while (nn) {
                u[nn % 10] = true;
                nn /= 10;
            }
            for (int j=0; j<10; j++) {
                if (u[j] == false) {
                    f = 0;
                    break;
                }
            }
            if (f) {
                printf("%d\n", n*i);
                break;
            }
        }
        if (!f)
            puts("INSOMNIA");
    }
/*------------------------------------------------------------------------------------*/
#ifdef MICRO_LOCAL
	printf("\nElapsed time : %.2lfms\n", ((double)clock() - (double)timer_start)/1000.0);
#endif
	return 0;
}
