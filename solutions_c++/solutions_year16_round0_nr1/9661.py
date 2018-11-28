#include<iostream>
#include<cstdio>
using namespace std;

int n, cnt;
bool used[20];

void update(int x) {
	while (x > 0) {
		if (!used[x % 10]) {
			-- cnt;
			used[x % 10] = 1;
		}
		x /= 10;
	}
}

void solve() {
	cnt = 10;
	for (int i = 0; i <= 9; ++i) used[i] = 0;
	for (int i = n; 0 < 1; i = i += n) {
		update(i);
		if (cnt == 0) {
			cout<<i<<endl;
			return;
		}
	}
}

int main() {
	int T;
	cin>>T;
	for (int test = 1; test <= T; ++test) {
		cin>>n;
		printf("Case #%d: ", test);  
		if (n == 0) cout<<"INSOMNIA"<<endl;
		else solve();
	}
	return 0;
}