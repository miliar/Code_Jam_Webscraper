#include <iostream>

#define ll long

using namespace std;

int main()
{
	int N;
	cin >> N;
	for (int i = 0; i < N; ++i)
	{
		ll r, t;
		cin >> r >> t;

		ll wr = r;
		ll ans = 0;
		while(true) {
			ll need = (wr+1)*(wr+1) - wr*wr;
			t -= need;
			if( t < 0 ) break;
			ans ++;
			wr += 2;
		}
		cout << "Case #" << i+1 << ": " << ans << endl;
	}
	return 0;
}