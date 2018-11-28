#include <bits/stdc++.h>
using namespace std;
#define fr(i,a,b) for(int i = a; i < b; ++i)
#define rep(i, n) fr(i, 0, n)


int main(){
	ios::sync_with_stdio(false);
	int t;
	cin >> t;

	fr(tt, 1, t+1){
		int mk[] = {0,0};

		rep(k, 2){
			int c;
			cin >> c;
			rep(i, 4) rep(j, 4){
				int x;
				cin >> x;
				if(i == c-1) mk[k] |= 1 << x;
			}
		}

		int inter = mk[0] & mk[1], card, cnt = 0;
		fr(i, 1, 17) if(inter & (1<<i)){
			++cnt;
			card = i;
		}

		cout << "Case #" << tt << ": ";
		if(cnt == 1) cout << card << endl;
		else if(cnt == 0) cout << "Volunteer cheated!" << endl;
		else cout << "Bad magician!" << endl;

	}

}



