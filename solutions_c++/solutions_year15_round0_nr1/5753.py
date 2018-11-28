#include<cstdio>
using namespace std;
int main(){
	freopen("0.in","r", stdin);
	freopen("0.out","w",stdout);
    int s[1005];
    int t;
    scanf("%d", &t);
    for(int ca = 1; ca <= t; ca ++){
		int n;
		scanf("%d", &n);
        for(int i = 0; i <= n; i ++){
            char tmps[2];
            scanf("%1s", tmps);
            s[i] = tmps[0] - '0';
        }
        int ans = 0;
        int now_people = 0;
        for(int i = 0; i <= n; i ++){
            if (i > now_people){
                ans += i - now_people;
                now_people = i;
            }
            now_people += s[i];
        }
        printf("Case #%d: %d\n", ca, ans);
    }
	return 0;
}
