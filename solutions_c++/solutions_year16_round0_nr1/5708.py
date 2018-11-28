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


int main(){
	int T;

	cin >> T;
	for(int caseNum=1; caseNum<=T; caseNum++){
		int N, ans=0;
		cin >> N;

		if( N == 0 ){
			printf("Case #%d: INSOMNIA\n", caseNum );
			continue;
		}

		bool f[10]={};
		int count = 0;
		for(int i=1; i<=100; i++){
			for(int tmp = i*N; tmp > 0; tmp/=10){
				if( f[ tmp % 10 ] == false){
					f[ tmp % 10 ] = true;
					count++;
				}
			}
			if(count>=10){
				ans = i*N;
				break;
			}
		}

		printf("Case #%d: %d\n", caseNum, ans );
	}

	return 0;
}
