#include <bits/stdc++.h>
#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define FOR(i,l,r) for(int i=(l);i<=(r);i++)

//#define DEBUG
#ifdef DEBUG
#define print(...) fprintf(stderr, __VA_ARGS__)
#else
#define print(...) 
#endif
template<typename T,typename S>inline bool upmin(T&a,const S&b){return a>b?a=b,1:0;}
template<typename T,typename S>inline bool upmax(T&a,const S&b){return a<b?a=b,1:0;}
#define mmo(a,b) (((a)=1ll*(a)*(b)%mo)<0?(a)+=mo:(a))  //<--
#define buli(x) (__builtin_popcountll(x))
#define bur0(x) (__builtin_ctzll(x))
#define bul2(x) (63-__builtin_clzll(x))

using namespace std;
typedef long long LL;


char getLoser[256];
int proj[256];


int n,r,p,s;
string sort(const vector<char> &vc, int l, int r) {
	if (l==r) return string("")+vc[l];
	int mid=l+r>>1;
	string ls=sort(vc, l, mid);
	string rs=sort(vc, mid+1, r);
	return ls<rs ? ls+rs : rs+ls;
}
void solve(char c, string &line, int gs[]) {
	FOR (i,0,2) gs[i]=0;
	vector<char> vc[2]; int p=0; vc[p].clear();
	vc[p].pb(c);
	for (int z=2;z<=n;z<<=1) {  //
		p=!p; vc[p].clear();
		for (int i=0;i<vc[1-p].size();i++) {
			vc[p].pb(vc[1-p][i]);
			vc[p].pb(getLoser[vc[1-p][i]]);
		}
	}
	line = sort(vc[p], 0, vc[p].size()-1);
	for (int i=0;i<line.size();i++) gs[proj[line[i]]]++;
}

string line[3];
int gs[3][3];
bool vis[20];
string n_line[20][3];
int n_gs[20][3][3];
int main() {
	getLoser['P'] = 'R';
	getLoser['R'] = 'S';
	getLoser['S'] = 'P';
	proj['P'] = 0;
	proj['R'] = 1;
	proj['S'] = 2;

	//基于N的预处理

	int T; scanf("%d",&T);
	for (int tt=1;T--;tt++) {
		scanf("%d%d%d%d",&n,&r,&p,&s);
		int nn=n;
		if (!vis[n]) {
			vis[n]=1;
			n=1<<n;
			solve('P', line[0], gs[0]);
			solve('R', line[1], gs[1]);
			solve('S', line[2], gs[2]);

			FOR (i,0,2) {
				n_line[nn][i]=line[i];
				FOR (j,0,2) n_gs[nn][i][j]=gs[i][j];
			}
		}

		//cout<<n<<endl;
		//cout<<line[0]<<" "<<line[1]<<" "<<line[2]<<endl;

		vector<string> ans;
		for (int i=0;i<3;i++)
			if (n_gs[nn][i][0]==p&&n_gs[nn][i][1]==r&&n_gs[nn][i][2]==s)
				ans.pb(n_line[nn][i]);

		printf("Case #%d: ", tt);
		if (ans.size() == 0) {
			puts("IMPOSSIBLE");
		}
		else {
			sort(ans.begin(), ans.end());
			puts(ans[0].c_str());
		}
	}
	return 0;
}
