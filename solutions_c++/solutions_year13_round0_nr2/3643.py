//============================================================================
// Name        : GCJ2013_Q_2.cpp
// Author      :
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <set>

using namespace std;

#define MAX_N 100
#define MAX_M 100
#define LAWN_L 100

int lawn[MAX_N][MAX_M];

int trylawn[MAX_N][MAX_M];

int yoko[MAX_N];
int tate[MAX_M];

string solve(int n, int m){
//	cout << "n :" << n << endl;
//	cout << "m :" << m << endl;

	string ret = "YES";

	// yoko
	for(int j = 0; j < n; j++){
		for(int k = 0; k < m; k++){
			if(trylawn[j][k] > yoko[j]){
				trylawn[j][k] = yoko[j];
			}
		}
	}

	// tate
	for(int k = 0; k < m; k++){
		for(int j = 0; j < n; j++){
			if(trylawn[j][k] > tate[k]){
				trylawn[j][k] = tate[k];
			}
		}
	}

	// print
//	for(int j = 0; j < n; j++){
//		for(int k = 0; k < m; k++){
//			cout << lawn[j][k];
//		}
//		cout << endl;
//	}
//	cout << endl;
//	for(int j = 0; j < n; j++){
//		for(int k = 0; k < m; k++){
//			cout << trylawn[j][k];
//		}
//		cout << endl;
//	}


	// compare
	for(int j = 0; j < n; j++){
		for(int k = 0; k < m; k++){
			if(lawn[j][k] != trylawn[j][k]){
//				cout << "j :" << j << ", k :" << k << endl;
//				cout << "lawn :" << lawn[j][k] << ", try :" << trylawn[j][k] << endl;
				return "NO";
			}
		}
	}

	return ret;

}
int main() {
	int testcase_num = 0;
	std::cin >> testcase_num;


	for(int i = 0; i < testcase_num; ++i){
		int n, m;
		cin >> n;
		cin >> m;

		for(int l = 0;  l < MAX_N; l++){
			yoko[l] = 0;
		}
		for(int l = 0;  l < MAX_M; l++){
			tate[l] = 0;
		}

		for(int j = 0; j < n; j++){
			int max_yoko = 0;
			for(int k = 0; k < m; k++){
				cin >> lawn[j][k];

				if(max_yoko < lawn[j][k]){
					max_yoko = lawn[j][k];
				}
				trylawn[j][k] = LAWN_L;
			}

			yoko[j] = max_yoko;
//			cout << "yoko[" << j << "] = " << yoko[j] << endl;
		}

		for(int k = 0; k < m; k++){
			int max_tate = 0;
			for(int j = 0; j < n; j++){
				if(max_tate < lawn[j][k]){
					max_tate = lawn[j][k];
				}
			}
			tate[k] = max_tate;
//			cout << "tate[" << k << "] = " << tate[k] << endl;
		}

		string ans = solve(n,m);
		cout << "Case #" << i+1 << ": " << ans << endl;
	}

	return 0;
}
