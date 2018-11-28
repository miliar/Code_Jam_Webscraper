#include <iostream>

using namespace std;

int check(int n) {
	if(n==0) return 0;
	int digits = 0x0000;
	int result = 0;
	int mod = 0;
	int d = 0;
	while(digits != 0x03FF) {
		result += n;
		mod = result;
		while(mod>0) {
			d = mod % 10;
			mod /= 10;
			digits |= 1 << d;
		}
	}
	return result;
}

int main() {
  int t, n, result;
  
  cin >> t;
  for (int i = 1; i <= t; ++i) {
    cin >> n;
    result = check(n);
    cout << "Case #" << i << ": ";
    if(result==0) {
    	cout << "INSOMNIA" << endl;
   	} else {
			cout << result << endl;
   	}
  }
  
  return 0;
}

