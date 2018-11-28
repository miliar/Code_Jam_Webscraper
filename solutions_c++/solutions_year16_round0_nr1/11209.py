#include<bits/stdc++.h>
#define LL long long
using namespace std;
bool check(LL Num){return (((1 << 10) - 1 == Num) || Num == 0);}
int main() {
	int tc; cin >> tc;
	for(int cs = 1; cs <= tc; cs++) {
		LL Num = 0, step = 0, N = 0;
		cin >> N;
		do {
			step++;
			N = (N / max(1LL,step-1)) * (step);
			LL tmp = N;
			while (tmp) {
				Num |= (1 << ((tmp)%10));
				tmp /= 10;
			}
		} while (!check(Num));
		cout << "Case #" << cs << ": " << ((N == 0) ? "INSOMNIA" : to_string(N)) << endl;
	}
}
