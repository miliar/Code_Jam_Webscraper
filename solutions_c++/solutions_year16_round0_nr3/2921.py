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
#define F(l,n) for (int l = 0; l < (int)(n); l++)

LL prime(LL x){
	LL d = 2;
	while (d < sqrt(x)){
		d+=1;
		if ((x%d) == 0)	
			return d;

	}
	return 1;
	
}
main(){

	FILE *fin = freopen("C-small.in", "r", stdin);
	assert (fin != NULL);
	
	FILE *fout = freopen("C-small.out", "w", stdout);
	
	int T, n = 16, cnt = 0, c = 0, cntp, cnt_mx=50;
	vector<vector<LL> > potegi(11,vector<LL>(n,1));
	vector<LL> dividors;
	LL pot, base, d;
	int pos;	
	//cin >> T;
	T = 1;
	for(int t = 1; t <= T; t++){
		//cout << "liczymy potegi " << endl;
		
		for (int i = 2; i <= 10; i++){
			pot = i;
			//cout << "potegi " << i << " : ";
			for(int j = 1; j < n; j++){
				//cout << pot << " ";
				potegi[i][j] = pot;
				pot *= i;
				

			}
			//cout << endl;

		}
		//cout << "obliczylismy potegi " << endl;
		int border = n;
		cout << "Case #" << t << ": " << endl;
		while (cnt < cnt_mx && border > 1){
			border--;
			for (int k = 1; k < border; k++){
				cntp = 9;
				dividors.clear();
				for (int b = 2; b <= 10; b++){
					base = potegi[b][0] + potegi[b][n-1] + potegi[b][k];						for (int m = border; m < n-1; m++){
						base += potegi[b][m];
					}
					d = prime(base);
					if (d == 1){

						//cout << k << " " << d << endl;
						//cntp--;
						break;
					}
					cntp--;
					dividors.push_back(d);


				}
				if (cntp == 0){
					cnt++;
					//cout << "cnt : " << cnt << endl;
				        cout << base << " ";
				        for (int f = 0; f < dividors.size(); f++){
						cout << dividors[f] << " ";
					}
					cout << endl;	

				}


			}
		}
		border = 3;
		while (cnt < cnt_mx && border < n-2){		
			for (int k = n-2; k > border; k--){
				cntp = 9;
				dividors.clear();
				for (int b = 2; b <= 10; b++){
					base = potegi[b][0] + potegi[b][n-1] + potegi[b][k];				
					for (int m = border; m > 0; m--){
						base += potegi[b][m];
					}
					d = prime(base);
					if (d == 1){

						//cout << k << " " << d << endl;
						//cntp--;
						break;
					}
					cntp--;
					dividors.push_back(d);


				}
				if (cntp == 0){
					cnt++;
					
					//cout << "cnt : " << cnt << endl;
					cout << base << " ";
				        for (int f = 0; f < dividors.size(); f++){
						cout << dividors[f] << " ";
					}
					cout << endl;	
					if (cnt == 50)
						break;

				}


			}
							
		}


		//cout << "Case #" << t << ": "<< cnt << endl;
		//for (int f = 0; f < )
		//cout << cnt << endl;
		//cout << 
	
	}
	exit(0);
}
