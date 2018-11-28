#include <bits/stdc++.h>
using namespace std;

#define mp(x , y) make_pair(x , y)
#define f first
#define s second

map<pair<long long , long long> , int > vst;

int Solve(long long a , long long b){
	if(a == 1){
		for(int i = 0 ; i <= 40 ; ++i){
			if((1LL << i) == b)return i;
		}
		return 1000000000;
	}

	if(vst.count(mp(a , b)))return vst[mp(a , b)];

	int res = 1000000000;
	for(int i = 1 ; i < a ; ++i){
		long long A = i;
		long long B = a - A;
		res = min(res , Solve(A / __gcd(A , b / 2) , (b / 2) / __gcd(A , b / 2)) + 1);
		res = min(res , Solve(B / __gcd(B , (b / 2)), (b / 2) / __gcd(B , b / 2)) + 1);
	}

	return (vst[mp(a , b)] = res);
}

int main() {
	freopen("A-small-attempt1.in","r",stdin);
	freopen("output.in","w",stdout);
	int T;
	int k = 1;
	cin >> T;
	while(T--){
		string res;
		long long p , q;
		char c;
		cin >> p >> c >> q;

		long long g = __gcd(p , q);
		p /= g;
		q /= g;

		bool find = 0;
		for(int i = 0 ; i <= 40 ; ++i){
			if((1LL << i) == q)find = 1;
		}
		if(!find || p % 2 == 0){
			res = "impossible";
			cout << "Case #" << k << ": " << res << endl;
			++k;
			continue;
		}

		int go = Solve(p , q);
		if(go == 1000000000){
			res = "impossible";
			cout << "Case #" << k << ": " << res << endl;
			++k;
		}
		else{
			cout << "Case #" << k << ": " << go << endl;
			++k;
		}
	}
	return 0;
}
