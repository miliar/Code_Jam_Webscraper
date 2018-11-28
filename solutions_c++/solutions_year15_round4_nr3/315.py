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

#define N 300000
map <string, int> mapa;
int cnt;

int maps (string s){
	if (mapa.find(s) == mapa.end()) mapa[s] = cnt++;
	return mapa[s];
}

int  E[N], F[N];
int EE[N], FF[N];
char s[N];
char t[N];
int n;

vector <int> V[N];

int main (){
	int tt; scanf("%d ", &tt);
	f (kase, 1, tt+1){
		clr (E, 0); clr (F, 0);
		f (i, 0, N) V[i].clear();
		cnt = 1; mapa.clear();
		scanf("%d ", &n);
		n -= 2;
		fgets (s, 100000, stdin);
		int pos = 0, aux;
		while (sscanf(s+pos, "%s%n", t, &aux) == 1){
			string aa = ""; aa += t;
			pos += aux;
			E[maps(aa)] = 1;
		}
		pos = 0;
		fgets (s, 100000, stdin);
		while (sscanf(s+pos, "%s%n", t, &aux) == 1){
			string aa = ""; aa += t;
			pos += aux;
			F[maps(aa)] = 1;
		}
		f (i, 0, n){
			fgets (s, 1000, stdin);
			pos = 0;
			while (sscanf(s+pos, "%s%n", t, &aux) == 1){
				string aa = ""; aa += t;
				pos += aux;
				V[i].pb(maps(aa));
			}
		}
		int ans = 10*cnt;
		//f (i, 0, cnt) printf("%d ", E[i]); cout << endl;
		//f (i, 0, cnt) printf("%d ", F[i]); cout << endl;

		f (mask, 0, (1<<n)){
			f (i, 0, cnt) EE[i] = E[i];
			f (i, 0, cnt) FF[i] = F[i];
			f (i, 0, n){
				if (1&(mask>>i)){
					f (j, 0, V[i].size()) EE[V[i][j]] = 1;
				}
				else{
					f (j, 0, V[i].size()) FF[V[i][j]] = 1;
				}
			}
			int ret = 0;
			f (i, 0, cnt) if (EE[i] && FF[i]) ret++;
			ans = min(ans, ret);
		}
		printf("Case #%d: %d\n", kase, ans);

	}

	return 0;
}





