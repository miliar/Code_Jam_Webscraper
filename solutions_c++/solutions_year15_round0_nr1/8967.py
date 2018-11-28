#include <iostream>
using namespace std;
int main() {
	freopen("A.in", "rt", stdin);
	freopen("A2.out", "wt", stdout);
	int t; cin>>t;
	for(int tt = 1 ; tt <= t ; tt++){
		int mx ;
		cin >> mx;
		int cnt = 0, ans = 0 ;
		for(int i = 0 ; i < mx+1 ; i++){
			char x;
			cin>>x;
			int nxt = x - '0';
			if(i > cnt && nxt){
				ans += (i-cnt), cnt += (i-cnt);
			}
			cnt += nxt;
		}
		cout << "Case #"<< tt << ": " << ans << endl;
	}
	return 0;
}

