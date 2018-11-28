#include<bits/stdc++.h>

using namespace std;

#define INF 1000000000
#define N 212346

int p[N];

int main(){
	freopen("ip.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int c, t, d, i, m, ans, tans;
	cin>>c;
	for(int j = 1; j <= c; j++){
		cin>>d;
        m = 1;
        for(i = 0; i < d; i++){
            cin>>p[i];
            m = max(m, p[i]);
        }
        ans = INF;
        for(t = 1; t <= m; t++){
            tans = t;
            for(i = 0; i < d; i++){
                tans += (p[i] + t - 1) / t - 1;
            }
            ans = min(ans, tans);
        }
        printf("Case #%d: %d\n", j, ans);
	}
	return 0;
}
