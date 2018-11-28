#include <iostream>
#include <algorithm>

#define MAXN 1010

using namespace std;

int N;
double Naomi[MAXN], Ken[MAXN];

int main()
{
	int i, n, k, t, T;
	int win_war, win_dwar;

	cin >> T;
	for (t = 1; t <= T; t++) {
		cin >> N;
		for (i = 0; i < N; i++)
			cin >> Naomi[i];
		for (i = 0; i < N; i++)
			cin >> Ken[i];
		sort(Naomi, Naomi + N);
		sort(Ken, Ken + N);

		n = 0;
		win_dwar = 0;
		for (k = 0; k < N; k++) {
			while (n < N && Naomi[n] < Ken[k]) n++;
			if (n == N) break;
			win_dwar++;
			n = n + 1;
		}

		k = 0;
		win_war = 0;
		for (n = 0; n < N; n++) {
			while (k < N && Ken[k] < Naomi[n]) k++;
			if (k == N) {
				win_war = N - n;
				break;
			}
			k = k + 1;
		}
		cout << "Case #" << t << ": " << win_dwar << " " << win_war << endl;
	}

	return 0;
}

