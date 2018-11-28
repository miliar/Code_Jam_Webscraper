#include <iostream>

using namespace std;

int main(){
  int T = 0;
  cin >> T;

  for(int t = 0; t < T; ++t){
		int N = 0;
		int ON = 0;
		int ans = 0;
		bool empty[10];
		int number_of_digits = 0;

		for(int i = 0; i < 10; ++i){
			empty[i] = true;
		}

		cin >> ON;
		N = ON;

		if(N == 0){
			cout << "Case #" << (t+1) << ": " << "INSOMNIA" << endl;
			continue;
		}

		int i = 1;
		while(number_of_digits != 10){
			N = (i++) * ON;
			int NN = N;
			while(NN != 0){
				int d = NN % 10;
				NN /= 10;

				if(empty[d]){
					empty[d] = false;
					++number_of_digits;
				}
			}
			ans = N;
		}
		cout << "Case #" << (t+1) << ": " << ans << endl;
  }
}

