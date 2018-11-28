#include <bits/stdc++.h>

using namespace std;

int main(){
	freopen("in.in", "r", stdin);
	freopen("in.out", "w", stdout);

	int T;

	cin >> T;
	for (int tc = 1 ; tc <= T ; tc ++){
		int R, C, V;
		cin >> R >> C >> V;
		cout << "Case #"<< tc << ": " <<  R*(V + (C-V)/V + !!(C%V)) << endl;

	}
	return 0;
}
