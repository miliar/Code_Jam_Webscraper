#include <iostream>
#include <vector>
#include <cstdio>
#include <algorithm>
#include <fstream>
#include <cstdint>
using namespace std;

int main()
{
	fstream f_in("A-large.in", fstream::in);
	fstream f_out("A-large.out", fstream::out);
	int n;
	f_in >> n;
	for (int i = 0; i < n; ++i){
		long long d;
		f_in >> d;
		if (d == 0){
			f_out << "Case #" << i + 1 << ": INSOMNIA\n";
			continue;
		}
		vector<bool> digits(10, false);
		long long j;
		for (j = 1;; ++j){
			long long temp = d * j;
			while (temp > 0){
				digits[temp % 10] = true;
				temp = temp / 10;
			}

			bool result = true;
			for (int k = 0; k < 10; ++k){
				if (digits[k] == false){
					result = false;
					break;
				}
			}
			if (result == true){
				f_out << "Case #" << i + 1 << ": " << j * d << "\n";
				break;
			}
		}
	}
	//f_out << "Case #" << i + 1 << ": INSOMNIA\n";
	
	system("pause");
	return 0;
}