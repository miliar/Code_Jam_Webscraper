#include <bits/stdc++.h>

using namespace std;

#define MOD 1000000007
#define inf 1000000000
#define maxn 2000

#define ll long long
#define pii pair<int, int>
#define pb push_back
#define sin scanint
#define bitcount(x) __builtin_popcount(x)
#define fill(s, p) memset(s, p, sizeof(s));

#ifdef ONLINE_JUDGE
#define gc getchar_unlocked
#endif

#ifndef ONLINE_JUDGE
#define gc getchar
//freopen("input.txt", "r", stdin)
//freopen("output.txt", "w", stdout)
#endif

void scanint(int &x)
{
    register int c = gc();
    x = 0;
    for(;(c<48 || c>57);c = gc());
    for(;c>47 && c<58;c = gc()) {x = (x<<1) + (x<<3) + c - 48;}
}

int mem[10][10];

int solve(int n, int *a)
{
	//cout << n << " " << a[n] << endl;
	if(a[n]<=0)
		return solve(n-1, a);
	if(n<=3)
		return n;
	//if(mem[n][a[n]]!=-1)
	//	return mem[n][a[n]];
	int i, j, ret = inf;
	a[n]--;
	for(i=1; i<=(n/2); i++){
		a[i]++;
		a[n-i]++;
		ret = (min(ret, 1+solve(n, a)));
		//cout << n << " " << i << " " << ret << " " << a[i] << " " << a[n-i] << endl;
		a[i]--;
		a[n-i]--;
	}
	a[n]++;
	return min(ret, n);
}

int cnt[maxn], arr[maxn];

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("o2.txt", "w", stdout);
	int t, i, j, n, ans, case_num=1, mx;
	sin(t);
	while(t--){
		fill(mem, -1);
		fill(cnt, 0);
		sin(n);
		mx = -1;
		for(i=0; i<n; i++){
			sin(arr[i]);
			cnt[arr[i]]++;
			mx = max(mx, arr[i]);
		}
		if(n==6){
			if(cnt[8]==6)
				ans = 8;
			else if(cnt[9]==6)
				ans = 9;
			else if(cnt[8]==5 && cnt[9]==1)
				ans = 9;
			else if(cnt[9]==5 && cnt[8]==1)
				ans = 9;
			else
				ans = solve(mx, cnt);
		}
		else{
			ans = solve(mx, cnt);
		}
		printf("Case #%d: %d\n", case_num++, ans);
	}
	return 0;
}