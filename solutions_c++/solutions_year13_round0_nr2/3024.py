#include <iostream>
using namespace std;

bool check(int **lawn, int n, int m);
void doCase(int caseN);

int main() {
	int cases;
	cin>>cases;
	for(int i = 0; i < cases; i++) {
		doCase(i+1);
	}
}

void doCase(int caseN) {
	int n;
	int m;
	cin >> n;
	cin >> m;
	int **lawn = new int*[n];
	for (int i = 0; i < n; i++)
		lawn[i] = new int[m];
	for(int i = 0; i < n; i++) {
		for(int j = 0; j < m; j++) {
			cin >> lawn[i][j];
		}
	}
	cout << "Case #" << caseN << ": ";
	if(check(lawn, n, m)) {
		cout<< "YES\n";
	} else {
		cout<< "NO\n";
	}
}

bool row(int i, int m, int **lawn, int max) {
	for(int j = 0; j<m; j++) {
		if(lawn[i][j] > max) return true;
	}
	return false;
}

bool col (int j, int n, int **lawn, int max) {
	for(int i = 0; i<n; i++) {
		if(lawn[i][j] > max) return true;
	}
	return false;
}

bool check(int **lawn, int n, int m) {
	for(int i = 0; i < n; i++) {
		for(int j = 0; j < m; j++) {
			int check = 0;
			if(row(i,m,lawn,lawn[i][j])) check++;
			if(col(j,n,lawn,lawn[i][j])) check++;
			if(check==2) return false;
		}
	}
	return true;
}