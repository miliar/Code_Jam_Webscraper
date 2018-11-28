#include      <iostream>
#define endl '\n'
typedef long long ll;
using namespace std;

const int MY = 1;
const int NEED = 0;

#define UPD(MAX, IMAX, JMAX, ORD) \
		for (int i = 0; i < IMAX; i += 1) {\
			if (MAX[MY][i] > MAX[NEED][i]) {\
				for (int j = 0; j < JMAX; j += 1) anHave ORD = min(anHave ORD, MAX[NEED][i]);\
				MAX[MY][i] = MAX[NEED][i], bChanged = true;\
			}\
		}

bool solve() {
	int anState[101][101], N, M, anMaxH[2][101], anMaxW[2][101], anHave[101][101];
	cin >> N >> M;
	for (int i = 0; i < N; i += 1) for (int j = 0; j < M; j += 1) cin >> anState[i][j], anHave[i][j] = 100;
	for (int i = 0; i < N; i += 1) { anMaxW[NEED][i] = 0; anMaxW[MY][i] = 100; for (int j = 0; j < M; j += 1) anMaxW[NEED][i] = max(anMaxW[NEED][i], anState[i][j]); }
	for (int i = 0; i < M; i += 1) { anMaxH[NEED][i] = 0; anMaxH[MY][i] = 100; for (int j = 0; j < N; j += 1) anMaxH[NEED][i] = max(anMaxH[NEED][i], anState[j][i]); }

	bool bChanged = true;
	while (bChanged) {
		bChanged = false;
		UPD(anMaxW, N, M, [i][j]);
		UPD(anMaxH, M, N, [j][i]);
	}

	bool bOk = true;
	for (int i = 0; i < N; i += 1) for (int j = 0; j < M; j += 1) bOk = bOk && anHave[i][j] == anState[i][j];
	return bOk;
}

int main(int argc, char **argv) {
	ios_base::sync_with_stdio(false), cin.tie(0);
	int T;
	cin >> T;
	for (int t = 1; t <= T; t += 1) {
		cout << "Case #" << t << ": " << (solve() ? "YES" : "NO") << endl;
	}
	return 0;
}
