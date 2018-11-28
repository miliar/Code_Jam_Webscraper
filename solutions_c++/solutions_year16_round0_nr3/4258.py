#include <iostream>
#include <fstream>
#include <stdio.h>
#include <vector>

using namespace std;

int main() {
	ifstream cin("C-small-attempt1.in");
	ofstream cout("C-small-attempt1.out");

//	



	long long int T;
	cin >> T;
	for (long long int t = 1; t <= T; t++){
		cout << "Case #" << t << ":\n";
		long long int N, J;
		cin >> N >> J;
		long long int m = 1 << (N - 2);
		for (long long int i = 0; i < m && J; i++){
			vector <long long int> a(9);
			long long int cen = i;
			vector<long long int> v;
			for (long long int j = 0; j < (N - 2); j++){
				if ((cen % 2) == 1){
					v.push_back(1);
				}
				else{
					v.push_back(0);
				}
				cen /= 2;
			}
			for (long long int base = 2; base <= 10; base++){
				cen = i;
				long long int num = 1;
				long long int g = base;
				for (long long int j = 0; j<(N-2); j++){
					if ( (cen % 2) == 1)
						num += g;
					cen /= 2;
					g *= base;
				}
				num += g;

//				cout << base << " " <<  num << endl;

				long long int quote = 0;
				for (long long int j = 2;  j*j <= num; j++){
					if (num%j == 0){
						quote = j;
						break;
					}
				}
				a[base - 2] = quote;
			}
			bool ok = true;
			for (long long int j = 0; j < 9; j++){
				if (a[j] == 0)
					ok = false;
			}
			if (ok){
				cout << "1";
				for (long long int i = v.size() - 1; i >= 0; i--)
					cout << v[i];
				cout << "1 ";
				for (long long int j = 0; j < 9; j++){
					cout << a[j] << " ";
				}
				J--;
				cout << "\n";
			}
		}

		
	
	}
	return 0;
}