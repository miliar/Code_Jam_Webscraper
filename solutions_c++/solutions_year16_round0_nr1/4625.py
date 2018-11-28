#include "iostream"
#include "stdio.h"
#include "vector"
#include "queue"
#include "algorithm"
#define MAXN 100005
using namespace std;

int main() {
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int T;
	cin >> T;
	for (int cst = 1; cst <= T; cst++) {
		cout << "Case #" << cst << ": ";
		int x;
		cin >> x;
		int digit[12] = {};
		for (int i = 1; i <= 101; i++) {
			int mul = x * i;
			while (mul != 0) {
				digit[mul % 10] = 1;
				mul = mul / 10;
			}
			int tmp = 1;
			for (int i = 0; i < 10; i++) {
				if (digit[i] == 0) {
					tmp = 0;
					break;
				}
			}
			if (tmp == 1) {
				cout << x * i << endl;
				break;
			}
			if (i == 101) {
				cout << "INSOMNIA" << endl;
			}
		}

	}	
}