#include <iostream>
#include <cstdio>
#include <fstream>
using namespace std;

int main() {
//	freopen("a.in","r",stdin);
//	freopen("b.out","w",stdout);
	int n;
	cin>>n;
	int r[2];
	int a[2][5][5];
	int num=0;
	while (n--) {
		for (int k=0; k<2; k++) {
			scanf("%d", &r[k]);
			for (int i=1; i<=4; i++) 
			for (int j=1; j<=4; j++) 
				scanf("%d", &a[k][i][j]);
		}
		int x=r[0];
		int y=r[1];
		
		int cnt=0;
		int ans=0;
		for (int i=1; i<=4; i++)
		for (int j=1; j<=4; j++)
		if (a[0][x][i]==a[1][y][j]) {
			cnt++;
			ans=a[0][x][i];
		}
		printf("Case #%d: ", ++num);
		if (cnt>1) printf("Bad magician!");
		if (cnt==1) printf("%d", ans);
		if (cnt<1) printf("Volunteer cheated!");
		printf("\n");
	}
	return 0;
}
