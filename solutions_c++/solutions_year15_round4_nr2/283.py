#include <bits/stdc++.h>
using namespace std;
const int N = 105;
int n;
long double V,X;
struct Node{
	long double r,c;
}a[N];

bool operator<(const Node & lhs,const Node& rhs){
	return lhs.c < rhs.c;
}

int sign(long double x){
	return (x < -1E-14) ? -1 : x > 1E-14;
}

#define INF 0x3f3f3f3f
const long double eps = 1e-11;
bool ok(long double t){
	long double has = 0;
	long double tot = 0;
	for(int i = 0; i < n; i++){
		if(sign(has + a[i].r * t - V) <= 0){
			has += a[i].r * t;
			tot += a[i].r * t * a[i].c;
		}else {
			tot += (V - has) * a[i].c;
			break;
		}
	}
	long double low = tot;
	has = 0, tot = 0;
	for(int i = n - 1; i >= 0; i--){
		if(sign(has + a[i].r * t - V) <= 0){
			has += a[i].r * t;
			tot += a[i].r * t * a[i].c;
		}else{
			tot += (V - has) * a[i].c;
			break;
		}
	}
	long double high = tot;
	if( sign(X * V - low) >= 0 && sign(X * V - high) <= 0)return true;
	return false;
}

void solve(){
	cin>>n>>V>>X;
	for(int i = 0; i < n; i++){
		cin>>a[i].r>>a[i].c;
	}
	sort(a,a+n);
	if(sign(a[n - 1].c - X) < 0 || sign(a[0].c - X) > 0){
		puts("IMPOSSIBLE");
		return;
	}
	long double low = 0, high = 1000000000.0; 
	while(low + eps < high){
		long double mid = (low + high) / 2.0;
		if(ok(mid))high = mid;
		else low = mid;
	}
	cout<<fixed<<setprecision(12)<<low<<endl;
}

int main(){
	int T;
	cin>>T;
	for(int cas = 0 ; cas < T; cas++){
		cout<<"Case #"<<cas+1<<": ";
		solve();
	}
	return 0;
}
