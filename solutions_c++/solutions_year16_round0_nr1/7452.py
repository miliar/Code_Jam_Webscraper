#include <iostream>
using namespace std;

int main() {
	int t;
	cin >> t;
	long long n;
	for (int i = 1; i <= t; i++) {
	    cin >> n;
	    if (n == 0) {
	        cout << "Case #" << i << ": INSOMNIA" << endl;
	        continue;
	    }
	    int flag = 0;
	    int j = 1;
	    long long mid = n;
	    while ((flag & 1023) != 1023) {
	        long long temp = mid;
	        while (temp != 0) {
	            int num = 1 << (temp%10);
	            flag = flag | num;
	            temp = temp/10;
	        }
	        if ((flag & 1023) == 1023) {
	            break;
	        }
	        j++;
	        mid = j*n; 
	    }
	    cout << "Case #" << i << ": " << mid << endl;
	}
	return 0;
}
