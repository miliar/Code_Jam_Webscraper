#include <map>
#include <set>
#include <cmath>
#include <stack>
#include <queue>
#include <string>
#include <vector>
#include <bitset>
#include <fstream>
#include <sstream>
#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <iostream>
#include <algorithm>
//#include <sys/time.h>
using namespace std;
#define li        long long int
#define rep(i,to) for(li i=0;i<((li)(to));++i)
#define pb        push_back
#define sz(v)     ((li)(v).size())
#define bit(n)    (1ll<<(li)(n))
#define all(vec)  (vec).begin(),(vec).end()
#define each(i,c) for(__typeof((c).begin()) i=(c).begin();i!=(c).end();i++)
#define MP        make_pair
#define F         first
#define S         second


#define MAX 37
li a[MAX];

int main()
{
	li T;
	cin >> T;
	rep(step, T){
		memset(a, 0, sizeof(a));
		li B, N;
		cin >> B >> N;
		rep(i, N) cin >> a[i];
		sort(a, a + MAX);
		
		double ans = 0;
		
		rep(use, MAX + 1)if(0 < use){
			li low = 0, high = bit(50);
			while(low + 1 < high){
				li mid = (low + high) >> 1;
				li spent = 0;
				double sum = 0;
				bool ok = true;
				rep(i, MAX){
					if(i < use){
						if(mid < a[i]) ok = false;
						spent += mid - a[i];
						sum += mid - a[i];
					}else{
						spent += max(0ll, (mid + 1) - a[i]);
					}
				}
				if(B < spent){
					high = mid;
				}else{
					low = mid;
					if(ok) ans = max(ans, sum * 36.0 / use - spent);
				}
			}
		}
		
		printf("Case #%lld: %0.20lf\n", step + 1, ans);
	}
	
}




