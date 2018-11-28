#include <bits/stdc++.h>
using namespace std;
#define LL long long
#define INF 1000000000
#define pii pair<int,int>
#define vi vector<int>
#define mp make_pair
#define fi first
#define se second
#define pu push
#define pb push_back

int main(){
	int tc,tot,ans,n,cc;
	cin>>tc;
	for(int zz = 1; zz <= tc; zz++){
		char input[1005];
		tot = ans = 0;
		scanf("%d %s", &n, &input);
		int len = n+1;
		for (int i = 0; i < len; i++){
			if (tot >= len)
				break;
			int kurang = (int)input[i] - '0';
			
			if (kurang == 0)
				continue;
			
			if (tot < i){
				int diff = i - tot;
				tot += diff;
				ans += diff;
			}

			tot += kurang;
			// printf("tot %d ans %d\n", tot, ans);
		}
		printf("Case #%d: %d\n", zz, ans);
	}
}