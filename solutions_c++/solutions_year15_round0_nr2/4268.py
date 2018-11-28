#include <cstdio>
#include <algorithm>
using namespace std;
int main(){
	int T;
	int tt = 1;
	int cake[1010];
	scanf("%d", &T);
	while(T--){
		int d;
		scanf("%d", &d);
		int mx = 0;
		for(int i = 0 ; i < d ; i++){
			scanf("%d", &cake[i]);
			mx = max(mx, cake[i]);
		}
		int ans = mx;
		for(int i = 1 ; i <= mx ; i++){
			int tans = 0;
			for(int j = 0 ; j < d ; j++){
				if(cake[j] > 0)
					tans += (cake[j]-1)/i;
			}
			ans = min(ans, tans+i);
		}
		printf("Case #%d: %d\n", tt++, ans);
	}
	return 0;
}