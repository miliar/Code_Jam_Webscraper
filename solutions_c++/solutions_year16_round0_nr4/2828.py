#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
	int T;
	cin >> T;
	for(int T_i = 0; T_i < T; T_i++){
		int K, C, S;
		cin >> K >> C >> S;
		int total = (K+1) / 2;
		vector<int> target;
		cout << "Case #" << T_i + 1 << ": ";
		if(S < total){
			cout << "IMPOSSIBLE";
		}else{
			if(C == 1){
				if(S < K)
					cout << "IMPOSSIBLE";
				else
					for(int i = 0; i < K; i++)
						cout << i+1 << " ";

			}else{

				for(int i = 0; i < total - 1; i++){
					double D = 2*i*(K+1)+2;
					target.push_back(D);
				}
				target.push_back(K*(K-1));

				for(int i = 0; i < target.size(); i++){
					cout << target[i] << " ";
				}
			}	
		}
		cout << endl;
	}  
    return 0;
}
