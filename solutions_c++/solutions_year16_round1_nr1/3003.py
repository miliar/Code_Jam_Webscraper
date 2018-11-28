#include <bits/stdc++.h>
using namespace std;

#define forn(i,n) for(int i=0;i<int(n);i++)
#define forsn(i,s,n) for(int i=(int)(s);i<(int)(n);i++)
#define dforsn(i,s,n) for(int i=(int)(n-1);i>=int(s);i--)
#define si(a) ((int)(a).size())
#define pb push_back
#define mp make_pair
#define endl '\n'
typedef vector<int> vi;
typedef pair<int,int> pii;
typedef long long int tint;

int main() {
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	
	ios_base::sync_with_stdio(false); 
	cin.tie(0);

	int nc;
	cin >> nc;
	
	forsn(i, 1, nc+1) {
		string s;
		cin >> s;
		
		string sol;
		sol += s[0];
		forsn(i, 1, si(s)) {
			if (s[i] >= sol[0]) sol = s[i] + sol;
			else sol += s[i];
		}
		
		cout << "Case #" << i << ": " << sol << endl;
	}

	return 0;
}
