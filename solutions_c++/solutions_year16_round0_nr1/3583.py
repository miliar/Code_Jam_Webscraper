#include<iostream>
#include<cstring>

using namespace std;

typedef long long ll;

int main() {
	ios::sync_with_stdio(false);
	int t; cin >> t;
	for (int i = 1; i <= t; i++) {
		ll n; cin >> n;
		cout << "Case #" << i << ": ";
		if (n==0)	cout << "INSOMNIA\n";
		else 
		{
			bool seen[10];
			memset(seen,false,10*sizeof(bool));
			int count = 0;
			int mul = 0;
			while (count!=10) {
				mul++;
				ll n1 = n*mul;
				while(n1!=0) {
					if (!seen[n1%10]) {
						seen[n1%10] = true;
						count++;
					}
					n1 /= 10;
				}
			}
			cout << n*mul << "\n";
		}
	}
}
