#include <iostream>
#include <vector>
#include <math.h> 

using namespace std;

typedef long long longInt;

int main(){
	//Input
	int T;
	cin >> T;
	vector<int> K(T);
	vector<int> C(T);
	vector<int> S(T);
	for(int i=0;i<T;i++){
		cin >> K[i] >> C[i] >> S[i];
	}

	//Output
	for(int i=0;i<T;i++){
		cout << "Case #" << i+1 << ": ";
		for(int j=1;j<K[i];j++){
			cout << j << " ";
		}
		cout << K[i] << endl;
	}

	return 0;
}