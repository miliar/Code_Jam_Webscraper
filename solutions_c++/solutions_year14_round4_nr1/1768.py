#include <iostream>
#include <algorithm>
using namespace std;

int N;
int discs[10000];

int main() {
	int T;
	cin >> T;

    for (int t = 1; t <= T; t++) {
        int N, X;
        cin >> N >> X;
        for (int i = 0; i < N; i++)
            cin >> discs[i];
        sort(discs, discs+N);
        int used = 0;
        for (int i = N-1; i >= used; i--) {
            if (i > used && discs[i] + discs[used] <= X) used++;
        }
        cout << "Case #" << t << ": " << N-used << '\n';
    }

	return 0;
}
