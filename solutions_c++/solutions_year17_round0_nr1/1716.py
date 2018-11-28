#include <bits/stdc++.h>
#define pb push_back
#define mp make_pair
#define int64 long long int
using namespace std;


void solve (int T)
{
	string S;
	int k, ans = 0, f = true;
	cin >> S >> k;
	for (int i = 0; i < S.size (); i++) {
		if (S[i] == '+') continue;
		if (i + k - 1 >= S.size ()) continue;
		for (int j = i; j < i + k; j++) {
			if (S[j] == '-') S[j] = '+';
			else S[j] = '-';
		}
		ans++;
	}
	for (int i = 0; i < S.size (); i++) {
		if (S[i] == '-') {
			f = false;
			break;
		}
	}
	printf ("Case #%d: ", T);
	if (!f) {
		puts ("IMPOSSIBLE");
		return;
	}
	printf ("%d\n", ans);
}		
int main ()
{
	int t;
	scanf ("%d", &t);
	for (int i = 1; i <= t; i++) solve (i);
	return 0;
}
