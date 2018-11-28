#include <bits/stdc++.h>
using namespace std;
#define forn(i, n) for(int i = 0; i < (int) (n); i++)
#define dforn(i, n) for(int i = (n) - 1; i >= 0; i--)
typedef long long tint;
const string inf = "999999999999999999";
const string noinf = "000000000000000000";

struct par {
	string a, b;
};

int tc, n, TC;
int delta[3] = {-1, 0, 1};
string s, t;

vector<int> xx, yy;

// state = 0 no hay info sobre < o >
// state = 1 es >
// state = 2 es <

int numm(char c){
	return c - '0';
}

char charr(int c){
	return c + '0';
}

string DIF(string a, string b){
	if(a > b) swap(a, b);
	string ans;
	dforn(i, a.size()){
		// printf("Comparando %c vs %c\n", a[i], b[i]);
		if(a[i] > b[i]){
			int k = numm(b[i]) + 10;
			k -= numm(a[i]);
			b[i - 1]--;
			ans += charr(k);
			// printf("t1 %d\n", k);
		}
		else {
			int k = numm(b[i]) - numm(a[i]);
			ans += charr(k);
			// printf("t2 %d\n", k);
		}
	}
	reverse(ans.begin(), ans.end());
	return ans;
}

par mejor(par A, par B){
	string p, q;
	p = DIF(A.a, A.b);
	q = DIF(B.a, B.b);
	if( p < q ){
		return A;
	}
	else if( p == q ){
		if(A.a < B.a) return A;
		if(A.a == B.a){
			if(A.b < B.b) return A;
			return B;
		}
		return B;
	}
	return B;
} 

par solve(string &a, string &b, int pos, int state){
	if(pos == n){
		par z;
		z.a = a;
		z.b = b;
		return z;
	}
	par ans;
	
	char c, d;
	c = a[pos];
	d = b[pos];
	
	if(c != '?' && d != '?'){
		if(state){
			return solve(a, b, pos + 1, state);
		}
		else {
			int st = 0;
			if(c > d) st = 1;
			else if(c < d) st = 2;
			return solve(a, b, pos + 1, st);
		}
	}
	
	ans.a = inf;
	ans.b = noinf;
	
	if(state == 1){
		bool b1 = (a[pos] == '?');
		bool b2 = (b[pos] == '?');
		
		if(b1 && b2){
			a[pos] = '0';
			b[pos] = '9';
		}
		else if(b1){
			a[pos] = '0';
		}
		else if(b2){
			b[pos] = '9';
		}
		
		ans = mejor(ans, solve(a, b, pos + 1, state));
		
		if(b1 && b2){
			a[pos] = '?';
			b[pos] = '?';
		}
		else if(b1){
			a[pos] = '?';
		}
		else if(b2){
			b[pos] = '?';
		}
	}
	else if(state == 2){
		bool b1 = (a[pos] == '?');
		bool b2 = (b[pos] == '?');
		
		if(b1 && b2){
			a[pos] = '9';
			b[pos] = '0';
		}
		else if(b1){
			a[pos] = '9';
		}
		else if(b2){
			b[pos] = '0';
		}
		
		ans = mejor(ans, solve(a, b, pos + 1, state) );
		
		if(b1 && b2){
			a[pos] = '?';
			b[pos] = '?';
		}
		else if(b1){
			a[pos] = '?';
		}
		else if(b2){
			b[pos] = '?';
		}
	}
	else {
		bool b1 = (a[pos] == '?');
		bool b2 = (b[pos] == '?');
		
		if(b1 && b2){
			forn(i, 3){
				a[pos] = charr(xx[i]);
				b[pos] = charr(yy[i]);
				int st = 0;
				if(a[pos] > b[pos]) st = 1;
				if(a[pos] < b[pos]) st = 2;
				ans = mejor(ans, solve(a, b, pos + 1, st) );
			}
			
			a[pos] = '?';
			b[pos] = '?';
		}
		else if(b1){
			
			forn(i, 3){
				if( numm(b[pos]) + delta[i] >= 10 ) continue;
				if( numm(b[pos]) + delta[i] >= 0 ){
					a[pos] = charr( numm(b[pos]) + delta[i] );
					int st = 0;
					if(a[pos] > b[pos]) st = 1;
					if(a[pos] < b[pos]) st = 2;
					ans = mejor(ans, solve(a, b, pos + 1, st) );
				}
			}
		
			a[pos] = '?';
		}
		else if(b2){
			
			forn(i, 3){
				if( numm(a[pos]) + delta[i] >= 10) continue;
				if( numm(a[pos]) + delta[i] >= 0){
					b[pos] = charr( numm(a[pos]) + delta[i] );
					int st = 0;
					if(a[pos] > b[pos]) st = 1;
					if(a[pos] < b[pos]) st = 2;
					ans = mejor(ans, solve(a, b, pos + 1, st) );
				}
			}
		
			b[pos] = '?';
		}
	}
	return ans; 
}

int main(){
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);
	xx.push_back(0);
	xx.push_back(1);
	xx.push_back(0);
	yy.push_back(0);
	yy.push_back(0);
	yy.push_back(1);
	
	scanf("%d", &tc);
	while(tc--){
		cin >> s >> t; n = (int) s.size();
		par v = solve(s, t, 0, 0);
		printf("Case #%d: ", ++TC);
		cout << v.a << " " << v.b << endl;
	}
	return 0;
}
