#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

long long reverse(long long k){
	long long revk = 0;
	int i = 1;
	while (k > 0){
		int t = k % 10;
		k = k / 10;
		revk = revk*10 + t;
		i++;
	}
	return revk;
}


int main(){
	


	long long k = 1;
	vector<long long> palins;
	while (k < pow(10.0,7)){

		long long r1 = reverse(k);

		if (r1 == k){
			long long k2 = pow(k,2.0);
			long long r2 = reverse(k2);
			if (r2 == k2){
				palins.push_back(k2);
			}
		}
		k++;
	}





	int t;
	cin >> t;

	for (int i=0; i<t; i++){


		int count = 0;
		int a, b;
		cin >> a >> b;

		int n = 0;
		while (palins[n] < a){
			n++;
		}

		while (palins[n] <= b){
			count++;
			n++;
		}

		cout << "Case #" << i+1 << ": " << count << '\n';

	}

	return 0;
}