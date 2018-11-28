#include<bits/stdc++.h>

using namespace std;

int main(){
	freopen("B-small-attempt0.in","r", stdin);
	freopen("outputB.out","w",stdout);
	int T, A, B, K;
	cin >> T;
	for (int i = 1; i <= T; i++){
		cin >> A >> B >> K;
		int res = 0;
		for (int j = 0; j < A; j++)
			for (int k = 0; k < B; k++){
				int temp = (j&k);
				if (temp < K) res++;
			}	
		cout << "Case #" << i << ": " << res << endl;
	}
	
}
