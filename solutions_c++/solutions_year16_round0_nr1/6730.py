#include <iostream>
#include <vector>
using namespace std;

int main() {
	// your code goes here
	long long int t;
	cin>>t;
	
	for (long long int i = 1; i <= t; i++) {
	//cout<<t<<endl;
		long long int n; cin>>n;
		vector<bool> digits(false);
		long long int counter = 1;
		if (n == 0) {
			cout << "Case #"<<i<<": INSOMNIA"<<endl;
		} else {
			long long int x = n;
			
			while (true) {
				//cout<<"counter is "<<counter<<endl;
				//cout<<"x is "<<x<<endl;
				long long int z = x * counter;
				//cout<<"z before is "<<z<<endl;

			   	while (z > 0) {
			   		long long int y = z % 10;
			   		digits[y] = true;
			   		z = z / 10;
			   	}
			   	//cout<<"z is "<<z<<endl;
			   	bool complete = true;
			   	for (int q = 0; q < 10; q++) {
			   		if (digits[q] == true) {
			   			continue;
			   		} else {
			   			complete = false;
			   			break;
			   		}
			   	}
			   	if (complete == true) {
			   		cout<<"Case #"<<i<<": "<<(x*counter)<<endl;
			   		break;
			   	} else {
			   		counter++;
			   	}
			}
		}
	}
	return 0;
}