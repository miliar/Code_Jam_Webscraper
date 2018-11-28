#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main(){
	int t, n, x, a;
	cin >> t;
	for (int i=0; i<t; ++i) {
		vector<bool> A(10, false);
		bool flag = false;
		cin >> n;
		if (!n) {
			cout << "Case #"<< (i+1) <<": INSOMNIA\n";
			continue;
 			flag = true;
		}
		int j;
		for (j = 1; (!flag); ++j) {
			a = n*j;
			while(a) {
				x = a%10;
				a = (int)(a/10);
				A[x] = true;
			}
			int f = true;
			for (int k=0; k<10; ++k) {
				f = f*A[k];
		//		cout << A[k] <<" ";
			}
			flag = f;
		}
		cout << "Case #"<< (i+1) <<": " << n * (j-1) <<endl;
	}
	return 0;
}