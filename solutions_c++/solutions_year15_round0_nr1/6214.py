#include <bits/stdc++.h>

long long inv = 301388891;
long long mod = 1000000007;
using namespace std;
#define pb push_back
#define mp make_pair
#define fs first
#define sc second
const int INF = (1 << 30);

long long modpow(int a, long long b, long long m) {
    a %= m;
    long long r = 1;
    while (b > 0) {
        if (b & 1) r = (r * 1LL * a) % m;
        a = (a * 1LL * a) % m;
        b >>= 1;
    }
    return r;
}

int main() {
	ios_base::sync_with_stdio(false); cin.tie(0);
	int t, sm;
	string s;
	cin>>t;
	for(int k = 1; k <= t; ++k){
		cin>>sm>>s;
		int answer = 0, sum = 0;
		if(s[0] == '0'){
			++answer;
			sum = 1;
		}
		else
			sum += int(s[0]) - 48;
		for(int i = 1; i<s.length(); ++i){
			if(i > sum){
				++answer;
				sum += (int(s[i]) - 48) + 1;
			}
			else
				sum += int(s[i]) - 48;
		}
		cout<<"Case #"<<k<<": "<<answer<<endl;
	}
	return 0;
}
