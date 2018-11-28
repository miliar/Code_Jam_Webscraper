#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;

int main()
{
	int T,n1,n2,ans;
	int gra1[4][4],gra2[4][4];
	bool flag[17],flagbad,flagvol;
	cin >> T;
	for(int t=1;t<=T;++t) {
		cin >> n1;
		for(int i=0;i<4;++i)
			for(int j=0;j<4;++j)
				cin >> gra1[i][j];
		cin >> n2;
		for(int i=0;i<4;++i)
			for(int j=0;j<4;++j)
				cin >> gra2[i][j];
		cout << "Case #" << t << ": ";
		memset(flag,0,sizeof(flag));
		flagbad=0;
		flagvol=1;
		for(int i=0;i<4;++i)
			flag[gra1[n1-1][i]]=true;
		for(int i=0;i<4;++i)
			if(flag[gra2[n2-1][i]]) {
				if(flagvol==0) {
					flagbad=1;
					break;
				}
				flagvol=0;
				ans=gra2[n2-1][i];
			}
		if(flagbad) cout << "Bad magician!" << endl;
		else if(flagvol) cout << "Volunteer cheated!" << endl;
		else cout << ans << endl;
	}
	return 0;
}
