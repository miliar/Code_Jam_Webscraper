#include<bits/stdc++.h>

using namespace std;

#define INF 1000000000
#define N 212346

int p[N], d, ans;

inline void inp(){
    cin>>d;
    for(int i = 0; i < d; i++){
        cin>>p[i];
    }
}

inline void solve(){
    int t, i, tans, MAXT = 1123;
    ans = INF;
    for(t = 1; t <= MAXT; t++){
        tans = t;
        for(i = 0; i < d; i++){
            tans += (p[i] + t - 1) / t - 1;
        }
        ans = min(ans, tans);
    }
}

int main(){
	freopen("input.in", "r", stdin);
	freopen("out2.txt", "w", stdout);
	int c;
	cin>>c;
	for(int j = 1; j <= c; j++){
		inp();
		solve();
        printf("Case #%d: %d\n", j, ans);
	}
	return 0;
}
