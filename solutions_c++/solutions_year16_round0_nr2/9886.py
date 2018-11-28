#include <bits/stdc++.h>
using namespace std;
#define all(x) (x).begin(),(x).end()
#define sz(x) (int)(x).size()
#define ll long long
#define ii pair<int,int>
#define mp make_pair
#define pb push_back
#define INF 1000000000
int dist[1030];
char s[15];
int tmp[15],tc;
queue<int> q;
int main() {
	scanf("%d",&tc);
	for (int kk=0;kk<tc;kk++) {
		scanf("%s",s);
		int n=strlen(s);
		int b=0;
		for (int i=0;i<(1<<n);i++) dist[i]=INF;
		for (int i=0;i<n;i++) {
			b|=((s[i]=='+')<<i);
		}
		while(!q.empty()) q.pop();
		q.push(b);
		dist[b]=0;
		while(!q.empty()) {
			int t=q.front();
			q.pop();
			memset(tmp,0,sizeof(tmp));
			for (int i=0;i<n;i++) {
				tmp[i]=!!(t&(1<<i));
			}
			for (int k=0;k<n;k++) {
				int c=0;
				for (int i=k;i>=0;i--) {
					c|=((!tmp[k-i])<<i);
				}
				for (int i=k+1;i<n;i++) {
					c|=(tmp[i]<<i);
				}
				if (dist[t]+1<dist[c]) {
					dist[c]=dist[t]+1;
					q.push(c);
				}
			}
		}
		printf("Case #%d: %d\n", kk+1,dist[(1<<n)-1]);
	}
}