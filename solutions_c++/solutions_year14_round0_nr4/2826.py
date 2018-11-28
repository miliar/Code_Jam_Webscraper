#include <iostream>
#include <algorithm>

using namespace std;

int T;
int N;
double n[1000];
double k[1000];
int main()
{
	cin >> T;
	for (int i = 1; i <= T; i++) {
		int d = 0;
		int w = 0;
		cin >> N;
		for (int j = 0; j < N; j++)
			cin >> n[j];
		for (int j = 0; j < N; j++)
			cin >> k[j];

		sort(n, n+N);
		sort(k, k+N);

		int p = 0;
		int q = 0;
		while (q < N) {
			if (k[q] < n[p]) {
				w++;
				q++;
			}
			else {
				q++;
				p++;
			}
				
		}


		p = 0;
		q = 0;
		while (p < N) {
			if (n[p] < k[q]) {
				d++;
				p++;
			}
			else {
				q++;
				p++;
			}
				
		}
		cout << "Case #" << i << ": " << N - d << " " <<  w << endl;
	}

}
