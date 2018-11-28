#include <iostream>
#include <algorithm>
#include <list>
#include <cmath>
#include <vector>
#include <string>
#include <cstring>
#include <climits>
#include <cstdio>
#include <set>
#include <map>
using namespace std;

#define forn(a,n) for(int a = 0; a<(n); ++a)
#define forsn(a,s,n) for(int a = (s); a<(n); ++a)
#define forall(a,all) for(__typeof(all.begin()) a = all.begin(); a != all.end(); ++a)

typedef long long tint;

int T, arr[10004], used[10004];

int main(){
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	cin >> T;

	forn(t, T) {
		int n, x;
		cin >> n >> x;

		forn(i,n) cin >> arr[i];
		sort(arr,arr+n);
		memset(used, 0, sizeof(used));

		int ret = 0;

		for(int i = n-1; i>=0; --i) if(!used[i]){
			for(int j = i-1; j>=0; --j) if(!used[j]){
				if(arr[i]+arr[j] <= x) {
					used[j] = 1;
					break;
				}
			}
			used[i] = 1;
			ret++;
		}

		printf("Case #%i: %i\n", t+1, ret);

	}

	return 0;
}
