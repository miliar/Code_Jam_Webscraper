#include <cstdio>
#include <iostream>

using namespace std;
typedef long long ll;

void solve()
{
    string t;
    cin >> t;
    string s = "";
    s += t[0];
    for (int i = 1; i < t.length(); ++i) {
        if (s[0] <= t[i]) s = t[i] + s;
        else s = s + t[i];
    }
    cout << s << endl;
}

int main()
{
	int t;
	cin >> t;
	for(int i = 1; i <= t; ++i) {
		cout << "Case #" << i << ": ";
		solve();
	}

	return 0;
}
