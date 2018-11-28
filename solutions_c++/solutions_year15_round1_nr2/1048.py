#include <algorithm>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <iostream>
#include <sstream>
#include <functional>
#include <map>
#include <string>
#include <cstring>
#include <vector>
#include <queue>
#include <stack>
#include <deque>
#include <set>
#include <list>
#include <numeric>
using namespace std;
const double PI = 3.14159265358979323846;
const double EPS = 1e-12;
const int INF = 1<<25;
typedef long long ll;
typedef unsigned long long ull;
typedef pair<ll, ll> P;

ll B, N;
vector<ll> d;

ll ct(ll a){
	ll res = 0;
	for(int i = 0; i < B; i++) res += (d[i]+a-1)/d[i];
	return res;
}

int main(){
	int T;
	cin>>T;
	for(int Case = 1; Case <= T; Case++){
		cin>>B>>N;
		// N--;
		d = vector<ll>(B);
		for(int i = 0; i < B; i++) cin>>d[i];
		ll lb = 0, ub = 1e15;
		while(ub-lb>1){
			ll md = (ub+lb)/2;
			if(ct(md)<N) lb = md;
			else ub = md;
		}
		ll K = ct(lb), pos = ub, res;
		cerr<<lb<<" "<<K<<endl;
		for(int i = 0; i < B; i++){
			if(!((pos-1)%d[i])){
				K++;
				if(K==N){
					res = i+1;
					break;
				}
			}
		}
		printf("Case #%d: %ld\n", Case, res);
	}
	return 0;
}

