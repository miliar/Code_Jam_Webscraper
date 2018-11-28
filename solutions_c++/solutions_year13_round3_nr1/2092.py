#include <vector>
#include <list>
#include <queue>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <malloc.h>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cstring>
#include <cctype>
#include <cmath>
#include <cstdlib>
#include <stdint.h>
#include <unistd.h>
#include <ctime>
#include <climits>
using namespace std;
#define EPS 		1e-8
#define FOR(i,a,b)  for(int i=(a);i<(b);i++)
#define F(i,a)      FOR(i,0,a)
#define PB          push_back
#define S           size()
#define MP          make_pair
#define MS(v, x)	memset(v, x, sizeof v)
#define ALL(v)      v.begin(),v.end()
#define LLA(v)      v.rbegin(),v.rend()
#define fi          first
#define se          second
#define NL 			printf("\n")
#define SP 			system("pause")
#define foreach(IT,C) for(typeof(C.begin())IT=C.begin();IT!=C.end();IT++)
const double PI = acos(-1.0);
int in(){int r=0,c;for(c=getchar();c<=32;c=getchar());if(c=='-') return -in();for(;c>32;r=(r<<1)+(r<<3)+c-'0',c=getchar());return r;}
typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<ii> vii;
typedef vector<string> vs;
typedef long long   LL;

void run() {
	string s;
	int n;
	LL ans = 0LL;
	cin >> s >> n;
	int l = s.S;
	int con = 0;
	bool sub = false;
	int prev = -1;
	int le, ri;
	F(i, l) {
		if(s[i] == 'a' || s[i] == 'e' || s[i] == 'i' || s[i] == 'o' || s[i] == 'u')
			con = 0;
		else con++;
		if(con == n) {
			ans += ((i-n-prev+1) * (l-i));
			prev = i-n+1;
			con--;
		}
	}
	printf("%lld\n", ans);
}

int main(){
	//freopen("asmall.in","r",stdin);
	//freopen("asmall.out","w",stdout);
	int t = in();
	FOR(i, 1, t+1) {
		printf("Case #%d: ", i);
		run();
	}
	return 0;
}




























//Author: Gabriel Menacho                      Nickname: tzyirvo.