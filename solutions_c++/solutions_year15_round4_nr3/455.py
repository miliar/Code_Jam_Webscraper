#include<cstdio>
#include<algorithm>
#include<vector>
#include<cstring>
#include<set>
#include<assert.h>
using namespace std;
#define FOR(i,a,b) for(int i = a; i <= b; ++i)
#define FORD(i,a,b) for(int i = a; i >= b; --i)
#define REP(i,n) FOR(i,0,(n)-1)
#define RI(i,n) FOR(i,1,n)
#define pb push_back
#define mp make_pair
#define st first
#define nd second
#define mini(a,b) a=min(a,b)
#define maxi(a,b) a=max(a,b)
bool debug;
typedef vector<int> vi;
typedef long long ll;
typedef unsigned long long llu;
typedef long double ld;
typedef pair<int,int> pii;
const int inf = 1e9 + 5;
const int nax = 1000;
const int P = 1000033;

set<llu> secik1, secik2;
int testy,n,akt_res,res;
char t[nax];
vector<llu> wyn[nax];

bool wczytaj() {
	int wsk = 0;
	scanf(" %c",&t[wsk]);
	while (t[wsk] <= 'z' && t[wsk] >= 'a')
		scanf("%c",&t[++wsk]);
	
	bool rres = true;
	if (t[wsk] == '\n')
		rres = false;
	t[wsk] = 0;
	return rres;
}

void luj_was_ze_taki_input_dajecie(int kt) {
	wyn[kt].clear();
	while(true) {
		bool kupa = wczytaj();
		int wsk = 0;
		llu hasz = 0;
		while (t[wsk]) {
			//printf("%c",t[wsk]);
			hasz = hasz * P + t[wsk++];
		}
		
		//printf("|\n");
		wyn[kt].pb(hasz);
		
		if (!kupa)
			break;
	}
}

void siekaj(int p) {
	if (p > n) 
		res = min(res, akt_res);
	
	if (akt_res >= res)
		return;
	
	vector<llu> pom;
	int akt_pom = 0;
	for (auto i: wyn[p]) {
		if (secik1.find(i) == secik1.end()) {
			secik1.insert(i);
			pom.pb(i);
			
			akt_pom += secik2.find(i) != secik2.end();
		} 
	}
	akt_res += akt_pom;
	siekaj(p+1);
	
	for (auto i: pom)
		secik1.erase(i);
	
	pom.clear();
	akt_res -= akt_pom;
	
	//drugie
	akt_pom = 0;
	for (auto i: wyn[p]) {
		if (secik2.find(i) == secik2.end()) {
			secik2.insert(i);
			pom.pb(i);
			
			akt_pom += secik1.find(i) != secik1.end();
		} 
	}
	akt_res += akt_pom;
	siekaj(p+1);
	
	for (auto i: pom)
		secik2.erase(i);
	
	pom.clear();
	akt_res -= akt_pom;
	
}

int main(int argc, char * argv[]) {
	debug = argc > 1;
	scanf("%d",&testy);
	FOR(g,1,testy) {
		printf("Case #%d: ",g);
		scanf("%d",&n);
		FOR(i,1,n)
			luj_was_ze_taki_input_dajecie(i);
		
		//FOR(i,1,n) { for (auto j: wyn[i]) printf("%llu ",j); puts(""); }
			
		secik1.clear(), secik2.clear();
		for (auto i: wyn[1])
			secik1.insert(i);
			
		akt_res = 0;
		for (auto i: wyn[2]) if (secik2.find(i) == secik2.end()) {
			akt_res += secik1.find(i) != secik1.end();
			secik2.insert(i);
		}
		
		res = inf;
		siekaj(3);
		printf("%d\n",res);
	}
	return 0;
}
