#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <vector>
#include <cstring>
using namespace std;

int A, B, K;
void Input()
{
	cin >> A >> B >> K;
}

void Solve(int t)
{
	int cnt = 0;
	for (int k = 0; k < K; k++) {
		for (int i = 0; i < A; i++) {
			for (int j = 0; j < B; j++) {
				if ((i & j) == k) {
						cnt++;
						// cout << i << " " << j << " " << k  << endl;
				}
			}
		}
	}
	cout << "Case #" << t << ": " << cnt << endl;
}

int main()
{
	int T;
	cin>>T;
	for (int i = 1; i <= T; i++) {
		Input();
		Solve(i);
	}
	return 0;
}
