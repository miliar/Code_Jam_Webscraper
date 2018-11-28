#include <bits/stdc++.h>
#define rep(i,n) for(int i = 0; i < n; i++)
#define INF 100000000
#define EPS 1e-10
#define MOD 1000000007
using namespace std;
typedef pair<int,int> P;

long long n;
bool a[10];

void solve(){
	cin >> n;
	rep(i,10) a[i] = false;
	for(long long i = 1; i <= 100000000; i++){
		long long m = n*i;
		long long M = m;
		while(m){
			a[m%10] = true;
			m /= 10;
		}
		bool end = true;
		rep(j,10) if(!a[j]){
			end = false;
			break;
		}
		if(end){
			printf("%lld\n",M);
			return;
		}
	}
	puts("INSOMNIA");
}

int main(){
	int t;
	cin >> t;
	rep(i,t){
		printf("Case #%d: ",i+1);
		solve();
	}
}