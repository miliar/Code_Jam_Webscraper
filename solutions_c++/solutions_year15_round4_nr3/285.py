#include <bits/stdc++.h>
using namespace std;

#define FOR(i,a,b) for(int i=a;i<int(b);i++)
typedef long long LL;
typedef pair<int,int> PT;

int TC, N;

int main() {
	cin >> TC;
	FOR(tc,1,TC+1) {
		cin >> N; cin.ignore(999, '\n');
		unordered_map<string, int> mpp;
		vector<vector<int>> st;
		FOR(n,0,N) {
			string s;
			getline(cin, s);
			istringstream ss(s);
			vector<int> vi;
			while (ss >> s) {
				if (!mpp.count(s)) {
					int i = mpp.size();
					mpp[s] = i;
				}
				vi.push_back(mpp[s]);
			}
			sort(begin(vi), end(vi));
			st.push_back(vi);
		}
		vector<int> wst(mpp.size());
		for (int x : st[0]) wst[x] |= 2;
		for (int x : st[1]) wst[x] |= 4;
		int ans = INT_MAX;
		FOR(bs, 0, 1<<(N-2)) {
			vector<int> wst2 = wst;
			FOR(n,2,N) for (int x : st[n]) {
				if (bs & (1<<(n-2))) wst2[x] |= 2; else wst2[x] |= 4;
			}
			int mm = 0;
			for (int x : wst2) if (x == 6) mm++;
			ans = min(ans, mm);
		}
		cout << "Case #" << tc << ": " << ans << endl;
	}
}
