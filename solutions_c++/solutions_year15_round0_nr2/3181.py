#include <bits/stdc++.h>

using namespace std;

typedef pair<int,int> pii;

const int MAXN = 1004, INF = 2*(int)1e9;

int tnum, d, p[MAXN], sum, count_acc[MAXN], ct[MAXN];

int main(){
    scanf("%d", &tnum);
    for (int t=1; t<=tnum; t++){
        sum = 0;
        memset(count_acc, 0, sizeof count_acc);
        memset(ct, 0, sizeof ct);
        
        scanf("%d", &d);
        for (int i=1; i<=d; i++){
            scanf("%d", &p[i]);
            sum += p[i];
            count_acc[p[i]]++;
            ct[p[i]]++;
        }
        
        for (int i=1; i<=1000; i++) count_acc[i] += count_acc[i-1];
        
        int ans = INF;
        
        for (int i=1; i<=1000; i++){
            int tem = i;
            for (int j=i+1; j<=1000; j++) tem+= ct[j] * (j/i - 1 +(j%i==0?0:1));
            ans = min(ans, tem);
        }
        
        printf("Case #%d: %d\n", t, ans);
    }
	return 0;
}
