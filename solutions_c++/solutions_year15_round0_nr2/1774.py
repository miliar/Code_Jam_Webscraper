#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

const int Maxn = 10010;

int N,p[Maxn],T;

int main() {
    scanf("%d", &T);
    for (int _ = 1; _ <= T; _++) {
        cin >> N;
        for (int i=1;i<=N;i++) cin >> p[i];
        int ans = 999999;
        for (int i=1;i<=1000;i++){
        	int now = i;
        	for (int j=1;j<=N;j++)
        		now += (p[j]-1) / i;
        	ans = min(ans , now);
        }
    	printf("Case #%d: %d\n",_,ans);
    }
    return 0;
}
