#include <bits/stdc++.h>
using namespace std;
#define ll long long
//string res[] = { "First", "Second" };
//const double pi = 3.1415926535897932384626433832795;
//int dx[] = {-1,0,1,0};
//int dy[] = {0,-1,0,1};

/*
 bool valid(int r,int c){
 return (r >= 0 && r < n && c >= 0 && c < m);
 }
 */

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	ios_base::sync_with_stdio(0) ;

	int T;
	cin >> T;
	for(int t=1;t <= T;++t) {
		ll n;
		cin >> n;
		if(n == 0) {
			printf("Case #%d: INSOMNIA\n",t);
			continue;
		}

		bool a[10];
		memset(a,1,sizeof(a));
		int c = 0,m = 1;

		while(1) {
			ll temp = n*m;
			ll ans = temp;
			m++;
			while(temp) {
				c += a[temp%10];
				a[temp%10] = 0;
				temp /= 10;
			}

			if(c == 10) {
				printf("Case #%d: %d\n",t,ans);
				break;
			}
		}

	}

}
