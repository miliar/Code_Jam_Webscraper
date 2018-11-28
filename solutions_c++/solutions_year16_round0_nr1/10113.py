#include <iostream>
using namespace std;

int main() {
	int a = 0;
	int *res = new int[1000001];
	for(int N = 0; N<=1000000; N++) {
		a = 0;
		int n = N;
		int count = 1;
		int prev ;
		bool ins = false;
		while(a != 0x3FF){
			prev = n;
			//cout << n<<endl;
			while(n && a != 0x3FF){
				int rem = n % 10;
				a = a | (1<<rem);
				n = n / 10;
			}
			count++;
			n = count*N;
			if(n == N){
				//cout << "INSOMNIA"<<endl;
				res[N] = -1;
				ins = true;
				break;
			}

		}
		if(!ins){
			res[N] = prev;
			//cout << prev<<endl;
		}

	}
	int t;
	int num;
	cin >> t;
	int i = 1;
	while(i<=t) {
		cin >> num;
		if(res[num] == -1) {
			cout << "Case #"<<i<<": INSOMNIA"<<endl;
		}
		else {
			cout << "Case #"<<i<<": "<<res[num]<<endl;
		}
		i++;
	}
	return 0;
}

