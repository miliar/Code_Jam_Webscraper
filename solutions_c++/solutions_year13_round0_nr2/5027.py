#include <iostream>

using namespace std;

int main(){
	int K;
	cin >> K;
	for(int k = 0; k< K; k++){
		cout << "Case #" << k+1 << ": ";
		bool done = false;
		long N,M;
		cin >> N >> M;
		int pattern[N][M];
		for(int n =0; n < N; ++n){
			for (int m = 0; m < M; ++m)
			{
				cin >> pattern[n][m];
			}
		}


		for(int n =0; n < N; ++n){
			if(done) break;
			for (int m = 0; m < M; ++m)
			{
				bool row = true;
				bool col = true;
				int val = pattern[n][m];
				//check row
				for(int r = 0; r < M; r++){
					if(pattern[n][r] > val){
						row = false;
						break;
					}
				}

				//check col
				for(int c = 0; c < N; c++){
					if(pattern[c][m] > val){
						col = false;
						break;
					}
				}


				//check for no heighers on x and y
				if(!row && !col){
					cout << "NO" << endl;
					done = true;
					break;
				}
			}
		}
		if(done) continue;
		cout << "YES" << endl;
	}
}