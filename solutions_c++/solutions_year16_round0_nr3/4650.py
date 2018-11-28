#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <algorithm>

#define rep(i,n) for(int i=0; i<(n); i++)
#define rrep(i,n) for(int i=(n)-1; i>=0; i--)
#define all(X) (X).begin(),(X).end()

using namespace std;
typedef long long int ll;
typedef pair<int,int> P;

template<class T> bool chmax(T &a, const T &b) { if (a<b) { a=b; return 1; } return 0; }
template<class T> bool chmin(T &a, const T &b) { if (a>b) { a=b; return 1; } return 0; }

template<class A, size_t N, class T> void Fill(A (&a)[N], const T &v){ fill( (T*)a, (T*)(a+N), v ); }

const int INF = 0x3fffffff;


vector<int> primes;
ll prime[100000008]={};
int main(){
	int T;

	for(ll i=2; i<1000008; i++){
		if( prime[i] == 0 ){
			for(ll j=i; j<1000008; j+=i){
				prime[j] = i;
				primes.push_back(i);
			}
		}
	}

	cin >> T;
	for(int caseNum=1; caseNum<=T; caseNum++){
		int N, J, ans=0;
		cin >> N >> J;

		printf("Case #%d:\n", caseNum );

		ll co = (1<<(N-1)) + 1;
		for(; co<(1<<N); co+=2){
			bool sure=true;
			ll out[11] = {};
			for(int i=2; i<=10 && sure; i++){
				ll tmp = 0, k=1;
				for(ll tc=co; tc>0; tc>>=1){
					tmp += k * (tc%2);
					k*=i;
				}
				for(auto t: primes){
					if( tmp % t == 0 && tmp / t > 1 ){
						out[i] = t;
						break;
					}
				}
				if( out[i] == 0 ) sure = false;
			}
			if( sure ){
				vector<int> o;
				for(ll tc=co; tc>0; tc>>=1){
					o.push_back(tc%2);
				}
				for(int i=o.size()-1; i>=0; i--){
					cout << o[i];
				}
				for(int i=2; i<=10; i++){
					cout << " " << out[i];
				}
				cout << endl;
				ans++;
				if(ans>=J) break;
			}
		}
	}

	return 0;
}
