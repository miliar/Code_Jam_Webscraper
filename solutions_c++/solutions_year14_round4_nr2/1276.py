#include <bits/stdc++.h>
using namespace std;
typedef pair<int, int> pii;

const int N=1e5;
int n, v[N], vl[N], vr[N], bit[N], vc[N];

int mod(int x) { return x>0 ? x : -x; }

int main() {
	int T;
	cin>>T;
	for(int t=1;t<=T;t++) {
		cin>>n;
		for(int i=0;i<n;i++) cin>>v[i];
		int ans=1<<30;
		for(int mask=0;mask<1<<n;mask++) {
			vector<int> v1, v2;
			for(int j=0;j<n;j++) {
				if((1<<j) & mask) v1.push_back(v[j]);
				else v2.push_back(v[j]);
			}
			sort(v1.begin(), v1.end());
			sort(v2.begin(), v2.end());
			reverse(v2.begin(), v2.end());
			for(int j=0;j<v2.size();j++) v1.push_back(v2[j]);
			int aux=0;
			for(int i=0;i<n;i++) {
				for(int j=0;j<v1.size();j++) if(v1[j] == v[i]) {
					v1.erase(v1.begin()+j);
					aux += j;
					break;
				}
			}
			ans = min(ans, aux);
		}
		printf("Case #%d: %d\n", t, ans);
	}
	return 0;
}
