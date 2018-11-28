#include <cstdio>
#include <iostream>
#define MAXN 1010
using namespace std;

int T;
int N;
char Ar[MAXN];

int main() {
	cin >> T;

	for(int t = 1; t <= T; t++){
		scanf("%d %s", &N, Ar);

		int res = 0;
		int sum = Ar[0] - '0';
		for(int i = 1; i <= N; i++){
			int val = Ar[i] - '0';
			if(sum < i){
				res += i - sum;
				sum += i - sum;
			}
			sum += val;
		}

		cout << "Case #" << t << ": " << res << endl;
	}

	return 0;
}
