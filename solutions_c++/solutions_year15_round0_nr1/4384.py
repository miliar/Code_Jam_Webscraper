#include<bits/stdc++.h>
using namespace std;
typedef long long int LL;
#define sd(x) scanf("%d", &x)
#define mp make_pair
#define pb push_back
#define vi vector<int>
#define ft first
#define sc second
#define INF 1000000000
#define MOD 10000007
int main()
{
	freopen("inp.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t, n, tc = 0;
	string s;
	cin>>t;
	while (t--) {
		cin>>n>>s;
		int ans = 0;
		int curr = 0;
		for (int i = 0; i <= n; i++) {
			if(curr >= i) {
				curr += s[i]-'0';
			} else {
				ans += i-curr;
				curr += i-curr+s[i]-'0';
			}
		}
		cout<<"Case #"<<++tc<<": "<<ans<<endl;
	}
	return 0;
}
