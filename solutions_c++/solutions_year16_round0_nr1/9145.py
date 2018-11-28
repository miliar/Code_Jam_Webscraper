#ifdef _MSC_VER
#define _CRT_SECURE_NO_WARNINGS
#endif
#include <memory.h>
#include <iostream>
#include <stdio.h>

using namespace std;

bool fr[10];

void check(long long n){

	int k = n;
	while (k != 0){
		int rem = k % 10;
		fr[rem] = 1;
		k /= 10;
	}

}

int main() {

	freopen("in.txt" , "r",stdin);
	freopen("out.txt", "w" , stdout);


	int n, t;

	cin >> t;

	t++;
	while (--t){
		cin >> n;
		if (n == 0){
			cout << "INSOMNIA\n";
			continue;
		}

		bool f = 0;
		int c = 1;
		long long m = n;
		memset(fr, 0, sizeof(fr));

		while (!f){
			check(m);
			m = n*c;
			c++;
			f = 1;
			for (int i = 0; i<10; i++){
				if (!fr[i]){
					f = 0;
					break;
				}
			}

		}

		cout << m - n << endl;

	}


	return 0;
}