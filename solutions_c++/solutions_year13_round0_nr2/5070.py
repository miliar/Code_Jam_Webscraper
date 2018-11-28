#include<iostream>
#include<fstream>
#include<string>

using namespace std;

int mp[111][111], hh[111][111];
int m, n;

int min()
{
	int i, j;
	int mm = 100;
	for (i=1; i<=n; i++)
		for (j=1; j<=m; j++) if (mp[i][j]<mm) mm=mp[i][j];
	return mm;
}

int main(){
	int i, j, k, a, b, c, t, tt, res;
	bool fd;
	int max1, max2;
	ifstream fin("B-large.in");
	ofstream fout("out.txt");
	fin >> tt;
	for (t=1; t<=tt; t++){
		fin >> n >> m;
		for (i=1; i<=n; i++)
			for (j=1; j<=m; j++) {
				fin >> mp[i][j];
				hh[i][j]=100;
			}
		while (1){
			fd = false;
			for (i=1; i<=n; i++) {
				max1 = max2 = -100;
				for (j=1; j<=m; j++) {
					if (max1 <mp[i][j]) max1 = mp[i][j];
					if (max2 <hh[i][j]) max2 = hh[i][j];
				}
				if (max2 > max1) {
					fd = true;
					for (j=1; j<=m; j++) hh[i][j] = max1;
				}
			}
			for (i=1; i<=m; i++) {
				max1 = max2 = -100;
				for (j=1; j<=n; j++) {
					if (max1 <mp[j][i]) max1 = mp[j][i];
					if (max2 <hh[j][i]) max2 = hh[j][i];
				}
				if (max2 > max1) {
					fd = true;
					for (j=1; j<=n; j++) hh[j][i] = max1;
				}
			}
			if (!fd) break;
		}
		for (i=1; i<=n; i++)
			for (j=1; j<=m;j ++) if (mp[i][j]!=hh[i][j]) {
				fd = true;
				break;
			}
		if (!fd) fout << "Case #" << t << ": YES" << endl;
		else fout << "Case #" << t << ": NO" << endl;
	}
}