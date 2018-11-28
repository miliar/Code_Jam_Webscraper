#include <iostream>
#include <vector>

using namespace std;

int ileTestow, sze, wys;
int t[100][100];
bool v[100][100];

int mxR(int r){
	int mx = t[r][0];
	for(int i=1; i<sze; i++) mx = max(mx, t[r][i]);
	return mx;
}
int mxC(int c){
	int mx = t[0][c];
	for(int i=1; i<wys; i++) mx = max(mx, t[i][c]);
	return mx;
}
void setR(int r, int val){
	for(int i=0; i<sze; i++) if( t[r][i] == val ) v[r][i] = true;
}
void setC(int c, int val){
	for(int i=0; i<wys; i++) if( t[i][c] == val ) v[i][c] = true;
}

int main(){

	scanf("%d", &ileTestow);

	for(int q=1; q<=ileTestow; q++){
		scanf("%d%d", &wys, &sze);

		for(int i=0; i<wys; i++) for(int j=0; j<sze; j++) scanf("%d", &t[i][j]);	

		memset(v,0,sizeof v);

		for(int i=0; i<wys; i++) setR(i, mxR(i));
		for(int i=0; i<sze; i++) setC(i, mxC(i));
		
		bool everything = true;
		for(int i=0; i<wys; i++) for(int j=0; j<sze; j++) if( !v[i][j] ) everything = false;
		if( !everything) {
			cout << "Case #" << q << ": NO" << endl;
		} else {
			cout << "Case #" << q << ": YES" << endl;
		}
	}

	return 0;
}
