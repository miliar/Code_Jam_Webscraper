
#include <iostream>
#include <stdio.h>
#include <math.h>
#include <vector>
using namespace std;


int main() {
	freopen("in.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int c;
	long long r, t;
	cin >> c;
	for(int a = 1; a <= c; a++){
		cin >> r >> t;
		long long res = 0;
		for(long long i = r + 1;; i += 2){
			long long tmp = (i * i) - ((i - 1) * (i - 1));
			t -= tmp;
			if(t < 0){
				break;
			}
			res++;
		}
		cout << "Case #" << a << ": " << res << endl;
	}
	return 0;
}

