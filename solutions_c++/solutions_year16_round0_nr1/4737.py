#include <iostream>
#include <cstring>
using namespace std;

int tot,n,f[12];

void work(int a) {
	while (a) {
		if (f[a%10] == 0) tot++;
		f[a%10]=1;
		a/=10;
	}
}

int main() {
	//freopen("in.txt", "r", stdin);
	int T, cas = 1;
	cin >> T;
	while (T--) {
		cout << "Case #" << cas++ << ": ";
		cin >> n;
		if (n == 0) {
			cout << "INSOMNIA" << endl;
			continue;
		}
		memset(f, 0, sizeof(f));
		tot = 0;
		int tt = n;
		while (1) {
			work(n);
			if (tot >= 10) break;
			n+=tt;
		}
		cout << n << endl;
	}
	return 0;
}
