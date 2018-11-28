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
#define MAX 10000010
int cnt = 0;
vector<LL> v;

bool isPalindrome(LL n) {
	stringstream ss;
	string s;
	ss << n;
	ss >> s;
	int ans = true;
	for(int i = 0, j = s.S - 1; ans && i < j; i++, j--)
		ans &= (s[i] == s[j]);
	return ans;
}

void init() {
	FOR(i, 1, MAX) {
		if(isPalindrome((LL) i)) {
			LL j = (LL) i * i;
			if(isPalindrome(j))
				v.PB(j);
		}
	}
}

void run() {
	LL A, B;
	scanf("%lld %lld", &A, &B);
	int sum = 0;
	F(i, v.S) {
		if(v[i] > B) break;
		if(v[i] >= A) sum++;
	}
	printf("Case #%d: %d\n", ++cnt, sum);
}

int main(){
	#ifdef DEBUG
		freopen("c_large1_input.in","r",stdin);
		freopen("c_large1_output.in","w",stdout);
		//freopen("sample.txt","r",stdin);
		time_t st=clock();
	#endif
	init();
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
