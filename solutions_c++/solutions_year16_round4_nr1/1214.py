#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<algorithm>
#include<cstring>
#include<vector>
#include<stack>
#include<queue>

using namespace std;

const int MOD=1000007;

char ans[5000];

int n, r, p, s, rcnt, pcnt, scnt;

void solve(char cur, int l, int r)
{
	//printf("cur=%c, l=%d r=%d\n", cur, l, r);
	if(l+1==r){
		if(cur=='R'){
			ans[l]='R';
			ans[r]='S';
			rcnt++;
			scnt++;
		}
		else if(cur=='P'){
			ans[l]='P';
			ans[r]='R';
			pcnt++;
			rcnt++;
		}
		else{
			ans[l]='P';
			ans[r]='S';
			pcnt++;
			scnt++;
		}
		return;
	}
	int mid=(l+r)/2;
	char curl, curr;
	if(cur=='R'){
		curl='R';
		curr='S';
	}
	else if(cur=='P'){
		curl='P';
		curr='R';
	}
	else{
		curl='P';
		curr='S';
	}
	solve(curl, l, mid);
	solve(curr, mid+1, r);
	int i, half=(r+1-l)/2;
	bool swappp=0;
	for(i=l;i<=mid;i++){
		if(ans[i]>ans[i+half]){
			swappp=1;
			break;
		}
	}
	if(swappp){
		for(i=l;i<=mid;i++){
			swap(ans[i], ans[i+half]);
		}
	}
}

void print()
{
	int i;
	for(i=0;i<n;i++) printf("%c", ans[i]);
	puts("");
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int t, cases, i;
	scanf("%d", &t);
	for(cases=1;cases<=t;cases++){
		scanf("%d %d %d %d", &n, &r, &p, &s);
		n=1<<n;
		printf("Case #%d: ", cases);
		rcnt=pcnt=scnt=0;
		solve('R', 0, n-1);
		if(rcnt==r&&pcnt==p&&scnt==s){
			print();
			continue;
		}
		rcnt=pcnt=scnt=0;
		solve('S', 0, n-1);
		if(rcnt==r&&pcnt==p&&scnt==s){
			print();
			continue;
		}
		rcnt=pcnt=scnt=0;
		solve('P', 0, n-1);
		if(rcnt==r&&pcnt==p&&scnt==s){
			print();
			continue;
		}
		puts("IMPOSSIBLE");
	}
	return 0;
}
