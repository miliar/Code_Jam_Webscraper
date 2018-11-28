#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <iostream>
using namespace std;
typedef long long LL;

main() {
	/*FILE *fin = freopen("template.in", "r", stdin);
	assert( fin!=NULL );*/
	FILE *fout = freopen("Asmall.out", "w", stdout);
	int T;
	cin >> T;
	for(int t = 1; t <= T; t++){
		cout << "Case #" << t << ": ";
		int a[2];
		int b[2][16];
		for(int i = 0; i < 2; i++){
			cin >> a[i];
			for(int j = 0; j < 16; j++){
				cin >> b[i][j];
			}
		}
		int num = 0;
		int n = 0;
		for(int i = 1; i <= 16; i++){
			int k = 0;
			for(int c =0; c < 2; c++){
			for(int j = a[c]*4-4; j < a[c]*4; j++){
				if(b[c][j] == i){
					k++;
				}
			}
			if(k == 2){
				num++;
				n = i;
			}
			}

		}
		if(num == 0){
			cout << "Volunteer cheated!" << endl;
		} else if(num == 1){
			cout << n << endl;
		} else {
			cout << "Bad magician!" << endl;
		}
	}
	exit(0);
}