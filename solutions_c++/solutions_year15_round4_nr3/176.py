#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
#include<map>
#include<vector>
using namespace std;

int n,totw;
char str[100005];
vector<int> v[205];
map<string,int> m;
int w[10005];

int main() {
	int tc;
	scanf("%d",&tc);
	for (int t=1; t<=tc; t++) {
		scanf("%d\n",&n);
		totw = 0;
		m.clear();
		for (int i=0; i<n; i++) {
			v[i].clear();
			gets(str);
			int x = 0,id;
			char ts[1005];
			while (sscanf(str+x,"%s%n",ts,&id) == 1) {
				if (m.find(ts) != m.end()) v[i].push_back(m[ts]);
				else {
					v[i].push_back(totw);
					m[ts] = totw++;
				}
				x += id;
			}
		}
		/*
		for (int i=0; i<n; i++) {
			for (int j=0; j<v[i].size(); j++)
				printf("%d ",v[i][j]);
			printf("\n");
		}
		*/
		int ret = totw;
		for (int i=0; i<(1<<(n-2)); i++) {
			memset(w,0,sizeof(w));
			for (int j=0; j<v[0].size(); j++) w[v[0][j]] |= 1;
			for (int j=0; j<v[1].size(); j++) w[v[1][j]] |= 2;
			for (int k=2; k<n; k++) {
				if ((1<<(k-2)) & i) {
					for (int j=0; j<v[k].size(); j++) w[v[k][j]] |= 1;
				}
				else {
					for (int j=0; j<v[k].size(); j++) w[v[k][j]] |= 2;
				}
			}
			int cnt = 0;
			for (int j=0; j<totw; j++) if (w[j] == 3) cnt++;
			ret = min(cnt,ret);
		}
		printf("Case #%d: %d\n",t,ret);
	}
    return 0;
}
