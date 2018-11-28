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

#define N (16)
#define J (50)
ll interpret(int num, int base)
{
    ll ret = 0LL;
    for (int i=N-1; i>=0; i--)
        ret = ret * base + (ll)((num >> i) & 1);
    return ret;
}

bool prime[(1<<20)+1];
vector<int> p;

ll firstDivisor(ll num) {
    int vs = p.size();
    for (int i=0; i<vs; i++) {
        if (num % p[i] == 0) {
            return p[i];
        }
    }
    return num;
}

int main()
{
#ifdef MICRO_LOCAL
	freopen("in.put", "r", stdin);
	clock_t timer_start = clock();
#endif
/*------------------------------------------------------------------------------------*/
    fill(prime, prime+(1<<20), true);
    prime[0] = prime[1] = 0;
    for (int i=2; i*i<(1<<20); i++) {
        if (prime[i]) {
            p.push_back(i);
            for (int j=i*i; j<(1<<20); j+=i)
                prime[j] = 0;
        }
    }
    puts("Case #1:");
    int cnt=0;
    ll temp[11];
    for (int i=(1<<(N-1))+1; i<(1<<N); i+=2) {
        bool f = 1;
        for (int b=2; b<=10; b++) {
            ll e = interpret(i, b), g;
            if ((g = firstDivisor(e)) != e) {
                temp[b] = g;
            }
            else {
                f = 0;
                break;
            }
        }
        if (f) {
            cnt++;
            int t = (1<<(N-1));
            while (t) {
                printf("%d", (i&t) ? 1 : 0);
                t>>=1;
            }
            printf(" ");
            for (int b=2; b<=10; b++) {
                printf("%lld ", temp[b]);
                //printf("%lld(%lld) ", temp[b], interpret(i, b));
            }
            printf("\n");
        }
        if (cnt >= J) {
            break;
        }
    }
/*------------------------------------------------------------------------------------*/
#ifdef MICRO_LOCAL
	printf("\nElapsed time : %.2lfms\n", ((double)clock() - (double)timer_start)/1000.0);
#endif
	return 0;
}
