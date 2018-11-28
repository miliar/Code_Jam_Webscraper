#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main() {

	int t, ca = 1;
	string s;

	cin >> t;
	cin.ignore (); 
	while (t--) {
		getline(cin, s);
		vector<int> cnt(26, 0);
		for (char c : s) {
			cnt[(int)c-65]++;
		}
		// Zero
		int z = (int)'Z'-65;		
		int e = (int)'E'-65;		
		int r = (int)'R'-65;	
		int o = (int)'O'-65;

		int w = (int)'W'-65;
		int t = (int)'T'-65;
		int h = (int)'H'-65;
		int f = (int)'F'-65;
		int u = (int)'U'-65;
		int i = (int)'I'-65;
		int v = (int)'V'-65;
		int s = (int)'S'-65;
		int x = (int)'X'-65;	
		int n = (int)'N'-65;	
		int g = (int)'G'-65;			
		string ans = "";
		while (cnt[z] > 0) {
			ans += "0";
			cnt[z]--;
			cnt[e]--;
			cnt[r]--;
			cnt[o]--;
		}
		// Two
		while (cnt[w] > 0) {
			ans += "2";
			cnt[t]--;
			cnt[w]--;
			cnt[o]--;
		}
		//Four
		while (cnt[u] > 0) {
			ans += "4";
			cnt[f]--;
			cnt[o]--;
			cnt[u]--;
			cnt[r]--;		
		}
		//Five
		while (cnt[f] > 0) {
			ans += "5";
			cnt[f]--;
			cnt[i]--;
			cnt[v]--;
			cnt[e]--;		
		}
		//Six
		while (cnt[x] > 0) {
			ans += "6";
			cnt[s]--;
			cnt[i]--;
			cnt[x]--;		
		}
		//Seven
		while (cnt[v] > 0) {
			ans += "7";
			cnt[s]--;
			cnt[e]--;
			cnt[v]--;
			cnt[e]--;
			cnt[n]--;		
		}
		//Eight
		while (cnt[g] > 0) {
			ans += "8";
			cnt[e]--;
			cnt[i]--;
			cnt[g]--;
			cnt[h]--;
			cnt[t]--;		
		}
		//Three
		while (cnt[h] > 0) {
			ans += "3";
			cnt[t]--;
			cnt[h]--;
			cnt[r]--;
			cnt[e]--;
			cnt[e]--;		
		}
		//Nine
		while (cnt[i] > 0) {
			ans += "9";
			cnt[n]--;
			cnt[i]--;
			cnt[n]--;
			cnt[e]--;		
		}
		// One
		while (cnt[o] > 0) {
			ans += "1";
			cnt[o]--;
			cnt[n]--;
			cnt[e]--;		
		}
		sort(ans.begin(), ans.end());
		cout << "Case #" << ca++ << ": " << ans << endl;
	}

}
