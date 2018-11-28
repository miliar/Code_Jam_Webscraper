#include <iostream>
#include <math.h>
#include <stdlib.h>
#include <cstdio>

using namespace std;

int main() {
	int t,a1,a2,st[4][4],nd[4][4],f,ff;
	freopen("A-small-attempt2.in", "r", stdin);
	freopen("a.out", "w", stdout);
	cin >> t;
	for (int h=0;h<t;h++) {
		ff=0;
		int x[4]={0};
		cin >> a1;
		a1--;
		for (int i=0;i<4;i++) {
			for (int j=0;j<4;j++) {
				cin >> st[i][j];
			}
		}
		cin >> a2;
		a2--;
		for (int i=0;i<4;i++) {
			for (int j=0;j<4;j++) {
				cin >> nd[i][j];
			}
		}
		/*for (int i=0;i<4;i++) {
			x[i]=st[a1][i];
		}*/
		for (int i=0;i<4;i++) {
			f=0;
			for(int j=0;j<4;j++) {
				if (nd[a2][i]==st[a1][j]) {f++;break;}
			}
			if(f>0){
				x[ff]=nd[a2][i];
				ff++;
			}
		}
		//out
		if(x[1]!=0) cout << "Case #" << h+1 << ": Bad magician!" << endl;
		else if(x[0]==0) cout << "Case #" << h+1 << ": Volunteer cheated!" << endl;
		else cout << "Case #" << h+1 << ": " << x[0] << endl;

	}
	fclose(stdout);
	//cin >> f;
	return 0;
}