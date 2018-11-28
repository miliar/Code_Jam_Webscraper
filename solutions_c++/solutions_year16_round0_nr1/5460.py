#include<iostream>
#include<cstring>
using namespace std;
long long t[20], T, N;
int main(){
	cin >> T;
	for (long long i = 0; i < T; ++i) {
		cin >> N;
		cout << "Case #" << i+1 << ": ";
		if (i==0) {
			cout << "INSOMNIA";
		} else {
			memset(t, 0, sizeof(t));
			bool found = false;
			long long cnt = 0;
			long long f = 0;
			while (!found) {
				++cnt;
				long long n = cnt * N;

		//		cout << endl << cnt << "==" << n << "     ";
				while (n>0) {
					long long c = n%10;
					n = n/10;
					if (t[c] == 0) f++;
					t[c]=1;
				};
		//		cout << f;
				if (f==10) found = true;
			};
			long long ret = cnt * N;
			cout << ret;
		};
		cout << endl;
	};
};
