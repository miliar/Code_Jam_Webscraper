#include <iostream>
#include <iomanip>
#include <algorithm>
using namespace std;

struct source {
	long long rate;
	long long temp;
};

bool operator<(source a, source b) {
	return a.temp < b.temp;
}

source sources[100];

inline long long inputdumb() {
	long long before, after;
	char c;

	cin >> before >> c >> after;
	return before * 10000 + after;
}

int main() {
	int T;
	cin >> T;

	cout << setprecision(15);

	for (int t = 1; t <= T; t++) {
		int N;
		long long V, X;

		cin >> N;
		V = inputdumb();
		X = inputdumb();

		long long totalrate = 0, totalheat = 0;
		for (int i = 0; i < N; i++) {
			sources[i].rate = inputdumb();
			sources[i].temp = inputdumb();

			totalrate += sources[i].rate;
			totalheat += sources[i].rate * sources[i].temp;
		}
		sort(sources, sources+N); 

		cout << "Case #" << t << ": ";

		if (sources[0].temp > X || sources[N-1].temp < X) {
			cout << "IMPOSSIBLE\n";
		} else if (totalheat > totalrate * X) {
			long long rate = 0, heat = 0;

			for (int i = 0; i < N; i++) {
				if ((heat+sources[i].rate*sources[i].temp) <= (rate+sources[i].rate)*X) {
					rate += sources[i].rate;
					heat += sources[i].rate*sources[i].temp;
					continue;
				}

				cout << double(V)/(double(X*rate-heat)/double(sources[i].temp-X) + double(rate)) << '\n';
				break;
			}
		} else if (totalheat < totalrate * X) {
			long long rate = 0, heat = 0;

			for (int i = N-1; i >= 0; i--) {
				if ((heat+sources[i].rate*sources[i].temp) >= (rate+sources[i].rate)*X) {
					rate += sources[i].rate;
					heat += sources[i].rate*sources[i].temp;
					continue;
				}

				cout << double(V)/(double(X*rate-heat)/double(sources[i].temp-X) + double(rate)) << '\n';
				break;
			}
		} else {
			cout << double(V)/double(totalrate) << '\n';
		}
	}

	return 0;
}
