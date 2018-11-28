#include <cstdio>
#include <iostream>
#include <stdlib.h>

using namespace std;

int N;
void solve(){

	freopen("ovation.in", "r", stdin);
	freopen("ovation.out", "w", stdout);
	fscanf(stdin, "%d", &N);
	for (int i = 0, K, count, ans; i < N; i++){
		int A[1010];
		for (int a = 0; a < 1010; a++){
			A[i] = 0;
		}
		fscanf(stdin, "%d", &K);
		char buffer[1010];
		fscanf(stdin, "%s", buffer);

		for (int j = 0; j <= K; j++){
			A[j] = buffer[j] - '0';
		}
		ans = count = 0;
		// for (int x = 0; x <= K; x++){
		// 	cout << A[x] << endl;

		// }
		//cout << "\n";
		for (int k = 0; k <= K; k++){
			if (count >= k){
				count += A[k];
			}
			else {
				ans += k - count;
				count = k + A[k];
			}

		}
		fprintf(stdout, "Case #%d: %d\n", i+1, ans);
	}

}

int main(){
	solve();
	return 0;
}