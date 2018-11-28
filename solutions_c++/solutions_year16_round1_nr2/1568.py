#include<iostream>
#include<fstream>
#include<string>
using namespace std;
int main(){
	ifstream cin("B-large (1).in");
	ofstream cout("out.out");
	int t, i, n, a[2501], x, o = 0;
	cin >> t;
	while (t--){
		o++;
		for (i = 1; i < 2501; i++){
			a[i] = 0;
		}
		cin >> n;
		for (i = 0; i < 2 * n * n - n; i++){
			cin >> x;
			a[x]++;
		}
		cout << "Case #" << o << ":";
		for (i = 1; i < 2501; i++){
			if (a[i] % 2){
				cout << " " << i;
			}
		}
		cout << endl;
	}
	return 0;
}