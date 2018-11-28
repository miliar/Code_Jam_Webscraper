#include<iostream> 
#include<cstdio> 
#include<cmath> 
#include<algorithm>
#include<string>
#include<cstring>
#include<vector>
#include<set>
#include<map>
#include<ctime>
#include<cassert>
#include<queue>

#define LL long long
#define LD long double
#define mp make_pair
#define f first
#define s second
#define pii pair<int, int>
#define pb push_back

using namespace std;

int main() {
//	#ifdef DEBUG
	freopen("a.in", "r", stdin);
	freopen(".out", "w", stdout);
//    #endif

    int T;
    cin >> T;

    for (int test = 0; test < T; test++) {
    	LL r, cnt = 0;
    	LD t;
    	cin >> r >> t;
    	for (LL i = r; ; i += 2) {
    		t -= 2 * i + 1;
    		if (t < 0) 
				break;
    		else
    			cnt++;
    	}

    	printf("Case #%d: %I64d\n", test + 1, cnt);
    }

	return 0;
}