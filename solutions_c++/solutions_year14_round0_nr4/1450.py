#include <iostream>
#include <algorithm>
#include <iomanip>
using namespace std;

#define MAX_BLOCK 1000

int T, nCase = 1;
double n[MAX_BLOCK], k[MAX_BLOCK];
int N;

void input()
{
	cin >> N;
	for (int i=0;i<N;++i) 
		cin >> n[i];
	for (int i=0;i<N;++i) 
		cin >> k[i];
}

int ansD, ansW;

void solve()
{
	sort(n, n+N);
	reverse(n, n+N);
	sort(k, k+N);
	reverse(k, k+N);
	ansD = ansW = 0;
	
	int hn=0, hk=0, cnt = 0;
	while (hn < N && hk < N) {
		if (n[hn] > k[hk]) ++cnt, ++hn;
		else --cnt, ++hk;
		if (cnt>ansW) ansW = cnt;
	}
	hn=0, hk=0;
	int tn=N-1, tk=N-1;
	for (int i=0;i<N;++i) {
		if (n[tn] > k[tk]) { ++ ansD, --tn, --tk; }
		else { --tn, ++hk; }
	}
	
}

int main()
{
	cin >> T;
	while (T--) {
		input();
		solve();
		cout << "Case #" << nCase ++ << ": " << ansD << " " << ansW << endl;
	}
	return 0;
}