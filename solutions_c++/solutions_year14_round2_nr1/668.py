#include<iostream>
#include<fstream>
#include<algorithm>
#include<vector>
#include<string>
using namespace std;

int main(){
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small-attempt0.out", "w", stdout);
	int t;
	cin >> t;
	for(int i = 0; i < t; i++){
		int n; cin >> n;
		vector<int> cnt[101];
		string s1[101];
		string s2[101];
		for(int i = 0; i < n; i++){
			cin >> s1[i];
			char bfr = 'A';
			for(int j = 0; j < s1[i].length(); j++){
				if(s1[i][j] != bfr){
					s2[i] += s1[i][j];
					cnt[i].push_back(1);
					bfr = s1[i][j];
				}else
					cnt[i][cnt[i].size() - 1]++;
			}
		}
		cout << "Case #" << i + 1 << ": ";
		bool isok = true;
		for(int j = 1; j < n; j++)
			if(s2[j] != s2[0])
				isok = false;
		if(!isok)
			cout << "Fegla Won" << endl;
		else{
			int ans= 0;
			for(int i = 0; i < s2[0].length(); i++){
				int mx = 0;
				for(int j = 0; j < n; j++)
					mx = max(mx, cnt[j][i]);

				int r = 1000;
				for(int j = 1; j <= mx; j++){
					int k = 0;
					for(int h = 0; h < n; h++)
						k += abs(cnt[h][i] - j);
					r = min(r, k);
				}
				ans += r;
			}
			cout << ans << endl;
		}
	}
	return 0;
}

