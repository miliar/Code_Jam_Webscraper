#include<iostream>
#include<cstdlib>
#include<cstdio>
#include<cmath>
#include<cstring>
#include<vector>
#include<set>
#include<unordered_set>
#include<algorithm>
using namespace std;

int n, r, p, s;

bool cmp(vector<char> ans, int st, int l) {
	int k = l / 2;
	for(int i=0;i<k;i++) {
		if (ans[i+st] > ans[st+i+k]) return true;
	}
	return false;
}

void work() {
	scanf("%d%d%d%d",&n, &r, &p, &s);
	vector<int> rd;
	rd.push_back(0);rd.push_back(1);
	//r=0   s=1   p=2
	for(int i=1; i<n;i++) {
		int sz = rd.size();
		for(int j=sz / 2; j < sz;j++) {
			rd.push_back(rd[j]);
			rd.push_back((rd[j] + 1) % 3);
		}

	// cout << rd.size() << en/dl;
	}
	int cnt[3];
	memset(cnt,0,sizeof(cnt));
	for(int i=0;i<rd.size();i++) {
		// printf("=%d\n", rd[i]);
		cnt[rd[i]]++;
	}
	// printf("%d %d %d\n", cnt[0], c/nt[1], cnt[2]);
	int pp = -1;
	if (r==cnt[0] && s==cnt[1] && p==cnt[2]) {
		pp = 0;
	} else if (s==cnt[0] && p==cnt[1] && r==cnt[2]) {
		pp = 1;
	} else if (p==cnt[0] && r==cnt[1] && s==cnt[2]) {
		pp = 2;
	} 

	if (pp == -1) {
		printf("IMPOSSIBLE\n");
	} else {
		vector<char> ans;
		for(int i=0;i<rd.size();i++) {
			int x = (rd[i] + pp) % 3;
			if (x == 0) ans.push_back('R');
			else if (x == 1) ans.push_back('S');
			else if (x == 2) ans.push_back('P');
		}
		for(int i=1;i<=n;i++) {
			int kk = 1 << i;
			for(int j=0;j<ans.size();j+=kk) {
				if (cmp(ans, j, kk)) {
					for(int k = j;k<j+kk/2;k++) {
						swap(ans[k], ans[k+kk / 2]);
					}
				}
			}
		}
		for(int i=0;i<ans.size();i++) {
			printf("%c", ans[i]);
		}
		printf("\n");
	}

}

int main() {
	// freopen("input.txt","r",stdin);
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int t;
	scanf("%d\n", &t);
	for(int i=0;i<t;i++) {
		printf("Case #%d: ", i+1);
		work();
	}

	return 0;
}

