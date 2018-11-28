#include <iostream>
#include <fstream>
#define ll unsigned long long
using namespace std;

bool a[10], flag;

void check() {
	flag = true;
	for(int i = 0; i < 10; ++i) {
		if(a[i] == false) {
			flag = false;
		}
	}
}

void modify(ll num) {
	while(num) {
		a[num%10] = true;
		num /= 10;
	}
}

int main() {
	ofstream out_file;
	ifstream in_file;
	out_file.open("A_large_out.txt");
	in_file.open("A_large_in.txt");

	int T;
	//cin >> T;
	in_file >> T;

	for(int i = 1; i <= T; ++i) {
		ll N;
		//cin >> N;
		in_file >> N;

		if(N == 0) {
			//cout << "Case #" << i << ": INSOMNIA" << endl;
			out_file << "Case #" << i << ": INSOMNIA" << endl; 
		}
		else {
			ll temp = 0;
			flag = false;
			int k = 1;
			for(int j = 0; j < 10; ++j) {
				a[j] = false;
			}
			while(flag == false) {
				temp += N;
				modify(temp);
				check();
			}
			//cout << "Case #" << i << ": " << temp << endl;
			out_file << "Case #" << i << ": " << temp << endl;
		}
	}
	in_file.close();
	out_file.close();
	return 0;
}