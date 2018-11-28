#include <bits/stdc++.h>
using namespace std;

#define int long long
#define MOD 1000000007

signed main(){
	freopen("a.txt","r",stdin);
	freopen("out.txt","w",stdout);
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	int tt;
	cin >> tt;
	for(int t = 1;t<=tt;t++){
		cout << "Case #" << t << ": ";
		int n,c,s;
		cin >> n >> c >> s;
		if(((c==1) && (s<n)) || (s<((n+1)/2))){
			cout << "IMPOSSIBLE\n";
			continue;
		}
		if(c==1){
			for(int i=1;i<=n;i++) cout << i << " ";
			cout << "\n";
			continue;
		}
		int cur = 1;
		for(int i=0;i<c-1;i++) cur *= n;
		int ccc = cur;
		ccc *= n;
		cur  *= 2;
		cur += 2;
		int cc = 2;
		for(int i=0;i<(n/2);i++){
			cout << cc << " ";
			cc += cur; 
		}
		if(n%2){
			cout << ccc ;
		}
		cout << "\n";
	}
	return 0;
}
