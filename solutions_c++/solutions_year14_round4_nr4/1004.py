#pragma comment(linker,"/STACK:300000000")
#include <iostream>
#include <fstream>
#include <stdio.h>
#include <algorithm>
#include <set>
#include <vector>
#include <map>
#include <queue>
#include <list>
#include <math.h>
#include <string>
#include <stdlib.h>
#include <stack>

#define gcd(a,b) __gcd((a),(b))
#define sqr(a) ((a)*(a))
#define odd(a) ((a)&1)
#define foru(i,n) for (int i=0;i<(n);i++)
#define ford(i,n) for (int i=(n)-1;i>=0;i--)
#define forab(i,l,r) for (int i=(l);i<=(r);i++)
#define forabd(i,r,l) for (int i=(r);i>=(l);i--)
#define fillchar(a,b) memset((a),(b),sizeof((a)))
#define pb push_back
#define F first
#define S second
#define all(x) x.begin,x.end
#define pw2(x) (1ull<<(x))
#define mp make_pair
#define filename "input"

const long double eps=1e-20;
const long double pi=acos(-1.0);
const long long inf=1000*1000*1000*1000*1000*1000;
const long long base=1000*1000*1000+7;

using namespace std;

int test = 1;

struct pp{
	int next[26];		
};
string sq[1111];
int n,m;

pp trie[4][1111];
int last[4];
int ans1, ans2;
int o[1111];
int tmp1;

void init(pp &a){
	foru(i,26) a.next[i] = -1;
}


void add(int pos, string s){
	int st = 0;
	foru(i,s.size()){
		if (trie[pos][st].next[s[i] - 'A'] == -1){
			last[pos]++;
			init(trie[pos][last[pos]]);
			trie[pos][st].next[s[i] - 'A'] = last[pos];
			st = last[pos];
		} else st = trie[pos][st].next[s[i] - 'A'];
	}	
}


void countt(){
	foru(i,m) init(trie[i][0]);	
	foru(i,m) last[i] = 0;
	foru(i,n) add(o[i], sq[i]);
	foru(i,m) if (last[i] == 0) return;
	foru(i,m) tmp1 += last[i] + 1;
}

void rec(int pos){
	if (pos == n){
		tmp1 = 0;
		countt();
		if (tmp1 == ans1) ans2++;
		else if (tmp1 > ans1){
			ans1 = tmp1;
			ans2 = 1;
		}
		return;
	}
	foru(i,m){
		o[pos] = i;
		rec(pos + 1);
	}
}

void solve(){
	cin >> n >> m;
	ans1 = 0;
	ans2 = 0;
	foru(i,n) cin >> sq[i];
	rec(0);
	cout << ans1 << " " << ans2 << endl;
}


int main(){
	freopen (filename".in","r",stdin);
	freopen (filename".out","w",stdout);
	ios_base :: sync_with_stdio(false);
	cin >> test;
	for (int tt = 1; tt <= test; tt++){
		cout << "Case #" << tt << ": ";
		solve();
	}
	return 0;
}
