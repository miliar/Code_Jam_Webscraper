#include <bits/stdc++.h>
#define PB push_back
#define MP make_pair
#define F first
#define S second
#define SZ(x) ((int)(x).size())
#define ALL(x) (x).begin(),(x).end()
#ifdef _DEBUG_
	#define debug(...) printf(__VA_ARGS__)
#else
	#define debug(...) (void)0
#endif
using namespace std;
typedef long long ll;
typedef pair<int,int> PII;
typedef vector<int> VI;

typedef pair<char,char> PCC;
const char *_win="PRSP";
char win(char c) { // who wins 'c'
	for(int i=1;;i++)
		if(_win[i]==c)
			return _win[i-1];
}
char lose(char c) { // who loses 'c'
	for(int i=0;;i++)
		if(_win[i]==c)
			return _win[i+1];
}
const int MAXN=14;
string all[3][MAXN];
int P[3][MAXN], R[3][MAXN], S[3][MAXN];

void ch(int s,int l,vector<PCC> &vec) {
	int ns=s+l;
	for(int i=0;i<l;i++) {
		if(vec[s+i]<vec[ns+i]) 
			return;
		else if(vec[s+i]>vec[ns+i]) {
			for(int k=0;k<l;k++)
				swap(vec[s+k],vec[ns+k]);
			return;
		}
	}
}

void go(int x,int y,vector<PCC> &vec) {
	for(int i=0;i<SZ(vec);i++)
		if(vec[i].F>vec[i].S)
			swap(vec[i].F,vec[i].S);
//	sort(ALL(vec));
	for(int i=1;i<SZ(vec);i*=2) {
		for(int j=0;j<SZ(vec);j+=i+i)
			ch(j,i,vec);
	}
	for(int i=0;i<SZ(vec);i++) {
		all[x][y]+=vec[i].F;
		all[x][y]+=vec[i].S;
	}
	for(char c:all[x][y])
		switch(c) {
			case 'P': P[x][y]++; break;
			case 'R': R[x][y]++; break;
			case 'S': S[x][y]++; break;
			default: assert(0);
		}
}

void init() {
	for(int i=0;i<3;i++) {
		vector<PCC> vec[MAXN];;
		vec[1].PB(MP(_win[i],lose(_win[i])));
		go(i,1,vec[1]);
		for(int j=2;j<MAXN;j++) {
			for(PCC u:vec[j-1]) {
				vec[j].PB(MP(u.F,lose(u.F)));
				vec[j].PB(MP(u.S,lose(u.S)));
			}
			go(i,j,vec[j]);
		}
	}
}

int main() {
	init();
	int all_kase;
	scanf("%d",&all_kase);
	for(int num_kase=1;num_kase<=all_kase;num_kase++) {
		int N,iR,iP,iS;
		scanf("%d%d%d%d",&N,&iR,&iP,&iS);
		printf("Case #%d: ",num_kase);
		bool yes=0;
		for(int i=0;i<3;i++) {
			if(iR==R[i][N] && iP==P[i][N] && iS==S[i][N]) {
				assert(!yes);
				cout << all[i][N] << '\n';
				yes=1;
			}
		}
		if(!yes)
			cout << "IMPOSSIBLE\n";
	}
	return 0;
}
