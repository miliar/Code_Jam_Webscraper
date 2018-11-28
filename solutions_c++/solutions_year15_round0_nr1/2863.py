#include <bits/stdc++.h>
using namespace std;

#define all(v) (v).begin(), (v).end()
#define rall(v) (v).rbegin(), (v).rend()
#define pb push_back
#define f(i,x,y) for(int i = x; i<y; i++ )
#define FORV(it,A) for(vector<int>::iterator it = A.begin(); it!= A.end(); it++)
#define FORS(it,A) for(set<int>::iterator it = A.begin(); it!= A.end(); it++)
#define quad(x) (x) * (x)
#define mp make_pair
#define clr(x, y) memset(x, y, sizeof x)
#define fst first
#define snd second
typedef pair<int, int> pii;
typedef long long ll;
typedef long double ld;


string s;
int n;
int main (){
	int t; cin >> t;
	f (tt, 1, t+1){
		cin >> n >> s;
		int acc = 0;
		int ans = 0;
		f (i, 0, n+1){
			if (acc < i){
				ans += (i-acc);
				acc = i;
			}
			acc += (s[i]-'0');
		}
		printf("Case #%d: %d\n", tt, ans);
	}
	return 0;
}


