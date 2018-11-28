//============================================================================
// Name        : .cpp
// Source      :
// Author      : Momen_Saeed
//============================================================================

#include <bits/stdc++.h>
using namespace std;

#define sz(v)			(int)(v.size())
#define mems(a , i)		memset(a , i , sizeof(a))
#define memc(a , b)		memcpy(a , b , sizeof(a));
#define mp(x , y)		make_pair(x , y)
#define pb(x)			push_back(x)
const double EPS = 1e-8;

int main() {
//#ifndef ONLINE_JUDGE
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
//#endif
	int t;
	cin >> t;
	for(int l = 1; l <= t ; l++){
		int n , m = 0;
		string s;
		cin >> n >> s;
		int sum = (s[0] - '0');
		for(int i = 1; i <= n ; i++){
			if(sum < i){
				m += i - sum;
				sum = i;
			}
			sum += (s[i] - '0');
		}
		printf("Case #%d: %d\n" , l , m);
	}
	return 0;
}















