#include<iostream>
using namespace std;

void solve();

int squares[1000];


bool is_palindrome(int num) {
	int rev = 0;
	int tmp = num;
	while (tmp != 0) {
		rev = rev * 10;
		rev += tmp % 10;
		tmp = tmp / 10;
	}
	if (rev == num) return true;
	else return false;
}

int main() {

	for (int i = 0; i <= 1000; i++) {
		if (is_palindrome(i)) {		
			squares[i] = i*i;
		}
		else {
			squares[i] = -1;
		}
	}
	//cout << "\n";
	
	int n;
	cin >> n;
	int t = 1;
	while (n--) {
		cout << "Case #" << t << ": ";
		solve();
		t++;
	}
	return 0;
}


bool is_square(int num) {
	for (int i=0; i<1000; i++) {
		if (squares[i] == num) return true;
		if (squares[i] > num) return false;
	}
	return false;
}

void solve() {
	int a, b;
	cin >> a >> b;
	
	int count = 0;
	for (int i = a; i <= b; i++) {
		if (is_palindrome(i) && is_square(i)) {
			count ++;
			//cout << "$" << i << "$" << endl;
		}
	}
	cout << count << "\n";
	
	return;
}
