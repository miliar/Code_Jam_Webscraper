#include <bits/stdc++.h>

using namespace std;

#define fr(a,b,c) for(int (a) = (b); (a) < (c); ++(a))
#define rp(a,b) fr(a,0,b)
#define fre(a,b) for(int a = adj[b]; ~a; a = ant[a])
#define cl(a,b) memset((a), (b), sizeof(a))
#define sc(a) scanf("%d", &a)
#define sc2(a,b) scanf("%d%d", &a, &b)
#define sc3(a,b,c) scanf("%d%d%d", &a, &b, &c)
#define scs(s) scanf("%s", s)
#define pri(x) printf("%d\n", x)

#define iter(a) __typeof((a).begin())
#define fore(a,b) for(iter(b) a = (b).begin(); a != (b).end(); ++a)

#define st first
#define nd second
#define mp make_pair
#define pb push_back

#define db(x) cerr << #x << " == " << x << endl
#define dbs(x) cerr << x << endl
#define _ << ", " <<

const int oo = 0x3f3f3f3f;

typedef long long ll;
typedef pair<int,int> pii;
typedef vector<int> vi;
typedef vector< vi > vii;

#define N 10009
#define M 100009
int an, adj[N], to[M], ant[M];

void add(int a, int b) {
	to[an] = b; ant[an] = adj[a]; adj[a] = an++;
}

map<string, int> mapa;

int n, cnt;

int find(string s) {
	if (!mapa.count(s)) mapa[s] = cnt++;
	//db(s _ mapa[s]);
	return mapa[s];
}

char buf[1000009], *p, *q;
int m[N][2];

int pd[23][1<<22];
int mark[23][1<<22], tempo;

int conta() {
	int ret = 0;
	fr(i, n, cnt) {
		if (m[i][0] > 0 && m[i][1] > 0) ret++;
	}
	return ret;
}

int go(int l, int msk) {
	int &ret = pd[l][msk];
	if (mark[l][msk] == tempo) return ret;
	mark[l][msk] = tempo;
	
	if (l == n) {
		ret = conta();
		//db(msk _ ret);
		return ret;
	}
	
	fre(it, l) m[to[it]][0]++;
	ret = go(l+1, msk);
	fre(it, l) m[to[it]][0]--;
	
	fre(it, l) m[to[it]][1]++;
	ret = min(ret, go(l+1, msk|(1<<l)));
	fre(it, l) m[to[it]][1]--;
	
	return ret;
}

int main() {
	cl(mark, 0);
	tempo = 0;
	int t, cn = 1;
	sc(t); while (t--) {
		printf("Case #%d: ", cn++);
		sc(n);
		
		cl(adj, -1);
		an= 0;
		cnt = n;
		mapa.clear();
		scanf("\n");
		
		rp(i, n) {
			scanf("%[^\n]\n", buf);
			p = buf;
			while (1) {
				q = p;
				while (isalpha(*q)) q++;
				
				int id = find(string(p, q));
				add(i, id);
				
				if (*q == 0) break;
				p = q+1;
			}
		}
		cl(m, 0);
		
		fre(it, 0) m[to[it]][0] = 1;
		fre(it, 1) m[to[it]][1] = 1;
		
		tempo++;
		int ans =go(2, 0);
		pri(ans);
	}
	return 0;
}
























