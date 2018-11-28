#include<iostream>
#include<stdlib.h>
using namespace std;
int main() {
	int n;
	cin >> n;
	for (int count = 1; count <= n; count++) {
		int a, b, k;
		int pair = 0;
		cin >> a;
		cin >> b;
		cin >> k;

		for (int i = 0; i < a; i++){
			for (int j = 0; j < b; j++) {
				if ((i & j) < k) {
					pair++;
				}
			}
		}
		cout << "Case #" << count << ":" << " " << pair << endl;
	}
	//system("pause");
}