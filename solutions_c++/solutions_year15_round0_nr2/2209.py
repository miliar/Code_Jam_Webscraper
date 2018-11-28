#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main() {
	ifstream fin("B-large.in");
	ofstream fout("output.txt");
	int n, m;
	fin >> n;
	int a[10000];
	for (int i=0; i<n; i++) {
		fin >> m;
		int max = 0;
		for (int j=0; j<m; j++)  {
			fin >> a[j];
			if (a[j] > max) max = a[j];
		}
		int ans = 10000;
		for (int j=1; j<=max; j++) {
			int now = 0;
			for (int k=0; k<m; k++)
				if (a[k]%j==0) now += a[k]/j-1; else now += a[k]/j;
			now += j;
			if (now < ans) ans = now;
		}
		fout << "Case #" << i+1 << ": " << ans << endl;
	}
	fin.close();
	fout.close();
}
