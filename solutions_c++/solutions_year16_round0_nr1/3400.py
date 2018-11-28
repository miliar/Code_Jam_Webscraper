#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <math.h>
using namespace std;
typedef long long LL;
#define F(i,n) for (int i = 0; i < (int)(n); i++)
main(){

	FILE *fin = freopen("A-large.in", "r", stdin);
	assert (fin != NULL);
	//cout << "A open ";
	FILE *fout = freopen("A-large.out", "w", stdout);
	//cout << "A created";
	int T, r, cnt = 0, k = 1;
	LL n, tmp;	
	vector<int> used(10,0);

	
	cin >> T;
	//cout << "Test cases: " << T;
	for(int t = 1; t <= T; t++){
		cin >> n;
		//cout << "start: " << n << endl;
		F(i,10)
			used[i] = 0;
		cnt = 0;

		if (n == 0){	
			cout << "Case #" << t << ": ";
			cout << "INSOMNIA" << endl;
			continue;
		}
		k = 1;
		while (cnt < 10){
			tmp = k * n;
			k++;
			//n = k * n;
			while (tmp > 0){
				r = tmp%10;
				if (!used[r]){
					cnt++;
					used[r] = 1;
				}
				tmp = tmp/10;	

			}
			//cout << n * (k-1) << " " << cnt << endl;

		}
				

		//cout << "Case #" << t << " (" << n <<" ): ";
		cout << "Case #" << t << ": ";
		cout << n*(k-1) << endl;
			


	}
	exit(0);
}
