#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef pair<ll,int> pli;
int T,len;
char str[110];
ll s,end;

ll change(ll f,int l) {
	int ts[20];
	ll re=0;
	for(int i=0; i<len; i++) {
		ts[len-i-1] = f%10;
		f/=10;
	}
	reverse(ts,ts+l);
	for(int i=0; i<l; i++) ts[i] = 1-ts[i];
	for(int i=0; i<len; i++)
		re = re*10+ts[i];
	return re;
}

int bfs(ll v) {
	if(v == end) return 0;
	ll tmp;
	pli t;
	set<ll> m;
	m.insert(s);
	queue<pli> q;
	q.push(pli(s,0));
	while(!q.empty()) {
		t = q.front();
		for(int i=1; i<=len; i++){
			tmp = change(t.first,i);
			if(tmp == end) return t.second+1;
			if(m.find(tmp) == m.end()) {
				q.push(pli(tmp,t.second+1));
				m.insert(tmp);
			}
		}
		q.pop();
	}
	return -1;
}

int main() {
	scanf("%d",&T);
	for(int tt=1; tt<=T; tt++) {
		s=0;
		end = 0;
		scanf("%s",str);
		len = strlen(str);
		for(int i=0; i<len; i++) {
			s=s*10+(str[i] == '+'?1:0);
			end=end*10+1;
		}
		printf("Case #%d: %d\n",tt,bfs(s));
	}
}
