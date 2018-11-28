#include <iostream>
#include <cstring>
using namespace std;

#define FOR(i,a,b) for(int i=(a);i<(b);i++)

struct building {
	int x1;
	int y1;
	int x2;
	int y2;
};

building bu[1024];
int D[1024][1024];

int main() {
	int T, te = 1;
	cin >> T;
	while(T--) {
		int W, H, B;
		cin >> W >> H >> B;
		FOR(i,0,B) cin >> bu[i].x1 >> bu[i].y1 >> bu[i].x2 >> bu[i].y2;
		memset(D,0x7f,sizeof(D));
		FOR(i,0,B) D[i][i] = 0;
		FOR(i,0,B) FOR(j,0,B) {
			int vd = 0, hd = 0;
			if(bu[i].y2 < bu[j].y1) {
				vd = bu[j].y1 - bu[i].y2 - 1;
			}
			if(bu[i].y1 > bu[j].y2) {
				vd = bu[i].y1 - bu[j].y2 - 1;
			}
			if(bu[i].x2 < bu[j].x1) {
				hd = bu[j].x1 - bu[i].x2 - 1;
			}
			if(bu[i].x1 > bu[j].x2) {
				hd = bu[i].x1 - bu[j].x2 - 1;
			}
			D[i][j] = D[j][i] = max(hd,vd);
		}
		FOR(k,0,B) FOR(i,0,B) FOR(j,0,B) D[i][j] = min(D[i][j],D[i][k]+D[k][j]);
		int res = W;
		FOR(i,0,B) res = min(res,bu[i].x1+W-bu[i].x2-1);
		FOR(i,0,B) FOR(j,0,B) res = min(res,bu[i].x1+D[i][j]+W-bu[j].x2-1);
		cout << "Case #" << te << ": " << res << endl;
		te++;
	}
	return 0;
}