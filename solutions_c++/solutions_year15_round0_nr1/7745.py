#include <bits/stdc++.h>

using namespace std;

typedef unsigned long long ull;
#define loop(i,a,b) for(int i=(a);i<ull(b);++i)
#define rep(i,n) loop(i,0,n)

const double eps = 1e-10;
const double pi  = acos(-1.0);
const double inf = (int)1e8;

int main(){
	int n;
	cin >> n;
	rep(_, n){
		int a; string b;
		cin >> a >> b;
		int count = 0;
		int ans = 0;
		rep(i, b.size()){
			if(i > count) {ans += i-count; count = i;}
			count += b[i]-'0';
		}
		cout << "Case #" << _+1 << ": ";
		cout << ans << endl;
	}
}
