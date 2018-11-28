#include <iostream>

using namespace std;

int v[10][10];
int n,m;

bool checkRow(int x, int y) {
	for (int i=0; i<m; i++) {
		if (v[x][i]!=1) return false;
	}
	return true;
}

bool checkColumn(int x, int y) {
	for (int i=0; i<n; i++) {
		if (v[i][y]!=1) return false;
	}
	return true;
}

int main() {
	freopen ("B-small-attempt0.in","r",stdin);
	freopen ("out.txt","w",stdout);
	int zz;
	cin>>zz;
	for (int ww=0; ww<zz; ww++) {
		bool res = true;
		
		cin>>n>>m;
		for (int i=0; i<n; i++) {
			for (int j=0; j<m; j++) {
				cin>>v[i][j];
			}
		}
		for (int i=0; i<n; i++) {
			for (int j=0; j<m; j++) {
				if (v[i][j]==1) {
					if ((checkColumn(i,j)||checkRow(i,j))) ;
					else {
						res=false;
					}
				}
			}
		}
		cout<<"Case #"<<ww+1<<": ";
		if (res) {
			cout<<"YES";
		}
		else {
			cout<<"NO";
		}
		cout<<'\n';
	}
	return 0;
}