#include <bits/stdc++.h>
#define pb push_back
#define mp make_pair
#define ft first
#define sc second
#define INF (int)1e9
typedef long long LL;
using namespace std;

int main(){
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int t, n;
	char arr[1005];
	scanf("%d",&t);
	for(int tc = 1; tc <= t; tc++ ){
		scanf("%d",&n);
		scanf("%s",arr);
		int p = 0, ans = 0;
		for(int i = 0; i <= n; i++ ){
			if(p<i){
				ans += i-p;
				p = i;
			}
			p += arr[i]-'0';
		}
		printf("Case #%d: %d\n",tc,ans);
	}
	return 0;
}


