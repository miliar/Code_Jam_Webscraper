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
	LL a;
	int n;
	scanf("%lld %d", &a, &n);
	vector<LL> v;
	F(i, n) {
		LL aux;
		scanf("%lld", &aux);
		v.PB(aux);
	}
	sort(ALL(v));
	LL ans = 0, res = n;
	priority_queue<LL> q;
	F(i, n) {
		if(v[i] < a) {
			a += v[i];
			continue;
		}
		res = min(res, n - i + ans);
		if(a == 1LL) {
            ans = n - i + ans;
            break;
		}
		while(v[i] >= a) {
			a += (a - 1LL);
			ans++;
		}
		i--;
	}
	printf("%d\n", min(res, ans));
}

int main(){
	//freopen("alarge.in","r",stdin);
	//freopen("alarge.out","w",stdout);
	int t = in();
	FOR(i, 1, t+1) {
		printf("Case #%d: ", i);
		run();
	}
	return 0;
}

/*if(v[i] < a) {
			a += v[i];
			continue;
		}
		if(v[i] < a + a - 1LL) {
			a += (a - 1LL);
			i -= 1;
		} else{
			 ans += (n - i);
			 break;
		}
		ans++;*/


























//Author: Gabriel Menacho                      Nickname: tzyirvo.
