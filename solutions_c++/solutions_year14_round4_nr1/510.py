#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <queue>
#include <set>
#include <map>
#include <cmath>

using namespace std;

typedef long long ll;
typedef vector <ll> VI;
typedef vector <VI> VVI;
typedef vector <bool> VB;
typedef vector <VB> VVB;
typedef pair <ll, ll> PII;
typedef set <int> SI;
typedef map <int, int> MII;

int main(){
	int T;
	cin >> T;
	for (int t = 1; t <= T; ++t){
		int N, X;
		cin >> N >> X;
		VI v(N);
		for (int i = 0; i < N; ++i) cin >> v[i];
		sort(v.begin(), v.end());
		VB used(N, false);
		int end = N-1;
		int cont = 0;
		for (int i = 0; i < N; ++i){
			used[i] = true;
			while ((v[end] + v[i] > X or used[end]) and end >= 0) --end;
			if (end >= 0){
				 ++cont;
				 used[end] = true;
			}
		}
		cout << "Case " << "#" << t << ": " << N - cont << endl;
	}
}
