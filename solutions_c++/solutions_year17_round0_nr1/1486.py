#include <bits/stdc++.h>
#define loop(i,n) for(int i = 0;i < (n);i++)
#define range(i,a,b) for(int i = (a);i <= (b);i++)
#define all(A) A.begin(),A.end()
#define pb push_back
#define mp make_pair
#define sz(A) ((int)A.size())
#define vi vector<int>
#define vl vector<long long>
#define vd vector<double>
#define vp vector<pair<int,int> >
#define ll long long
#define pi pair<int,int>
#define popcnt(x) __builtin_popcount(x)
#define LSOne(x) ((x) & (-(x)))
#define xx first
#define yy second
#define PQ priority_queue
#define print(A,t) cerr << #A << ": "; copy(all(A),ostream_iterator<t>(cerr," " )); cerr << endl
#define prp(p) cerr << "(" << (p).first << " ," << (p).second << ")";
#define prArr(A,n,t)  cerr << #A << ": "; copy(A,A + n,ostream_iterator<t>(cerr," " )); cerr << endl
#define PRESTDIO() cin.tie(0),cerr.tie(0),ios_base::sync_with_stdio(0)
#define what_is(x) cerr << #x << " is " << x << endl
#define bit_lg(x) (assert(x > 0),__builtin_ffsll(x) - 1)
const double PI = acos(-1);
//#define inp "input.in"
#define inp "A-large.in"
using namespace std;

char line[1024];
int K;

int main(){/*
	freopen("logger.out","w",stderr);
	#ifndef ONLINE_JUDGE
		freopen(inp, "r", stdin);
		freopen("output.out", "w", stdout);
	#endif*/
	int T; scanf("%d",&T);
	for(int t = 1;t <= T;t++){
		scanf("%s %d",line,&K);
		int L = strlen(line),ans = 0;
		for(int i = 0;i < L && ans >= 0;i++){
			if(line[i] == '-') {
				if(L - i >= K) {
					ans++;
					loop(j,K) line[i + j] = (line[i + j] == '-') ? '+' : '-';
				}
				else ans = -1;
			}
		}
		printf("Case #%d: ",t);
		if(ans == -1) puts("IMPOSSIBLE");
		else printf("%d\n",ans);
	}

	return 0;
}
