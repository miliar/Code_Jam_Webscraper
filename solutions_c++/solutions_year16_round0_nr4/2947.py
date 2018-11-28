#include <iostream>
#include <fstream>

using namespace std;

int main(){
	ifstream ii("D-small-attempt0.in");
	ofstream oo("os.out");
	int T;
	bool collect[10] = {false,false,false,false,false,false,false,false,false,false};
	ii >> T;
	int *K = new int[T];
	int *C = new int[T];
	int *S = new int[T];

	for (int i = 0;i < T;i++){
		ii >> K[i];
		ii >> C[i];
		ii >> S[i];
	}
	for (int i = 0; i < T;i++){
		if (S[i] < K[i] - C[i] +1){
			oo << "Case #" << i+1 << ": IMPOSSIBLE" << endl;
		}
		else {
			if (S[i] == K[i]){
				oo << "Case #" << i+1 << ": "  ;
				int j;
				for (j = 0;j<S[i]-1;j++){
					oo << j+1 << " ";
				}
				oo << j+1 << endl;
			}
		}
	}

}