#include <iostream>
#include <algorithm>

using namespace std;

int main(int argc, char** argv){

	int T;
	cin >> T;

	for(int t=1; t<=T; ++t){
		cout << "Case #" << t << ": ";

		int N,M;
		cin >> N >> M;

		int heights[M*N];

		for(int i=0; i < N*M; ++i){
			cin >> heights[i];
		}

		bool possible = true;

		for(int n = 0; n < N; ++n){
			for(int m = 0; m < M; ++m){
				int height = heights[m + n*M];

				bool row_possible = true;
				bool column_possible = true;

				for(int m2=0; m2<M; ++m2){
					int other_height = heights[m2 + n*M];
					if(height < other_height)
					{
						//cout << "row:" << n << endl;
						row_possible = false;
						break;
					}
				}

				for(int n2=0; n2<N; ++n2){
					int other_height = heights[m + n2*M];
					if(height < other_height)
					{
						//cout << "column:" << m << endl;
						column_possible = false;
						break;
					}
				}

				if(!column_possible && !row_possible){
					possible = false;
					break;
				}
			}
			if(!possible) break;
		}

		if(possible)
			cout << "YES" << endl;
		else 
			cout << "NO" << endl;
	}

	return 0;
}
