#include <bits/stdc++.h>
using namespace std; 

#define ALL(x) (x).begin(),(x).end() 

typedef long long ll;
const double eps = 1e-10;

int N;
string s;
int solve(){
	int p, u;
	for(int i = 0; i < s.size(); ++i) s[i] -= '0';
	p = 0;
	u = s[0];
	for(int i = 1; i <= N; ++i){
		if(u < i){
			p += i - u;
			u += i - u;
		}
		u += s[i];
	}
	return p;
}
int main(){
	int T;
	cin >> T;
	for(int t=1; t<=T; ++t){
		cin >> N >> s;
		cout << "Case #" << t << ": " << solve() << endl;
	}
	return 0;
}
