#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
ll p[1005];
int main()
{
	int tc;
	cin >> tc; 
	for (int cs = 1; cs <= tc; cs++) {
		int n;
		cin >> n;
		int cnt = 0;
		for (int i = 0; i < n; i++) {
			cin >> p[i];
			cnt += p[i];
		}

		vector <string> ans;
		ans.clear();
		while (cnt != 0) {
			if (cnt == 3)
				break;
			int mx1 = -1, mx2 = -1, idx1, idx2;
			for (int i = 0; i < n; i++) {
				if (mx1 == -1) {
					mx1 = p[i];
					idx1 = i;
					continue;
				}
				if (mx1 <= p[i]) {
					mx2 = mx1;
					idx2 = idx1;
					mx1 = p[i];
					idx1 = i;
					continue;
				}
				if (mx2 <= p[i]) {
					mx2 = p[i];
					idx2 = i;
					continue;
				}
			}
			if (mx1 == mx2) {
				char c1  = (char)(idx1 + 'A');
				char c2  = (char)(idx2+ 'A');
				string str = "";
				str += c1;
				str += c2;
				p[idx1]--;
				p[idx2]--;
				ans.push_back(str);
				cnt -= 2;
			}
			else {
				char c = (char)(idx1 + 'A');
				string str = "";
				str += c;
				p[idx1]--;
				ans.push_back(str);
				cnt--;
			}
		}
		int tmp[5];
		memset(tmp, -1, sizeof(tmp));
		
		if (cnt == 3) {
			int j = 0;
			for (int i = 0; i < n; i++) {
				if (p[i] == 1) {
					tmp[j] = i;
					j++;
				}
			}
			string str = "";
			str += (char)(tmp[0]+'A');
			ans.push_back(str);
			str = "";
			str += (char)(tmp[1]+'A');
			str += (char)(tmp[2]+'A');
			ans.push_back(str);
			
		}
		int sz = ans.size();
		cout << "Case #" << cs << ": ";
		for (int i = 0; i < sz; i++){
			cout << ans[i] << " ";
		}
		cout<<endl;
	}
	return 0;
}
