#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cstdlib>


using namespace std;

#define frl(a, b, c) for( (a) = (b);( a) < (c); (a++))
#define fru(a, b, c) for( (a) = (b); (a) <= (c); (a++))
#define frd(a, b, c) for( (a) = (b); (a) >= (c); (a--))
#define mst(a, b) memset(a, b, sizeof(a))
#define si(a) scanf("%d", &a)
#define ss(a) scanf("%s", a)
#define sc(a) scanf("%c", &a)

#define pb(a) push_back(a)
#define mp make_pair
#define nwl puts("");
#define sp << " " <<

#define sz size()
#define bg begin()
#define en end()
#define X first
#define Y second

#define vi vector <int>
#define vs vector <string>
#define ll long long int
#define dec int i = 0, j= 0, k = 0;

#define i(n) cin >> n;
#define p(s) cout << s;

int main(){
	int t, i, j, k;
	freopen("A-large.in", "r", stdin);
	freopen("outLargeA.txt", "w", stdout);
	cin >> t;

	for(int tt = 1; tt <= t; tt++){

		string str;
		cin >> k >> str;
		// cout << str << endl;
		int cnt = 0, ans = 0;
		cnt += str[0] - '0';

		for(int i = 1; i < str.sz; i++){
			if(cnt < i)
				ans += i - cnt, cnt += i - cnt, cnt += str[i] - '0';
			else
				cnt += str[i] - '0';
			// cout << cnt << " " << ans << endl;
		}
		cout << "Case #" << tt << ": " << ans << endl;
	}
}







































