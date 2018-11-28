#include <iostream>
#include <bitset>

using namespace std;

int main() {

	int T;
	long long N, temp, count;
	int digit = 0;
	bool stop = false;
	bitset<10> check;
		
	cin >> T;
	for(int i = 0; i<T; i++) {
		cin >> N;
		check.reset();
		cout << "Case #" << i+1 << ": ";
		if(N == 0)
			cout << "INSOMNIA" << endl;
	else {
			count = 0;
			stop = false;
			while (!stop) {
				count++;
				temp = N*count;
				while(1) {
					digit = temp%10;
					check[digit] = 1;
					temp/=10;
					if(temp == 0)
						break;
					
				}
				if(check.all())
					stop = true;
			}
			cout << count*N << endl;
		}
	}
	
	return 0;

}