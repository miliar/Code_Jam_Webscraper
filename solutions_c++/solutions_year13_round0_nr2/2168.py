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
#define ALL(v)      v.begin(),v.end()
#define LLA(v)      v.rbegin(),v.rend()
#define fi          first
#define se          second
#define NL 			printf("\n")
#define SP 			system("pause")
#define foreach(IT,C) for(typeof(C.begin())IT=C.begin();IT!=C.end();IT++)
const double PI = acos(-1.0);
int in(){int r=0,c;for(c=getchar();c<=32;c=getchar());if(c=='-') return -in();for(;c>32;r=(r<<1)+(r<<3)+c-'0',c=getchar());return r;}
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int,int> ii;
typedef vector<ii> vii;
typedef vector<string> vstr;
typedef long long   LL;
//#define DEBUG
int cnt = 0;
int o[110][110];

void run() {
	int n = in(), m = in();
	vi ver(n, 0);
	vi hor(m, 0);
	F(i, n) F(j, m) {
        o[i][j] = in();
        ver[i] = max(ver[i], o[i][j]);
        hor[j] = max(hor[j], o[i][j]);
    }
    bool ans = true;
    for(int i = 0; ans && i < n; ++i) for(int j = 0; ans && j < m; ++j) {
        int aux = 100;
        aux = min(aux, min(ver[i], hor[j]));
        ans &= (aux == o[i][j]);
    }
	printf("Case #%d: %s\n", ++cnt, ans? "YES": "NO");
}

int main(){
	#ifdef DEBUG
		freopen("b_large_input.in","r",stdin);
		freopen("b_large_output.in","w",stdout);
		time_t st=clock();
	#endif
	int t = in();
	while(t--)
	run();
	#ifdef DEBUG
		//printf("=============\n");
		//printf("Time: %.2lf sec\n",(clock()-st)/double(CLOCKS_PER_SEC));
	#endif
	return 0;
}




























//Author: Gabriel Menacho                      Nickname: tzyirvo.
