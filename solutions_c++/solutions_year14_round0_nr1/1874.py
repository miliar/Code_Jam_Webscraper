#include<iostream>
#include<string>
#include<vector>
#include<algorithm>

using namespace std;

int main()
{
	int T;
	while(cin >> T){
		for(int t = 1; t<= T; ++t){
			int r1, r2;
			int m[4][4], n[4][4];
			cin >> r1;
			for(int i = 0; i< 4; ++i){
				for(int j = 0; j< 4; ++j){
					cin >> m[i][j];
				}
			}
			cin >> r2;
			for(int i = 0; i< 4; ++i){
				for(int j = 0; j< 4; ++j){
					cin >> n[i][j];
				}
			}
			vector<int> pm = vector<int>(4);
			vector<int> pn = vector<int>(4);
			for(int j = 0; j< 4; ++j){
				pm[j] = m[r1-1][j];
			}
			for(int j = 0; j< 4; ++j){
				pn[j] = n[r2-1][j];
			}
			sort(pm.begin(), pm.end());
			sort(pn.begin(), pn.end());
			int v = -1;
			int cnt = 0;
			int i = 0, j = 0;
			while(i<4 && j< 4){
				if(pm[i] == pn[j]){
					cnt ++;
					v = pm[i];
					i++; j++;
				}
				else if(pm[i] < pn[j]){
					i++;
				}
				else j++;
			}
			if(cnt == 1) cout << "Case #" << t << ": " << v;
			else if(cnt == 0) cout << "Case #" << t << ": " << "Volunteer cheated!";
			else cout << "Case #" << t << ": " << "Bad magician!"; 
			cout << endl;
		}

		
	}
}