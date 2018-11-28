#include <stdio.h>
#include <iostream>
#include <stdlib.h>
#include <vector>
#include <string.h>
#include <queue>
#include <map>
#include <set>

using namespace std;

#define MAXN 15
#define INF 2000000000
typedef long long ll;
typedef pair <ll, ll> pp;
int C;
string s;
ll d[1<<MAXN];

ll change(int idx, ll num)
{
	ll res = num;
	for(int i=idx; i>=0; i--) {
		ll cu = (1<<(i));
		if((num & cu) == cu) res -= cu;
		else res += (1<<(idx-i));
	}
	return res;
}
int main(void) 
{
	cin >> C;
	for(int c=1; c<=C; c++) {
		int cnt = 0;
		cin >> s;
	//	if(c != 5) continue;
		ll st = 0;
		for(int i=0; i<(1<<(MAXN)); i++) d[i] = INF;
		for(int i=0; i<s.length(); i++) {
			 if(s[i] == '+') st += (1<<i);
			 cnt++;
		}
		
		ll tot = 1<<(cnt);
		tot--;
		queue <pp> q;
		q.push(pp(st, 0));
		while(!q.empty()) {
			ll cur = q.front().first;
			ll val = q.front().second;
		//	printf("%lld\n", cur);
			q.pop();
			if(val >= d[cur]) continue;
			d[cur] = val;
	//		printf("%lld %lld\n", cur, val);
			if(cur == tot) break;
			for(int i=0; i<cnt; i++) q.push(pp(change(i, cur), val+1));
		}
				
		printf("Case #%d: %lld\n", c, d[tot]);
	}
	
	return 0;
}
