#include <iostream>
using namespace std;

typedef long long int lld;

lld pow(int n, int k){
	if(k == 0)
		return 1;
	else if(k == 1)
		return n;
	return pow(n, k/2) * pow(n, k/2 + k%2);
}

int main(){
	int n;
	cin >> n;
	for(int t=0; t < n; t++){
		int K, C, S;
		cin >> K >> C >> S;
		cout << "Case #" << t+1 << ":";
		lld size = (lld) pow(K, C);
		for(lld i=0; i < size; i+=size/K){
			cout << " " << i+1;
		}
		cout << endl;

	}
}
