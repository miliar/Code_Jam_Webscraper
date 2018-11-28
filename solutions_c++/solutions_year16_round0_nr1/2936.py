#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <string>
#include <cstring>
#include <queue>
#include <map>
#include <stack>

using namespace std;

long long n;
int a[10];

void parse() {
	cin >> n;
}

void solve() {
	if (n == 0){
		cout << "INSOMNIA"	<< endl;
		return ;
	}

	memset(a, 0, sizeof(a));
	int sum = 0;
	long long tmp;
	long long m = n;
	while (1){
		tmp = m;
		while (tmp){
			if (!a[tmp % 10]){
				sum ++;
				a[tmp % 10] = 1;
			}
			tmp /= 10;
		}
		if (sum == 10){
			cout << m << endl;
			return ;
		}
		m += n;
	}
}

/*
void test(){
	for (int i = 0; i <= 100; i++){
		cout << "Case i = " << i <<"  : ";
		n = i;
		solve();
	}
}
*/


int main() {
	int T;
	cin >> T;

	for (int i = 1; i <= T; i++){
		parse();
		cout << "Case #" << i << ": ";
		solve();
	}
	return 0;
}
