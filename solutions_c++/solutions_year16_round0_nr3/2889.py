#include <bits/stdc++.h>
using namespace std;
#define pb push_back
#define mp make_pair
#define ft first
#define sd second
#define mem(a, v) memset(a, v, sizeof(a))
#define PI 3.14159265358979323846
typedef long long ll;
typedef vector<int> VI;
typedef pair<int, int> PII;
typedef vector<VI> matrix;
const ll MOD = 1000000007LL;

int N, J;
vector<ll> ans;

ll convert(ll n, ll base)
{
	ll ret = 0, mul = 1;
	while(n){
		ll x = (n & 1LL);
		ret += x * mul;
		mul *= base;
		n /= 2;
	}
	return ret;
}

bool isOk(ll n)
{
	for(ll i=2; i*i*i <= n; i++){
		if(n % i == 0)
			return true;
	}
	return false;
}

ll fact(ll n)
{
	for(ll i=2; i*i*i <= n; i++){
		if(n % i == 0)
			return i;
	}
	assert(false);
	return 0;
}

bool check(ll n)
{
	bool flag = false;
	for(ll i = 2; i <= 10; i++){
		ll chk = convert(n, i);
		if(!isOk(chk)){
			flag = true;
		}
	}
	return (!flag);
}

void go(ll n, int idx, bool flag = false)
{
	if(idx >= N)
		return;
	if(ans.size() == J)
		return;
	if(flag && check(n)){
		ans.pb(n);
	}
	go(n, idx+1);
	go(n | (1 << idx), idx+1, true);
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for(int tc = 1; tc <= t; tc++){
		printf("Case #%d:\n", tc);
		scanf("%d %d", &N, &J);
		N--;
		ll n = 1;
		n |= (1LL << N);
		go(n, 1, true);
		for(int i=0; i<ans.size(); i++){
			ll cur = ans[i];
			//printf("%lld ", cur);
			for(int i=N; i>=0; i--){
				cout<<(bool)(cur & (1LL << i));
			}
			cout<<" ";
			for(int i=2; i<=10; i++){
				//printf("%lld %lld ", convert(cur, i), small[convert(cur, i)]);
				printf("%lld ", fact(convert(cur, i)));
			}
			printf("\n");
		}
		ans.clear();
	}	
	return 0;
}