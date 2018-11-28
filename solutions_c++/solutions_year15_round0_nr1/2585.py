#include <bits/stdc++.h>
#define MOD 1000000007
#define pb push_back
using namespace std;
int main() {
	ios_base::sync_with_stdio(false);
	freopen("a.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int t;
	cin >> t;
	for(int tt=1;tt<=t;tt++){
		cout << "Case #" << tt << ": ";
		int n;
		cin >> n;
		int a[1001];
		for(int i=0;i<1001;i++) a[i]=0;
		string s;
		cin >> s;
		int cur = 0;
		int ans = 0;
		for(size_t i=0;i<s.length();i++){
			a[i]=s[i]-'0';
			if(i>cur){
				ans+=(i-cur);
				cur+=(i-cur);
			}
			cur += a[i];
		}
		cout << ans << "\n";
	}
}
