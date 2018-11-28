#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main(){

	int NSteps;
	cin >> NSteps;

	for(int t=1; t<=NSteps; t++){
		cout << "Case #" << t << ": ";
		int A, B, K;
		cin >> A >> B >> K;
		int nSolutions = 0; 
		for(int i=0; i<K; i++){
			for(int j=0; j<A; j++){
				for(int k=0; k<B; k++){
					//cout << j << " " << k << " = "<< (j&k) << " - "  << i << endl;
					if((j & k) == i){
						nSolutions++;
					//	cout << "Solution!" << endl;
					}
				}
			}
		}
		cout << nSolutions << endl;

	}
}
