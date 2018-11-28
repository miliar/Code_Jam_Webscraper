// TwT514 {{{
#include <bits/stdc++.h>
#define SZ(x) ((int)(x).size())
#define FOR(i,c) for (auto i=(c).begin(); i!=(c).end(); i++)
#define REP(i,n) for (int i=0; i<(n); i++)
#define REP1(i,a,b) for (int i=(int)(a); i<=(int)(b); i++)
#define ALL(x) (x).begin(),(x).end()
#define MS0(x,n) memset(x,0,(n)*sizeof(*x))
#define MS1(x,n) memset(x,-1,(n)*sizeof(*x))
#define MP make_pair
#define PB push_back
#define RI(a) scanf("%d",&(a))
#define RII(a,b) scanf("%d%d",&(a),&(b))
#define RIII(a,b,c) scanf("%d%d%d",&(a),&(b),&(c))
using namespace std;
typedef long long LL;
typedef pair<int,int> PII;
typedef vector<int> VI;
// }}}

#define N 1010
#define L 110
#define MOD 1000000007

struct Node{
	Node* c[26];
	bool has;
	int ct;
	LL ans1, ans2;
	Node(){
		REP(i,26) c[i]=NULL;
		has = false;
		ct = 0;
		ans1 = ans2 = 0;
	}
	void free(){
		REP(i,26){
			if(c[i]==NULL) continue;
			c[i]->free();
			delete c[i];
		}	
	}
};

int n, m;
char s[N][L];
void input(){
	RII(n,m);
	REP(i,n) scanf("%s",s[i]);
}

Node* root;

void build(){
	root = new Node();

	REP(i,n){
		int l = strlen(s[i]);		
		Node* now = root;
		now->ct++;
		REP(j,l){
			int k = s[i][j]-'A';
			if(now->c[k]==NULL) now->c[k] = new Node();
			now = now->c[k];
			now->ct++;
		}
		now->has = true;
	}
}


void free(){
	root->free();
	delete root;
}

LL C[L][L];
LL predo(){
	REP(i,L) C[i][0] = C[i][i] = 1;
	REP(i,L) for(int j=1; j<i; j++) C[i][j] = (C[i-1][j-1] + C[i-1][j])%MOD;
}

LL dp[30][L];

void go(Node& now){
	now.ans1 = 0;
	now.ans2 = 1;
	bool big = false;
	REP(i,26){
		if(now.c[i]==NULL) continue;
		go(*now.c[i]);
		now.ans1 += now.c[i]->ans1;
		if(now.c[i]->ct >= m) big = true;
	}
	
	now.ans1 += min(now.ct, m);
	LL& x = now.ans2;				
	if(now.ct<=m){
		int rem = now.ct;
		if(now.has){ x*=rem; rem--; }
		REP(i,26){
			if(now.c[i]==NULL) continue;
			int k = now.c[i]->ct;
			x = (x*C[rem][k])%MOD;
			rem-=k;
		}
	}
	else if(big){
		if(now.has) x*=m;
		REP(i,26){
			if(now.c[i]==NULL) continue;
			int k = min(now.c[i]->ct, m);
			x = (x*C[m][k])%MOD;
		}
	}
	else{
		int lv = 0;
		REP(i, m+1) dp[lv][i] = 0;
		if(now.has) dp[lv][1] = m;
		else dp[lv][0] = 1;

		REP(i,26){
			if(now.c[i]==NULL) continue;
			int k = now.c[i]->ct;
			lv++;
			for(int sm = m; sm>=0; sm--){
				dp[lv][sm] = 0;
				for(int j=0; j<=sm; j++){
					int A = m-j, B = j;
					int a = sm-j, b = k-a; 
					if(a>=0 && a<=A && b>=0 && b<=B){
						dp[lv][sm] = (dp[lv][sm] + dp[lv-1][j] * (C[A][a]*C[B][b]%MOD))%MOD;
					}
				}	
			}
			//REP(j, m+1) cout << dp[lv][j] << ' '; cout << endl;
		}	
		x = dp[lv][min(now.ct, m)];
	}
	REP(i, 26){
		if(now.c[i]==NULL) continue;
		x = (x*now.c[i]->ans2)%MOD;
	}
	//cout << "---" << now.ans1 << ',' << now.ans2 << endl;
}

void solve(){
	static int zi = 0;
	go(*root);
	printf("Case #%d: ",++zi);
	cout << root->ans1 << ' ' << root->ans2 << endl;
}

int main() {
	predo();
	int zn;
	RI(zn);
	while(zn--){
		input();
		//cout <<"XD" << zn << endl;
		build();
		solve();
		free();
	}
    return 0;
}

