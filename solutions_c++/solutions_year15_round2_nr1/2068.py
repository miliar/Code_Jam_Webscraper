/* attention to overflow */
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <cstdio>
#include <queue>
#include <sstream>
#include <set>
#include <map>
#include <cmath>
#include <numeric>
#include <tuple>
#include <iomanip>

#define dump(x) cerr<< #x << " = " << x <<endl
#define ALL(container) (container).begin(),(container).end()

using namespace std;
const int INF = 1 << 25;
void io() { cin.tie(0); ios::sync_with_stdio(false);}
template <class S,class T> ostream& operator<<(ostream& os, const pair <S,T> &s){return os<<'('<<s.first<<','<<s.second<<')';}
/*printf("%.9Lf\n",cf);*/
const int MOD = 1000000007;
const double EPS=1e-8;

int dp[10001000];

int main() {
	io();
	int T;
	cin>>T;

	for(int i=0;i<10000100;i++){
		dp[i]=i;
	}

	for(int i=1;i<1000100;i++){
		//if(i%1000000==0) cout<<i<<endl;
		dp[i+1]=min(dp[i+1],dp[i]+1);
		string t=to_string(i);
		reverse(t.begin(),t.end());
		long long tmp=stoll(t);
		dp[tmp]=min(dp[tmp],dp[i]+1);
	}

	for(int t=0;t<T;t++){
		long long s;
		cin>>s;
		cout<<"Case #"<<t+1<<": "<<dp[s]<<endl;
	}

	return 0;
}