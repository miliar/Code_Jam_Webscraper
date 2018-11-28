#include <iostream>

using namespace std;

int main() {
    int t;
    cin >> t;

    for (int z = 1; z <= t; z++) {
	int d;
	cin >> d;

	int a[d];
	for (int i = 0; i < d; i++)
	    cin >> a[i];

	int ans = 0x3f3f3f3f;
	for (int i = 1; i <= 1000; i++) {
	    int cur = 0;
	    for (int j = 0; j < d; j++)
		cur += (a[j] - 1)/i;
	    ans = min(ans, cur + i);
	}
	
	cout << "Case #" << z << ": " << ans << endl;
    }
}
