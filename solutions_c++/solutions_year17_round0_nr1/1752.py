#include<bits/stdc++.h>
using namespace std;
char ipt[1005];

void solve (int tc) {
	printf("Case #%d: ",tc);
	scanf("%s",ipt);
	int n = strlen(ipt), k, cnt = 0;
	scanf("%d",&k);
	for(int i=0;i<=n-k;i++) {
		if(ipt[i] == '-') {
			for(int j=i;j<i+k;j++) ipt[j] = (ipt[j] == '-' ? '+' : '-');
			cnt++;
		}
	}
	for(int i=0;i<n;i++) if(ipt[i] == '-') {puts("IMPOSSIBLE"); return;}
	printf("%d\n",cnt);
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int tc;
	scanf("%d",&tc);
	for(int i=1;i<=tc;i++) solve(i);
}
