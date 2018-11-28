#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <iomanip>

using namespace std;

#define MAXN 10000002

int T;
double C, F, X;
double DN[MAXN];
bool vis[MAXN];
const double E = 1e-06;

double calc(int pos) {
	if (vis[pos]) 
		return DN[pos];
	vis[pos] = true;
	return DN[pos] = calc(pos - 1) + C / (2 + (pos - 1) * F);
}

void solve() {
	double val = X / 2.0;
	for (int i = 1; i < MAXN; i++) {
		double secs = calc(i);
		double sum = i * F + 2;
		double next = secs + (X / sum); 
		if (val - next > E) {
			val = next;
		}
	}
	cout << fixed << setprecision(7) << val << endl;
}

int main() {
	cin>>T;
	for(int i=0; i<T; i++){
		memset(vis, false, sizeof vis);
		cin >> C >> F >> X;
		cout << "Case #"<< (i+1) <<": ";
		vis[1] = true;
		DN[1] = C / 2.0;
		solve();
	}
	return 0;
}
