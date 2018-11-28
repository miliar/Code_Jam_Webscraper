#include <iostream>
#include <memory.h>
#include <string>
#include <vector>
using namespace std;

int a[4][4], b[4][4];
bool mark[16];

int main(){
	int T, cnt = 1;
	cin >> T;
	while (T--){
		int r1, r2;
		cin >> r1;
		memset(mark, false, sizeof mark);
		for (int i = 0;i < 4;++i)
			for (int j = 0;j < 4;++j)
				cin >> a[i][j];
		cin >> r2;
		for (int i = 0;i < 4;++i)
			for (int j = 0;j < 4;++j)
				cin >> b[i][j];
		r1--, r2--;
		for (int i = 0;i < 4;++i)
			mark[a[r1][i] - 1] = true;
			
		int ans = -1;
		for (int i = 0;i < 4;++i){
			if (mark[b[r2][i] - 1] == true){
				if (ans == -1)
					ans = b[r2][i];
				else ans = -2;
			}
		}
		
		cout << "Case #" << cnt++ << ": ";
		if (ans > 0) cout << ans << endl;
		else if (ans == -2) cout << "Bad magician!" << endl;
		else cout << "Volunteer cheated!" << endl;
	}
	return 0;
}