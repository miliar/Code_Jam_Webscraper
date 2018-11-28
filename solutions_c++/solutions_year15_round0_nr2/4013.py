//In the name of God
#include <bits/stdc++.h>
using namespace std;
#define For(i,a,b) for(int (i)=(a);(i) < (b); ++(i))
#define Rof(i,a,b) for(int (i)=(a);(i) >= (b); --(i))
#define mkp make_pair
#define XX first
#define YY second
#define pb push_back
const int Maxn = 2e5 + 9;
int arr[Maxn];
int main(){
	freopen("file.out","w",stdout);
	int t;
	cin >> t;
	int tc = 0;
	while(t--){
		int n;
		scanf("%d",&n);
		For(i,0,n)
			scanf("%d",&arr[i]);
		int ans = 1e9;
		For(i,1,1001){
			int cnt = 0;
			For(j,0,n){
				cnt += (arr[j] - 1) / i;
			}
			ans = min(ans,cnt + i);
		}
		printf("Case #%d: %d\n",++tc,ans);
	}
}
