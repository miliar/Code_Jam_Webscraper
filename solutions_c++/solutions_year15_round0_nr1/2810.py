#include <bits/stdc++.h>

using namespace std;

#define MAXN 100000

char A[MAXN];

int main(){
	int T;
	cin >> T;
	for(int caso = 1; caso <= T; caso++){
		printf("Case #%d: ", caso);
		int N;
		cin >> N >> A;
		int sum = 0;
		int ans = 0;
		for(int i = 0; i <= N; i++){
			if(sum < i){
				ans += i - sum;
				sum = i;
			}
			
			sum += A[i] - '0';
		}
		cout << ans << endl;
	}
	return 0;
}