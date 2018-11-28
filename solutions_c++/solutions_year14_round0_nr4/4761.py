#include <iostream>
#include <algorithm>
using namespace std;

int dwar(float* Naomi, float* Ken, int& N) {
	int n = 0, points = 0;
	for (int ik = 0; ik < N; ik++)
		for (int in = n; in < N; in++) //{
			if (Naomi[in] > Ken[ik]) {
				n = in + 1;
				points++;
				break;
			} //else if (in == N-1) return points;
		//}
	return points;
}

int war(float* Naomi, float* Ken, int& N) {
	int in, ik, newik=0;
	float n;
	for (in = 0; in < N; in++) {
		n = Naomi[in];
		ik = newik;
		while (ik!=N && n>Ken[ik]) 	ik++;
		if (ik < N) 	newik = ik + 1;
		else			break;
	}	return N-in;
}

int main() {
	int T;	cin >> T;
	int N, i, point;
	float *Naomi, *Ken;
	for (int x = 1; x <= T; x++) {
		cin >> N;
		Naomi = new float[N];
		for (i = 0; i < N; i++)		cin >> Naomi[i];
		sort(Naomi, Naomi+N);
		Ken = new float[N];
		for (i = 0; i < N; i++) 	cin >> Ken[i];
		sort(Ken, Ken+N);
		cout << "Case #" << x << ": " << dwar(Naomi, Ken, N) << ' ' << war(Naomi, Ken, N) << endl;
	}
}
