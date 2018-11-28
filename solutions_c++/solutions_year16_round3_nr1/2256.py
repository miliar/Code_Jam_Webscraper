#include <bits/stdc++.h>

using namespace std;

typedef vector<int> vi; 
typedef vector<vi> vvi;
typedef vector<string> vs;
typedef set<int> se;
typedef pair<int,int> pii;
typedef long long int tint;

#define forsn(i,s,n) for(int i = (int)(s); i<((int)n); i++)
#define dforsn(i,s,n) for(int i = (int)(n)-1; i>=((int)s); i--)
#define forn(i,n) for(int i=0;i<(int)(n);i++)
#define decl(v, c) typeof(c) v = c
#define forall(i, c) for(decl(i, c.begin()); i!=c.end(); ++i)
#define rall(c) (c).rbegin(), (c).rend()
#define all(c) (c).begin(), (c).end()
#define D(a) << #a << "=" << a << " "


#define si(a) int((a).size())
#define pb push_back
#define mp make_pair

int main () {
	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);
    
	ios_base::sync_with_stdio(false);
	
	int T; 
	
	cin >> T;
	
	forsn(cas,1,T+1) {
		int n; cin >> n;
		vi P(n,0);
		int sum = 0;
		
		forn(i,n) { cin >> P[i]; sum += P[i]; }
		
		cout << "Case #" << cas << ":";
				
		for(;;) {
			
			if (sum == 0) break;
			
			int a,b; a = -1; b = -1;
			forn(i,n) {
				if (a == -1 || P[i] > P[a]) { b = a; a = i; }
				else if (b == -1 || P[i] > P[b]) { b = i; }
			}
			
			if (P[b] == 0) {
				cout << " " << (char)('A'+a); break;						
			}
			if (P[a] == 1 && sum == 3) {
				cout << " " << (char)('A'+a); P[a]-- ; sum--; continue;
			}
			
			cout << " " << (char)('A'+a) << (char)('A'+b);
			P[a]--; P[b]--;	sum -=2;					
		}
		
		
		
		cout << endl;
	}
	

  return 0;

}


