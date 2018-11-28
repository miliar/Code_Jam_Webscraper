#include <iostream>
#include <vector>
#include <algorithm>
#include <cctype>
#include <ctime>
#include <set>
#include <map>
using namespace std;
int cal (vector < vector <char> > arr,int p, int q, char c) {
	int cou = 0;
	for (int i = 0; i < 4; i++) {
		if (arr[i][q] == c || arr[i][q] == 'T') {
			cou++;
			if (cou == 4)
				return cou;
		}
		else
			break;
	}
	cou = 0;
	for (int i = 0; i < 4; i++) {
		if (arr[p][i] == c || arr[p][i] == 'T') {
			cou++;
			if (cou == 4)
				return cou;
		}
		else
			break;
	}
	cou = 0;
	if (p == q) {
		if ((arr[0][0] == c || arr[0][0] == 'T') && (arr[1][1] == c || arr[1][1] == 'T') && (arr[2][2] == c || arr[2][2] == 'T') && (arr[3][3] == c || arr[3][3] == 'T')) {
			cou = 4;
			return cou;
		}
	}
	if ((p == 1 && q==2) || (p==2 && q==1)) {
		if ((arr[3][0] == c || arr[3][0] == 'T') && (arr[2][1] == c || arr[2][1] == 'T') && (arr[1][2] == c || arr[1][2] == 'T') && (arr[0][3] == c || arr[0][3] == 'T')) {
			cou = 4;
			return cou;
		}
	}
	if ((p==3 && q == 0) || (p==0 && q==3)) {
		if ((arr[3][0] == c || arr[3][0] == 'T') && (arr[2][1] == c || arr[2][1] == 'T') && (arr[1][2] == c || arr[1][2] == 'T') && (arr[0][3] == c || arr[0][3] == 'T')) {
			cou = 4;
			return cou;
		}
	}
	return 0;
}

int main () {
	int t;
	cin >> t;
	for (int y = 1; y <= t; y++) {
		int emp = 0;
		int ansx = 0;
		int anso = 0;
		char x;
		vector < vector <char> > v (4,vector <char> (4,'c'));
		//vector < vector <bool> > s (4,vector <bool> (4,false));
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				cin >> x;
				v[i][j] = x;
			}
		}
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				if (v[i][j] == '.') {
					emp = 1;
				}
			//if (emp == 1)
				//break;
			if (v[i][j] == 'X') 
				ansx = cal (v,i,j,v[i][j]);
			if (v[i][j] == 'O')
				anso = cal (v,i,j,v[i][j]);
			}
			if (ansx == 4 || anso == 4)
				break;
			//if (emp == 1)
				//break;
		}
		if (ansx == 4)
			cout <<"Case #"<<y<<": "<< "X won" << endl;
		if (anso == 4)
			cout <<"Case #"<<y<<": "<< "O won" << endl;
		if (ansx != 4 && anso != 4) {
			if (emp == 1) {
				cout <<"Case #"<<y<<": "<<"Game has not completed" << endl;
			}
		}
		if (ansx != 4 && anso != 4) {
			if (emp == 0) {
				cout <<"Case #"<<y<<": "<< "Draw" << endl;
			}
		}

	}
	return 0;
}

