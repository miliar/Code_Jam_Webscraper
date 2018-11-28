#include <iostream>
using namespace std;

int main() {
	long T, n;
	cin>>T;
	for (long ti = 1; ti <= T; ti++) {
		cout<<"Case #"<<ti<<": ";
		cin>>n;
		if (n == 0) {
			cout<<"INSOMNIA"<<endl;
			continue;
		}
		bool digitsFound[10] = {false};
		long f = -1;
		int leftCount = 10;
		
		do {
			f++;
			long m = f * n;

			while (m) {
				int c = m % 10;
				if (!digitsFound[c]) {
					digitsFound[c] = true;
					leftCount--;
				}
				m /= 10;
			}

		} while(leftCount);

		cout<<(f*n)<<endl;
	}

	return 0;
}