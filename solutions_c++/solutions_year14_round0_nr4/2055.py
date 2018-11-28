#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

int main(){
    int T;
    freopen("D-large.in", "r", stdin);
    freopen("b.txt", "w", stdout);
    scanf("%d", &T);
    for(int t = 0; t < T; t++){
        int n;
        double a[1010], b[1010];
        scanf("%d", &n);
        for(int i = 0; i < n; i++){
        	scanf("%lf", &a[i]);
        }
        for(int i = 0; i < n; i++){
        	scanf("%lf", &b[i]);
        }
        sort(a, a + n);
        sort(b, b + n);
        int j = 0;
        int ans1 = 0;
        for(int i = 0; i < n; i++){
        	while(j < n && b[j] < a[i]) j++;
			if(j < n){
				ans1++;
				j++;
			}
        }
        ans1 = n - ans1;
        j = n - 1;
        int p = n - 1;
        int ans2 = 0;
		while(j >= 0){
        	if(a[p] > b[j]){
        		ans2++;
        		p--;
        		j--;
        	}
			else{
				j--;
			}
        }
        printf("Case #%d: %d %d\n", t + 1, ans2, ans1);
    }
    return 0;
}
