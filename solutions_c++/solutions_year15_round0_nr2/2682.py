#include <bits/stdc++.h>

using namespace std;

#define MAXN 100000

int A[MAXN];

int main(){
	int T;
	cin >> T;
	for(int caso = 1; caso <= T; caso++){
		printf("Case #%d: ", caso);
		int N;
		cin >> N;
		for(int i = 0; i < N; i++)
			cin >> A[i];
		int ans = 1 << 30;
		for(int i = 1000; i > 0; i--){
			int now = i;
			for(int j = 0; j < N; j++){
				if(A[j] > i){
					now += A[j] / i;
					if(A[j] % i == 0)
                        now--;
				}
			}
			ans = min(ans, now);
		}
		cout << ans << endl;
	}
	return 0;
}
