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
		cout << "Case #" << tt << ":\n";
		int n,k;
		cin >> n >> k;
		int ct = 0;
		for(int i=(1<<(n-1))+1;i<(1<<n);i+=2){
			int flag=0;
			int res[11];
			memset(res,-1,sizeof(res));
			for(int j=2;j<=10;j++){
				int cur = 0;
				int cc = 1;
				for(int l=0;l<n;l++){
					if((1<<l)&i) cur += cc;
					cc *= j;
				}
				for(int l=2;l*l <= cur; l++){
					if(cur % l == 0){
						res[j] = l;
						break;
					}
				}
				if(res[j]==-1){
					flag = 1;
				}
			}
			if(flag==0){
				ct++;
				for(int l=n-1;l>=0;l--){
					if((1<<l)&i) cout << 1;
					else cout << 0;
				}
				cout << " " ;
				for(int l=2;l<11;l++) cout << res[l] << " ";
				cout << "\n";
			}
			if(ct == k) break;
		}
	}
	return 0;
	
}
