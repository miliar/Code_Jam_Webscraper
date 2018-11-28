#include <iostream>
#include <vector>
#include <cmath>
#include <cstring>
#include <set>
#include <utility>
#include <algorithm>

using namespace std;

int main(){

	int T, N;
	cin >> T;
	for (int t = 1 ; t <= T ; t++){
		cin >> N;
		int p[N];
		int sum = 0;
		for (int n = 0 ; n < N; n++){
			cin >> p[n];
			sum += p[n];
		}		
		
		cout << "Case #" << t << ": ";
		while (sum > 0){
			int max, max_idx, second_max, second_max_idx;

			if(p[0] > p[1]) {
 				second_max = p[1];
				second_max_idx = 1;
				max = p[0];
				max_idx = 0;
			} else {
 				second_max = p[0];
				second_max_idx = 0;
 				max = p[1];
				max_idx = 1;
			}

			for(int i = 2; i < N; i++){
    				if(p[i] >= max){  
        				second_max=max;
					second_max_idx = max_idx;
        				max=p[i];
					max_idx = i;          
    				} else if(p[i] > second_max){
        				second_max=p[i];
					second_max_idx = i;
    				}
			}

			
			char c1 = 'A' + max_idx;
			char c2 = c1;
			cout << c1;	
			if (sum == 3) {
				
			} else if (sum == 2) {
				p[second_max_idx]--;
				c2 = 'A' + second_max_idx;
				cout << c2;
				sum--;
			} else if (p[second_max_idx] > (sum-1) / 2){
				p[second_max_idx]--;
				c2 = 'A' + second_max_idx;
				cout << c2;
				sum--;
			} else if (p[second_max_idx] > (sum-2) / 2) {
				p[second_max_idx]--;
				c2 = 'A' + second_max_idx;
				cout << c2;
				sum--;
			} else {
				p[max_idx]--;
				cout << c2;
				sum--;
			}
			p[max_idx]--;
			sum--;
			cout << " ";					
		}
		cout << endl;
	} 
	return 0;
}
