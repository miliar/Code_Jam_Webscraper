#include <iostream>
#include <string.h>
typedef long long ll;
using namespace std;

int a[10], sum=0;
ll N;

ll last(ll Nu, int c)
{
	if (c == 1000) return -1;
	int Nc = Nu; int ch = 0;
	while (Nc)
	{
		if (a[Nc % 10] != 1) { a[Nc % 10] = 1; ch = 1; sum++; }
		Nc /= 10;
	}
	if (sum == 10) return Nu;
	if (ch == 1) return last(Nu + N, 0);
	return last(Nu + N, c + 1);
}

int main()
{
	ios::sync_with_stdio(false);
	int T; cin >> T;
	for (int t = 1; t <= T; t++)
	{
		memset(a, 0, sizeof(a));
		sum = 0;
		cin >> N;
		ll ans = -1;
		if (N!=0) ans=last(N, 0);
		cout << "Case #"<<t<<": ";
		if (ans != -1) cout << ans << endl;
		else cout << "INSOMNIA" << endl;
	}
	return 0;
}