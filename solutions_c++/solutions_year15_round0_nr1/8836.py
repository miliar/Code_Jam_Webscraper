#include <iostream>
#include <string>

using namespace std;

int main (){
	int n, t;
	n = t = 0;
	string inp;
	int crowd[1000];
	for(int i = 0; i < 1000; i++){
		crowd[i] = 0;
	}
	int sum_crowd[1000];
	cin >> n;

	for(int i = 1; i <= n; i++){
		cin >> t;
		//cout << t << endl;
		cin >> inp;
		for(int j = 0; j <= t; j++){
			crowd[j] = inp[j] - '0';
		}

		// for(int k = 0; k <= t; k++){
		// 	cout << crowd[k] << endl;
		// }
		int sum = 0;
		for(int j = 0; j <= t; j++){
			sum += crowd[j];
			sum_crowd[j] = sum;
		}

		// for(int j = 0; j <= t; j++){
		// 	cout << sum_crowd[j] << " ";
		// }
		// cout << endl;

		int atendee_to_add = 0;
		for(int j = 1; j <= t; j++){
			// cout << "scj-1 " << sum_crowd[j-1] << endl;
			if(sum_crowd[j-1] < j && crowd[j] > 0){	
				atendee_to_add += (j - sum_crowd[j-1]);
				for(int k = j; k <= t; k++){
					sum_crowd[k] += j - sum_crowd[j-1];
				}
				// cout << "Attend" << atendee_to_add << endl;
			}
		}

		// cout << "Case #" << i << ": " << atendee_to_add << endl;
		cout << "Case #" << i << ": " << atendee_to_add << "\n";
	}
	return 0;
}