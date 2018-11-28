#include <iostream>
#include <algorithm>

using namespace std;

int T;
int N, X;
int S[10000];

int main()
{
	cin >> T;
	for (int i = 1; i <= T; i++) {
		cin >> N;
		cin >> X;
		for (int j = 0; j < N; j++)
			cin >> S[j];

		sort(S, S+N);

		int p = 0;
		int q = N - 1;
		int count = 0;
		while (p < q) {
			if (S[p]+S[q] <= X) {
				count++;
				p++;
				q--;
			}
			else {
				count++;
				q--;
			}
		}
		if (p == q)
			count++;

		cout << "Case #" << i << ": " << count <<endl;
	}

}
