#include<cstdio>
#include<cstring>
#include<algorithm>
#include<cmath>
#include<cstdlib>
using namespace std;
const int MAX = 10000 + 10;
int rec[MAX];
int main(){
	freopen("Alarge.in", "r", stdin);
	freopen("Alarge.out", "w", stdout);
	int TN;
	int n, m;
	scanf("%d", &TN);
	for(int casen = 1 ; casen <= TN ; casen++){
		scanf("%d %d", &n, &m);
		for(int i = 0 ; i < n ; i++){
			scanf("%d", &rec[i]);
		}
		sort(rec, rec+n);
		int l = 0, ans = 0;
		for(int i = n-1 ; i >= l ; i--){
			if(i==l){
				ans++;
				break;
			}
			if(rec[i] + rec[l] <= m){
				l++, ans++;
			}else ans++;
		}
		printf("Case #%d: %d\n", casen, ans);
	}
	return 0;
}
