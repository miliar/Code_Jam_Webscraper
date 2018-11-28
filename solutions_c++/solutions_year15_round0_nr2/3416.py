#include <iostream>
#include <set>

using namespace std;

int T,D,n;
int c;
int a[2000];

int main() {
	freopen("B-large.in.txt", "r", stdin);
	freopen("Pancakes.out", "w", stdout);
	cin>>T;
	for (int sT = 1; sT <= T; sT++) {
		cin>>D;
		c = 0;
		for (int i = 0; i < D; i++) {
			cin>>a[i];
		}
		int res = 1000000000;
		int sum = 0;
		for (int c = 1; c <= 1000; c++) {
			sum = 0;
			for (int i = 0; i < D; i++) {
				sum += (a[i] - 1) / c;
			}
			res = min(res, sum + c);
		}

		cout<<"Case #"<<sT<<": "<<res<<endl;
	}
}