#include<cstring>
#include<vector>
#include<cstdio>
#include<cassert>
#include<iostream>
#include<algorithm>
using namespace std;
bool isleaf[105*1000];
int next[105*1000][26];
int NODES=0;
int new_node() {
	int id=NODES++;
	memset(next[id],-1,sizeof next[id]);
	return id;
}
int go(int id, char c) {
	int & nxt = next[id][c-'A'];
	if (nxt==-1) nxt=new_node();
	return nxt;
}
const int mod = 1000000007;
vector<pair<int,int> > answer[105*1000]; // (opt.val, #ways (twee verschillende volgordes tellen voor 1))
int n,K;
int C[1025][1025];
int fac[1025];
int Comb(int n,int k) {
	assert(0 <= n && n <= 1010);
	assert(0 <= k && k <= 1010);
	return C[n][k];
}
int Fac(int n) {
	assert(0 <= n && n <= 1010);
	return fac[n];
}
inline void ADD(pair<int,int> & x, int yA, int yB) {
	if (yB == 0) return;
	if (x.second==0)x=make_pair(yA,yB); else
	if (yA >  x.first) x=make_pair(yA,yB); else
	if (yA == x.first) x.second=(x.second+yB)%mod;
}
void dp(int nodeID) { // return #nodes in subtree
	// for each k, return (max total #nodes, #ways such that this is reached) to partition leafs in this tree in k non-empty subsets.
	vector<pair<int,int> > cur (2);
	if (isleaf[nodeID]) {
		cur[0] = make_pair(0,0);
		cur[1] = make_pair(1,1);
	} else {
		cur[0] = make_pair(0,1);
		cur[1] = make_pair(0,0);
	}
	for (int c=0; c<26; c++) {
		if (next[nodeID][c] != -1) {
			dp(next[nodeID][c]);
			vector<pair<int,int> > subtree_result = answer[next[nodeID][c]];
			for (int i=0;i<(int)subtree_result.size();i++)subtree_result[i].first+=i;//add 1 for parent node
			// merge.
			int nA=(int)cur.size()-1;
			int nB=(int)subtree_result.size()-1;
			int mx=min(K, nA+nB);
			vector<pair<int,int> > cur2 (mx+1);
			for (int cntA=0; cntA<=nA; cntA++)if(cur[cntA].second>0)
			for (int cntB=0; cntB<=nB; cntB++)if(subtree_result[cntB].second>0)
			for (int cnt=max(cntA,cntB); cnt<=min(mx,cntA+cntB); cnt++)
			{
				int total=cntA+cntB;
				if (total < cnt) continue;
				int pairs = cntA+cntB-cnt;
				int total_node_count = cur[cntA].first+subtree_result[cntB].first-pairs;
				ADD(cur2[cnt], total_node_count, (long long)cur[cntA].second%mod*subtree_result[cntB].second%mod*Comb(cntA,pairs)%mod*Comb(cntB,pairs)%mod*Fac(pairs)%mod);// C(cntA,pairs)*C(cntB,pairs)*factorial(pairs).
			}
			cur = cur2;
		}
	}
	answer[nodeID] = cur;
}
int main() {
	freopen("D.in","r",stdin);
	fac[0]=1;
	for(int i=1;i<=1010;i++)fac[i]=(long long)fac[i-1]*i%mod;
	memset(C,0,sizeof C);
	C[0][0]=1;
	for (int N=1;N<=1010;N++){
		C[N][0]=C[N][N]=1;
		for(int K=1;K<N;K++){
			C[N][K]=(C[N-1][K-1]+C[N-1][K])%mod;
		}
	}
	int T;
	//T=100;
	scanf("%d",&T);
	for (int tc=1; tc<=T; tc++) {
		fprintf(stderr,"doing case#%d\n",tc);
		scanf("%d%d",&n,&K);
		//n=1000;
		//K=100;
		NODES=0;
		memset(isleaf,0,sizeof isleaf);
		int root = new_node();
		for (int i=0; i<n; i++) {
			string s;
			cin >> s;
			//if(i<100){for(int j=0;j<i;j++)s+='A'; s+='B';}
			//else for(int i=0;i<100;i++)s+='A'+rand()%26;
			int at = root;
			for (string::iterator it=s.begin(); it!=s.end(); ++it) {
				char c = *it;
				at = go(at, c);
			}
			isleaf[at] = true;
		}
		//printf("dp\n");
		dp(root);
		int mx=0;
		for (int i=0;i<(int)answer[root].size();i++)if(answer[root][i].second > 0)mx=max(mx,answer[root][i].first);
		int totalways=0;
		for (int i=0;i<(int)answer[root].size();i++)if(answer[root][i].first==mx) {
			int ways=answer[root][i].second;
			ways=(long long)ways*Fac(i)%mod;
			ways=(long long)ways*C[K][i]%mod;
			totalways+=ways;
			totalways%=mod;
		}
		printf("Case #%d: %d %d\n",tc,mx,totalways);
		fprintf(stderr,"%d\n",totalways);
	}
}
