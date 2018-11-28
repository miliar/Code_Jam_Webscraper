#include <bits/stdc++.h>
using namespace std;

int a[10] = {0};

void getInt(long long n) {
	while (n) {
		int k = n % 10;
		a[k] = 1;
		n /= 10;
	}
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	
	long long t, n;
	
	cin >> t;
	
	for (int i = 1; i <= t; ++i) {
		for (int j = 0; j < 10; ++j)
			a[j] = 0;
			
		cin >> n;
		long long sol = n;
		long long idx = 1;
		
		while (idx <= 111 * n) {
			int count = 0;
			getInt(sol);
		
			for (int j = 0; j < 10; ++j)
				if (a[j])
					++count;
				
			if (count == 10)
				break;
				
			++idx;
			sol += n;
		}
		
		if (idx <= 111 * n)
			cout << "Case #" << i << ": " << sol << "\n";
		else cout << "Case #" << i << ": INSOMNIA\n";
	}
	
	return 0;
}
