#include <bits/stdc++.h>

using namespace std;

const int MAXN = 2000;

int p[MAXN];
int c[MAXN];

int main()
{
	int T;
	cin>>T;
	for (int cases = 1; cases<=T; cases++) {
        int n;
        cin>>n;
        for (int i = 1; i<=n; i++) {
            cin>>p[i];
        }
		int res = INT_MAX;
		for (int t = 1000; t>=1; t--) {
            int delta = 0;
            for (int k = 0; k<=n; k++) c[k] = p[k];
            for (int i = 1; i<=n; i++) {
                if (c[i]<=t) continue;
                else {
                    int tmp = (c[i]+t-1)/t;
                    delta += tmp-1;
                    c[i] = (c[i]+tmp-1)/tmp;
                }
            }
            int sol = c[1];
            for (int i = 1; i<=n; i++) {
                sol = max(sol,c[i]);
            }
            sol += delta;
            res = min(sol,res);
		}
		cout<<"Case #"<<cases<<": "<<res<<endl;
	}
}
