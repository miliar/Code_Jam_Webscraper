#include <bits/stdc++.h>
using namespace std;
#define MOD 1000000007
#define int long long
signed main() {
	freopen("a.txt","r",stdin);
	freopen("out.txt","w",stdout);
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	int tt;
	cin >> tt;
	for(int t = 1;t<=tt;t++){
		cout << "Case #" << t << ": ";
		int n;
		cin >> n;
		if(n==0){
			cout << "INSOMNIA\n";
			continue;
		}
		int res[10];
		memset(res,0,sizeof(res));
		int flag=10;
		int c = n;
		while(1){
			int x = c;
			int y;
			while(x!=0){
				y = x%10;
				x /= 10;
				if(res[y]==0){
					flag--;
					res[y] = 1;
				}
			}
			if(flag==0){
				cout << c << "\n";
				break;
			}
			c += n;
		}
	}
    return 0;
}
