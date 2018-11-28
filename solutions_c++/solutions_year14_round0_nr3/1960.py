#include <iostream>
#include <fstream>
#include <cstdlib>
#include <cmath>
#include <cstdio>
#include <algorithm>
#include <vector>

#define ll long long
#define ld long double
#define vi vector<int>
#define vvi vector<vi>
#define vb vector<bool>

using namespace std;

const int dx[] = {-1, -1, -1, 0, 0, 1, 1, 1};
const int dy[] = {-1, 0, 1, 1, -1, -1, 0, 1};

int row[6];
bool otvet[5][5], ispolz[5][5], svobodn_kl[5][5];
int n, m, bomba;
bool nashli;

bool prov() {
	for(int i=0;i < n; i++)
		for(int j = 0;j < 5;j++){
			ispolz[i][j]=false;
			svobodn_kl[i][j]=false;
		}

	int cur_space = 0;
	for (int i = 0; i < n; i++) {
		cur_space += row[i];
		for (int j = 0; j < row[i]; j++) {
			svobodn_kl[i][j] = true;
			ispolz[i][j] = true;
		}
	}

	for (int i = 0; i < n; i++)
		for (int j = 0; j < m; j++)
			if (!ispolz[i][j]) {
				bool ok = false;
				for (int k = 0; k < 8; k++)
					if((i + dx[k]) < n && (j + dy[k]) < m && (i + dx[k]) > -1 && (j + dy[k]) > -1)
						if (ispolz[i + dx[k]][j + dy[k]]) ok = true;
				if (ok) {
					svobodn_kl[i][j] = true;
					cur_space++;
				}
			}
			if (cur_space == n * m - bomba) {
				for (int i = 0; i < n; i++)
					for (int j = 0; j < m; j++) otvet[i][j] = svobodn_kl[i][j];
				return true;
			}
			return false;
}

void rec(int dlin) {
	if (nashli) return;
	if (dlin == n - 1) {
		if (prov()) nashli = true;
		return;
	}
	for (int i = (dlin == 0) ? 1 : 0; i < m; i++) {
		row[dlin] = i;
		rec(dlin + 1);
		row[dlin] = 0;
	}
}

int main(){
	ifstream in("input.txt");
	ofstream out("output.txt");
	int t;
	in >> t;
	for(int qwe = 0;qwe < t;qwe++){
		out << "Case #" << (qwe + 1) << ": " << endl;
		in >> n >> m >> bomba;
		for(int i = 0;i < 5; i++){			
			for(int j = 0;j < 5;j++){
				otvet[i][j]=false;
			}
		}
		for(int i = 0;i < 5;i++)
			row[i]=0;
		if (bomba == n * m - 1) {
			for (int k = 0; k < n; k++) {
				for (int j = 0; j < m; j++)
					if (k == 0 && j == 0) 
						out << 'c';
					else out << '*';
					out << endl;
			}
			continue;
		}
		if (n == 1) {
			for (int k = 0; k < n * m - bomba; k++) 
				otvet[0][k] = true;
			for (int k = 0; k < n; k++) {
				for (int j = 0; j < m; j++) {
					if (k == 0 && j == 0) {
						out << 'c';
						continue;
					}
					if (otvet[k][j]) 
						out << '.';
					else out << '*';
				}
				out << endl;
			}
			continue;
		}
		if (m == 1) {
			for (int k = 0; k < n * m - bomba; k++) 
				otvet[k][0] = true;
			for (int k = 0; k < n; k++) {
				for (int j = 0; j < m; j++) {
					if (k == 0 && j == 0) {
						out << 'c';
						continue;
					}
					if (otvet[k][j]) 
						out << '.';
					else out << '*';
				}
				out << endl;
			}
			continue;
		}
		nashli = false;
		rec(0);
		if (!nashli) {
			out << "Impossible" << endl;
			continue;
		}
		for (int k = 0; k < n; k++) {
			for (int j = 0; j < m; j++) {
				if (k == 0 && j == 0) {
					out << 'c';
					continue;
				}
				if (otvet[k][j]) 
					out << '.';
				else out << '*';
			}
			out << endl;
		}
	}
	return 0;
}