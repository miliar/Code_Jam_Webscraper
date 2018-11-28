#include <bits/stdc++.h>
using namespace std;


#define forn(i,n) for(int i=0;i<(int)(n);i++)
#define si(c) ((int)(c).size())
#define forsn(i,s,n) for(int i = (int)(s); i<((int)n); i++)
#define dforsn(i,s,n) for(int i = (int)(n)-1; i>=((int)s); i--)
#define decl(v, c) typeof(c) v = c
#define forall(i, c) for(decl(i, c.begin()); i!=c.end(); ++i)
#define dforall(i, c) for(decl(i, c.rbegin()); i!=c.rend(); ++i)
#define all(c) (c).begin(), (c).end()
#define rall(c) (c).rbegin(), (c).rend()
#define D(a) cerr << #a << "=" << a << endl;
#define pb push_back
#define mp make_pair


typedef long long int tint;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<tint> vt;
typedef vector<vt> vvt;
typedef vector<double> vd;
typedef vector<vd> vvd;
typedef vector<bool> vb;
typedef vector<vb> vvb;
typedef vector<string> vs;
typedef pair<int,int> pii;

struct trie {
	typedef map<char,trie*> hijos;
	hijos child;
	bool final;
	
	trie() {
		final = false;
	}
	
	void insert(const string &s) {
		trie *now = this;
		int n = si(s);
		forn(i,n) {
			// actualizar data del nodo
			
			if (!(now->child.count(s[i]))) 
				now->child[s[i]] = new trie();
				
			now = now->child[s[i]];			
		}
		now->final = true; // o arco a '$'		
	}
	
	void clear() {
		for (hijos::iterator it = child.begin(); it != child.end(); it++) {
			it->second->clear();					
		}
		child.clear();
	}

	int cnt() {
		int res = 0;
		for (hijos::iterator it = child.begin(); it != child.end(); it++) {
			res += it->second->cnt();
		}
		return res+1;
	}
	
};

int m,n;
string s[10];
int cnt[1<<10];

int t[10];
int mcost = -1, rcnt = 0;
void go(int from) {
	if (from == m) {
		int cost = 0;
		forn(ti,n) {
			int mask = 0;
			forn(i,m) if (t[i] == ti) mask |= 1<<i;
			if (mask == 0) { cost = -1; break; }
			cost += cnt[mask];
		}
		if (cost > mcost) {
			mcost = cost;
			rcnt = 1;
		}
		else if (cost == mcost) rcnt++;
		return ;
	}
	forn(as,n) {
		t[from] = as;
		go(from+1);
	}	
}

int main() {
        freopen("in.txt","r",stdin);
        freopen("out.txt","w",stdout);

        int ncas; cin >> ncas;
        forn(cas, ncas) {
        	cout << "Case #" << cas+1 << ": ";
        	cin >> m >> n;
        	forn(i,m) cin >> s[i];

        	trie t;
        	forn(mask,1<<m) {
        		t.clear();
        		forn(i,m) if (mask & (1<<i)) t.insert(s[i]);
        		cnt[mask] = t.cnt();
        		// cerr << mask << ' ' << cnt[mask] << endl;
        	}

        	mcost = -1; rcnt = 0; go(0);
        	cout << mcost << ' ' << rcnt << endl;

        }

        return 0;
}
