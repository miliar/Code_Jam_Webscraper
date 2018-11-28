#include<bits/stdc++.h>
#define si(n) scanf("%d",&n);
#define sl(n) scanf("%lld",&n);
#define ss(n) scanf("%s",n);
#define fr(i, n) for(i = 0; i < n; i++)
#define ms(i, n) memset(i, n, sizeof(i))
typedef long long LL; 
using namespace std;
int main () {
	//freopen ("input.in","r",stdin);
	//freopen ("output.txt","w",stdout);
	int t, u;
	double c, f, x, t_elap, made, rate, next_ans, prev_ans;
	si(t);
	u = t;
	while (t--) {
		scanf("%lf %lf %lf", &c, &f, &x);
		t_elap = 0;
		rate = 2.0;
		next_ans = x / 2;
		while (1) {
			prev_ans = next_ans;
			made = c / rate;
			rate += f;
			t_elap += made;
			next_ans = t_elap + (x / rate);
			if (next_ans >= prev_ans)
				break;
		}
		printf("Case #%d: ", u - t);
		printf("%.7lf\n", prev_ans);
	}
	return 0;
}

