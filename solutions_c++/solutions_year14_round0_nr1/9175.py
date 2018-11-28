#include <iostream>
#include <string>

using namespace std;

int main(){
	int T;
	cin >> T;
	for(int t=0;t<T;t++){
		int num[17], y;
		fill(num, num+17, 0);
		for(int k=0;k<2;k++){
			cin >> y;
			for(int i=0;i<4;i++){
				for(int j=0;j<4;j++){
					int tmp;
					cin >> tmp;
					if(y == i + 1) num[tmp]++;
				}
			}
		}
		int ans, cnt = 0;
		for(int i=1;i<17;i++) if(num[i] == 2) {ans = i; cnt++;}
		cout << "Case #" << t+1 << ": ";
		if(cnt == 0) cout << "Volunteer cheated!" << endl;
		else if(cnt > 1) cout << "Bad magician!" << endl;
		else cout << ans << endl;
	}
	return 0;
}
