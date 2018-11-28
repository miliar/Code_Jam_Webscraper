#include <iostream>
#include <vector>
#include <string>
#include <math.h>

using namespace std;
#define M 10000000

typedef long long ll;

int arr[M];
ll base[9];

vector<int> primes;

int T;
int N;
int J;

void erat()
{
	for (int i=0; i<M; ++i) {
		arr[i] = 1;
	}

	for (int i=2; i<sqrt(M); ++i) {
		if (arr[i]) {
			primes.push_back(i);
//			cout << i << " ";
			for (int j=2; i*j <= M; ++j) {
				arr[i*j] = 0;
			}
		}
	}
}

int main()
{
	erat();

	cin >> T;
	cin >> N >> J;

	cout << "Case #1:" << endl;
	int n=0;
	for (int i=0; i<(1 << (N-2)); ++i) {

		for (int j=2; j<=10; ++j) {
			base[j-2] = 1;
		}

		string d("1");

		for (int j=N-2-1; j>=0; --j) {
			if (i & (1<<j)) {
				d.append(1,'1');
				for (int k=2; k<=10; ++k) {
					base[k-2] = base[k-2] * k + 1;
				}
			} else {
				d.append(1,'0');
				for (int k=2; k<=10; ++k) {
					base[k-2] = base[k-2] * k;
				}
			}
		}

		d.append(1, '1');
//		cout << d << endl;
		for (int k=2; k<=10; ++k) {
			base[k-2] = base[k-2] * k + 1;
//			cout << "Base " << k << ":" << base[k-2] << endl;
		}


		int cj=0;
		for (int j=2; j<=10; ++j) {
			for (auto it=primes.begin(); it!=primes.end() && *it < base[j-2]; ++it) {
				if ((base[j-2] % *it) == 0) {
//					cout << " = " << (*it) << " * " << (base[j-2] / *it) << endl;
					++cj;
					base[j-2] = *it;
					break;
				}
			}
		}

		if (cj == 9) {
			cout << d;
			for (int j=2; j<=10; ++j) {
				cout << " " << base[j-2];
			}
			cout << endl;

			++n;
		}
		if (n == J) break;
	}

	return 0;
}