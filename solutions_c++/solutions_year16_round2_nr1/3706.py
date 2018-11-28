#include <bits/stdc++.h>
#define _ printf("\n");
#define sc1(a) scanf("%d", &a)
#define sc2(a, b) scanf("%d%d", &a, &b)
#define sc3(a, b, c) scanf("%d%d%d", &a, &b, &c)
#define sc4(a, b, c, d) scanf("%d%d%d%d", &a, &b, &c, &d)
#define pb(a) push_back(a)
#define inf 0x3f3f3f3f
#define linf 0x3f3f3f3f3f3f3f3fLL
#define fr(i, a, n) for(int i = (a); (i) < (n); ++(i))
#define rp(a, b) fr(a, 0, b)
#define mp(a, b) make_pair(a, b)
#define st first
#define nd second
#define EPS 1e-9
#define clr(a, b) memset(a, b, sizeof(a))
#define addEdge(a, b, c) from[z] = a; to[z] = b; ant[z] = adj[a]; adj[a] = z; cost[z] = c; z++

using namespace std;
typedef vector<int> vi;
typedef long long int ll;
typedef pair<int, int> pii;
const double PI = acos(-1);

int v[30];
char s[2010];
string ans;
bool found;
string numb[] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};

void go(int n, string str) {
	//cout << n << " " << str << endl;
	if(n >= 10) {
		bool ok = 1;
		fr(i, 0, 30) {
			if(v[i] != 0) {
				ok = 0;
				break;
			}
		}
		if(ok) {
			found = 1;
			ans = str;
		}
		return;
	}
	bool exists = 1;
	int qtd = 0;
	
	go(n+1, str);
	while(exists && !found) {
		fr(j, 0, numb[n].length()) {
			if(v[numb[n][j]-'A'] <= 0) {
				exists = 0;
				break;
			}
		}
		if((n == 3 || n == 7) && v['E'-'A'] < 2) exists = 0;
		if(n == 9 && v['N'-'A'] < 2) exists = 0;
		
		if(exists) {
			fr(j, 0, numb[n].length()) v[numb[n][j]-'A']--;
			str.pb(char(n+'0'));
			go(n+1, str);
			qtd++;
			if(found) break;
		}
	}
	
	fr(j, 0, numb[n].length()) v[numb[n][j]-'A']+=qtd;
}

int main () {
	int t, caso = 0;
	sc1(t);
	
	while(t--) {
		//if(caso) puts("");
		caso++;
		scanf(" %s", s);
		fr(i, 0, 30) v[i] = 0;
		ans = "";
		
		for(int i = 0; s[i] != '\0'; i++) {
			v[s[i]-'A']++;
		}	
		found = 0;
		go(0, "");
	
		printf("Case #%d: %s\n", caso, ans.c_str());
	}
	
	return 0;
}













