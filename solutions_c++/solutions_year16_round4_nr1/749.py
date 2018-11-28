#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <cstring>
#include <map>
#include <cstdlib>
#include <ctime>
#include <cassert>
#include <bitset>
#define f first
#define s second
#define ll long long
#define ull unsigned long long
#define mp make_pair
#define pb push_back
#define vi vector <int>
#define ld long double
#define pii pair<int, int>
using namespace std;    
const int N = int(3e5), mod = int(1e9)  + 7;
int T;
string s;
string ans;
int n,r,p,k;
int len,pos;
int cnt[N];
bool ok;
string dp[5000][400];
bool was[5000][400];

string rec(int v,char c){
	if(v == n + 1){
		if(c == 'P') return "P";
		if(c == 'R') return "R";
		if(c == 'S') return "S";
	}
	if(was[v][c]) return dp[v][c];
	was[v][c] = 1;
	if(c == 'P'){
		return dp[v][c] = min(rec(v+1,'P') + rec(v+1,'R'),rec(v+1,'R') + rec(v+1,'P'));
	}
	else if(c == 'R'){
		return dp[v][c] = min(rec(v+1,'S') + rec(v+1,'R'),rec(v+1,'R') + rec(v+1,'S'));
	}
	else{
		return dp[v][c] = min(rec(v+1,'P') + rec(v+1,'S'),rec(v+1,'S') + rec(v+1,'P'));
	}
}

void rec1(int v,char c){
	if(v == n + 1){
		cnt[c]++;
		return;
	}
	if(c == 'P'){
		rec1(v+1,'P');
		rec1(v+1,'R');
	}
	else if(c == 'R'){
		rec1(v+1,'S');
		rec1(v+1,'R');
	}
	else{
		rec1(v+1,'P');
		rec1(v+1,'S');
	}
}


int main () {
	freopen("in","r",stdin);
	freopen("out","w",stdout);
	scanf("%d",&T);
	for(int tt=1;tt<=T;tt++){
		printf("Case #%d: ",tt);
		memset(was,0,sizeof(was));
		scanf("%d%d%d%d",&n,&r,&p,&k);
		len = 0;
		cnt['P'] = cnt['R'] = cnt['S'] = 0;
		s = rec(1,'P');
		rec1(1,'P');
		ans = "";
		if(cnt['P'] == p && cnt['R'] == r &&  cnt['S'] == k){
			ans = s;
		}
		cnt['P'] = cnt['R'] = cnt['S'] = 0;
		s = rec(1,'R');
		rec1(1,'R');
		if(cnt['P'] == p && cnt['R'] == r &&  cnt['S'] == k){
			if(ans.size() == 0 || ans > s){
				ans = s;
			}
		}
		cnt['P'] = cnt['R'] = cnt['S'] = 0;
		len = 0;
		s = rec(1,'S');
		rec1(1,'S');
		if(cnt['P'] == p && cnt['R'] == r &&  cnt['S'] == k){
			if(ans.size() == 0 || ans > s){
				ans = s;
			}
		}
		if(ans.size() == 0){
		    ans = "IMPOSSIBLE";
		}
		cout << ans << endl;
	}

return 0;
}