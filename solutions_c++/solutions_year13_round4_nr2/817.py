
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
typedef pair<int,int> P;
typedef long long ll;
typedef unsigned long long ull;

ll worst(ll x, ll N){
	if(x==0 || N==0) return 0;
	else return (1LL<<(N-1))+worst((x-1)/2,N-1);
}

ll best(ll x, ll N){
	return (1LL<<N)-1-worst((1<<N)-1-x,N);
}


int main(){
	int T;
	cin>>T;
	//for(int i = 0; i < 1<<T; i++)cout<<worst(i,T)<<' '<<best(i,T)<<endl;
	//return 0;
	for(int Case = 1; Case <= T; Case++){
		ll N,P,ans1,ans2;
		cin>>N>>P;

		ll lb = 0, ub = 1LL<<N;
		while(ub-lb>1){
			ll md = (lb+ub)/2;
			if(worst(md,N)<P)lb = md;
			else ub = md;
		}
		ans1 = lb;

		lb = 0, ub = 1LL<<N;
		while(ub-lb>1){
			ll md = (lb+ub)/2;
			if(best(md,N)<P)lb = md;
			else ub = md;
		}
		ans2 = lb;
		printf("Case #%d: %lld %lld\n",Case,ans1,ans2);

	}
	return 0;
}

