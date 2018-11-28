#include <bits/stdc++.h>
#define pb push_back
#define mk make_pair
#define fi first
#define se second
#define For(i,a,b) for(int (i)=(a);(i) < (b); ++(i))
using namespace std;
typedef vector<int> vi;
typedef pair<int,int> ii;
typedef long long ll;
typedef vector<bool> vb;



int main(void) {
	ios::sync_with_stdio(false);
	int T;
	cin >> T;
	for(int t = 1; t <= T; t++){
		string s;
		cin >> s;
		int cnt = 0;
		for(int i = 0; i < s.size() - 1; i++){
			if(s[i]!= s[i + 1]){
				cnt++;
			}
		}

		if(s.back() == '-'){
			cnt++;
		}
		cout << "Case #" << t << ": " << cnt << endl;
	}	
	
	return 0;
}
