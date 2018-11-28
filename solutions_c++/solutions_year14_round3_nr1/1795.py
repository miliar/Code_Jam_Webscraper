# include <iostream>
# include <string>
# include <cmath>

using namespace std;

int main(){
	int num_cases,P,Q;
	char slash;
	cin >> num_cases;
	for(int i = 1; i <= num_cases; i++){
		cin >> P >> slash >> Q;
		double logq = log2(Q);
		if(logq - floor(logq) != 0){
			cout << "Case #" << i << ": impossible\n";
		} else{
			double logp = log2(P); 
			cout << "Case #" << i << ": " << (int)(logq - floor(logp)) << endl;
		}
	}
	return 0;
}
