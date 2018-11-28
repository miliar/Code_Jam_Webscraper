#include<bits/stdc++.h>

using namespace std;

typedef pair<int, int> pii;
typedef long long int LL;
typedef vector<int> VI;

#define sd(x) scanf("%d", &x)
#define MP make_pair
#define PB push_back
#define F first
#define S second
#define MOD 1000000007
#define D double
#define LD long double
double EPS = 1e-12;

#define N 1123456

vector<LL> vec;
LL sum[N];
LL maxx[N], minx[N];
LL x[N];

int main(){
	freopen("B-large (1).in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t;
	sd(t);
	for(int cas = 1; cas <= t; cas++){
		int n, k, i;
		cin>>n>>k;
		for(i = 0; i < n - k + 1; i++){
			cin>>sum[i];
		}
		for(i = 0; i < k; i++){
			x[i] = 0;
			maxx[i] = 0;
			minx[i] = 0;
		}
		for(i = 0; i < n - k; i++){
			x[i + k] = x[i] + sum[i + 1] - sum[i];
		}
		for(i = k; i < n; i++){
			maxx[i % k] = max(x[i], maxx[i % k]);
			minx[i % k] = min(x[i], minx[i % k]);
		}
		LL mi = 1123456789;
		mi *= mi;
		LL ma = -mi;
		for(i = 0; i < k; i++){
			mi = min(mi, minx[i]);
			ma = max(ma, maxx[i]);
			//cout<<i<<" "<<minx[i]<<" "<<maxx[i]<<endl;
		}
		LL s = sum[0];
		vec.clear();
		for(i = 0; i < k; i++){
			s += minx[i] - mi;
			vec.PB(maxx[i] - minx[i]);
		}
		//cout<<s<<endl;
		sort(vec.begin(), vec.end());
		s %= k;
		s += k;
		s %= k;
		for(i = 0; i < k - 1; i++){
			s -= vec[k - 1] - vec[i];
		}
		LL ans = 0;
		if(s <= 0){
			ans = vec[k - 1];
		}
		else{
			ans = vec[k - 1] + 1;
		}
		printf("Case #%d: %lld\n", cas, ans);
		cerr << "Case #" << cas << ": Done!" << endl;
	}
	return 0;
}

