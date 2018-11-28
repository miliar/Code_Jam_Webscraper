#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <math.h>
using namespace std;
typedef unsigned long long LL;
#define F(l,n) for (int l = 0; l < (int)(n); l++)


main(){

	FILE *fin = freopen("D-small.in", "r", stdin);
	assert (fin != NULL);
	
	FILE *fout = freopen("D-small.out", "w", stdout);
	
	int T, k, c, s;
	long long tmp;
	cin >> T;
	for(int t = 1; t <= T; t++){
		cin >> k;
		cin >> c;
		cin >> s;
		//cout << k <<endl;
		//cout << c << endl;
		//cout << s << endl;
		tmp = 1;
		F(i,c-1){
			tmp*=k;
		}
		//cout << tmp << endl;

		cout << "Case #" << t << ": ";
		if (s < k){
			cout << "IMPOSSIBLE";
		}
		else
		F(i,k){
			cout << tmp*i + 1 << " ";
	
		}	
		cout << endl;
		
	
	}
	exit(0);
}
