#include <string>
#include <iostream>
#include <vector>

using namespace std;


// key word : general harmonic progression ,  Digamma function
int main(){
	int T;
	int i,j,k;

	double C, F, X;

	cin >> T;

	for (i=1;i<=T;i++){
		cin >> C >> F >> X;

		double pre_time = 0;
		double time = X/2;

		for(j=1;;j++){
			pre_time = pre_time + C/(2 + (j-1) * F);
			if (time > pre_time + X/(2 + j*F)){
				time = pre_time + X/(2 + j*F);
			}else{
				break;
			}
		}

		std::cout.precision(7);

		cout << "Case #" << i <<": " << std::fixed << time << endl;
	}
}
