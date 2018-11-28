#include <bits/stdc++.h>
using namespace std;

int t,n,ans,a[15],p[15],pre,nxt; bool ok;

int main(){
	ios::sync_with_stdio(0); cin.tie(0);
	freopen("bffs.in","r",stdin);
	freopen("bffs.out","w",stdout);
	cin >> t;
	for (int tc=1;tc<=t;tc++){
		cout << "Case #" << tc << ": ";
		cin >> n; ans=0;
		for (int i=1;i<=n;i++){
			cin >> a[i]; p[i]=i;
		}
		do{
			for (int i=1;i<=n;i++){
				ok=true;
				for (int j=1;j<=i;j++){
					pre=p[j==1?i:j-1];
					nxt=p[j==i?1:j+1];
					ok&=a[p[j]]==pre||a[p[j]]==nxt;
				}
				if (ok) ans=max(ans,i);
			}
		}while (next_permutation(p+1,p+n+1));
		cout << ans << "\n";
	}
}
