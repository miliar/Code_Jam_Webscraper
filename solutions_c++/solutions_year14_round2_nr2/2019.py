#include <iostream>

using namespace std;

void solve() {
	int A, B, K;
	 cin >> A >> B >> K;
	 int win = 0;
	 for (int i = 0; i < A; ++i)
	 {
	 	for (int j = 0; j < B; ++j)
	 	{
	 		int x = i & j;
	 		if(x < K) {
	 			win++;
	 		}
	 	}
	 }
	 cout << win;
}

int main()
{
	int T; cin >> T;
	for (int i = 1; i <= T; ++i)
	{
		cout << "Case #" << i << ": ";
		solve();
		cout << endl;
	}
	return 0;
}
