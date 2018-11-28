//---------------------------------------------------------------------
#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>

#include <vector>
#include <set>
#include <map>
#include <deque>
#include <string>
#include <bitset>

#include <algorithm>
#include <cmath>
using namespace std;


//---------------------------------------------------------------------

int const MAX_N = 1010;

double girl[MAX_N],boy[MAX_N];
int nnew[MAX_N];

int p[MAX_N],ans,num,flag[MAX_N];
vector<int> e[MAX_N];

int dfs(int v) {
	if (flag[v]==num) return 0;
	flag[v]=num;
	for (int i=0; i<(int) e[v].size(); i++)
		if (p[e[v][i]]==-1 || dfs(p[e[v][i]])) {
			p[e[v][i]]=v;
			return 1;
		}
	return 0;
}

int main() {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int t;
	scanf("%d",&t);
	for (int qq=0; qq<t; qq++) {
		int n;
		scanf("%d",&n);
		for (int i=0; i<n; i++) scanf("%lf",&girl[i]);
		for (int i=0; i<n; i++) scanf("%lf",&boy[i]);
		sort(girl,girl+n);
		sort(boy,boy+n);

		int score_unfair = 0;
		int j = 0, k = n-1;
		while (j<n && girl[j]<boy[k]) {
			int can_hap = 1;
			int jj = j, kk = 0;
			while (jj < n) {
				if (girl[jj] > boy[kk]);
				else can_hap = 0;
				jj++;
				kk++;
			}
			if (can_hap)
				break;
			j++;
			k--;
		}
		while (j<n) {score_unfair++; j++;}

		int score_fair = 0;
		j = 0;
		for (int i=0; i<n; i++) nnew[i] = 0;
		while (j < n) {
			int is_ok = 0;
			for (int q=0; q<n; q++)
				if (boy[q] > girl[j] && !nnew[q]) {
					nnew[q] = 1;
					is_ok = 1;
					break;
				}
			if (!is_ok) {
				while (j<n) {
					score_fair++;
					j++;
				}
				break;
			}
			j++;
		}

		int new_score_unfair = 0;
		j = 0, k = n-1;
		int mx_gr = n;
		while (j<mx_gr) {
			if (girl[j] < boy[k]) {
				j++;
				k--;
			}
			else
				if (girl[mx_gr-1] > boy[k]) {
					mx_gr--;
					k--;
					new_score_unfair++;
				}
		}
		while (j<mx_gr) {new_score_unfair++; j++;}

		score_unfair = max(score_unfair, new_score_unfair);

		//
		for (int i=0; i<n; i++)
			e[i].clear();
		for (int i=0; i<n; i++)
			for (int j=0; j<n; j++)
				if (girl[i] > boy[j])
					e[i].push_back(j);
		for (int i=0; i<n; i++) {
			p[i]=-1;
			nnew[i] = 0;
		}
		ans = 0;
		for (int i=0; i<n; i++)
			if (!nnew[i])
				for (int j=0; j<(int) e[i].size(); j++)
					if (p[e[i][j]]==-1) {
						p[e[i][j]]=i;
						nnew[i]=1;
						ans++;
						break;
					}
		for (int i=0; i<n; i++)
			if (!nnew[i]) {
				num++;
				ans+=dfs(i);
			}
		//

		score_unfair = max(score_unfair, ans);

		printf("Case #%d: %d %d\n",qq+1,score_unfair,score_fair);
	}

	return 0;
}