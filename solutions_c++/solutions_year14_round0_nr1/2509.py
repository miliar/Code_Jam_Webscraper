#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define S(x) scanf("%d", &x);
#define div /
int main()
{
	freopen("in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t;
	S(t);
	int i,j;
	int tt;
	for(tt = 1;tt <= t;tt++) {
		int xx,yy;
		S(xx);
		xx--;
		int a[6][6];
		for(i = 0;i < 4;i++) {
			for(j = 0; j < 4;j++) {
				S(a[i][j]);
			}
		}
		S(yy);
		yy--;
	//	cout << xx << "  " << yy << "\n";
		int b[6][6];
		for(i = 0;i < 4;i++) {
			for(j = 0; j < 4;j++) {
				S(b[i][j]);
			}
		}
		int co = 0;
		int in;
		for(j = 0;j < 4;j++) {
			for(i = 0;i < 4;i++){
				if(a[xx][j] == b[yy][i]) {
					co++;
					in = b[yy][i];
				}
		//		cout << co << " " << b[yy][i] <<" "  <<a[xx][j] <<"\n";
			}
		}
		if(co == 1) {
			printf("Case #%d: %d\n" ,tt, in);
		}
		else if(co > 1){
			printf("Case #%d: Bad magician!\n",tt);
		}else if(co == 0){
			printf("Case #%d: Volunteer cheated!\n",tt);
		}
	}
	return 0;
}


