#include <iostream>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;

int main(){
	int T;
	long long N;
	vector<int> digits(10);
	for(int i=0; i<10; i++){
		digits[i] = i;
	}

	cin >> T;

	for(int i=1; i<=T; i++){
		vector<int> seen;
		bool sleep = 1;
		long long N_it;

		cin >> N_it;

		N = N_it;
		for(int j=0; j<1000000; j++){
			sleep = 1;
			string N_s = to_string(N_it);
			//cout << N_it << " looping\n";

			for(int k=0; k<N_s.size(); k++){
				if(find(seen.begin(), seen.end(), (N_s[k]-'0')) == seen.end()){	
					seen.push_back(N_s[k] - '0');
					//cout << N_s[k] << " seen\n";
				}
			}

			for(int k=0; k<digits.size(); k++){
				if(find(seen.begin(), seen.end(), digits[k]) == seen.end()){
					sleep = 0;
					break;
				}
			}

			if(sleep){ 
				break; 
			}
			else{
				N_it = N * (j+2);
			}
		}

		if(sleep){
			printf("Case #%d: %lld\n", i, N_it);
		}
		else{
			printf("Case #%d: INSOMNIA\n", i);
		}
	}

	return 0;
}
