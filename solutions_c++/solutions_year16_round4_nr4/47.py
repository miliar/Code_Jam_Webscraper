#include <bits/stdc++.h>
using namespace std;

const int MAXN = 100;
const int inf = 1000000000;

bool mark[MAXN];
bool adj[MAXN][MAXN];
int n;
string s[MAXN];

void main2(){
	cin >> n;
	int N = 2*n;
	for (int i=0; i<N; i++){
		for (int j=0; j<N; j++)
			adj[i][j] = 0;
		adj[i][i] = 1;
	}
	for (int i=0; i<n; i++){
		cin >> s[i];
		for (int j=0; j<n; j++){
			adj[i][j+n] = s[i][j]=='0' ? 0 : 1;
			adj[j+n][i] = adj[i][j+n];
		}
	}

	for (int k=0; k<N; k++)
		for (int i=0; i<N; i++)
			for (int j=0; j<N; j++)
				adj[i][j] = (adj[i][j]) || (adj[i][k] && adj[k][j]);

	int c01 = 0;
	int c10 = 0;
	vector< pair<int,int> > q;
	vector<int> edges;
	int res = 0;
	memset(mark, 0, sizeof mark);	
	for (int i=0; i<N; i++) if (mark[i] == false){
		int cnt_0 = 0;
		int cnt_1 = 0;
		for (int j=0; j<N; j++) if (adj[i][j] == 1){
			mark[j] = true;
			if (j<n)
				cnt_0++;
			else
				cnt_1++;
		}
		int cnt_edge = 0;
		for (int j=0; j<n; j++) if (adj[i][j] == true)
			for (int k=n; k<N; k++) if (adj[i][k] == true){
				if (s[j][k-n] == '1')
					cnt_edge++;
			}
		if (cnt_0==cnt_1){
			res+= cnt_0*cnt_0 - cnt_edge;
			continue;
		}
		if (cnt_0==0 && cnt_1==1)
			c01++;
		else if (cnt_0==1 && cnt_1==0)
			c10++;
		else{
			q.push_back(make_pair(cnt_0,cnt_1));
			edges.push_back(cnt_edge);
		}
	}

	int dp[(1<<(int)q.size())][c01+1][c10+1];

	for (int i=0; i<=c01; i++)
		for (int j=0; j<=c10; j++)
			dp[0][i][j] = ((i==j) ? i : inf);

	for (int mask=1; mask < (1<<(int)q.size()); mask++){
		for (int i=0; i<=c01; i++){
			for (int j=0;j<=c10; j++){
				dp[mask][i][j] = inf;
				for (int sub=mask; sub; sub=(sub-1)&mask){
					int first=0, second=0, total_edges=0;
					for (int iter=0; iter<(int)q.size(); iter++) if (sub & (1<<iter)){
						first += q[iter].first;
						second+= q[iter].second;
						total_edges+= edges[iter];
					}
					int new_i = i-max(0,first-second);
					int new_j = j-max(0,second-first);
					if (new_i<0 || new_j<0) continue;
					dp[mask][i][j] = min(dp[mask][i][j], dp[mask^sub][new_i][new_j] + max(first,second) * max(first,second) - total_edges);
				}
			}
		}
	}
	cout << res + dp[(1<<(int)q.size())-1][c01][c10] << endl;
}

int main(){
	int t; cin >> t;
	for (int o=1; o<=t; o++){
		cout << "Case #" << o << ": ";
		main2();
	}
	return 0;
}
