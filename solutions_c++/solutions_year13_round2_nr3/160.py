#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <set>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

typedef long long LL;
typedef pair<int,int> PII;
typedef vector<int> VI;
typedef vector<string> VS;

#define rep(i,s,e) for(int i=s;i<e;i++)
#define sz(X) ((int)(X.size()))
#define tr(it,x) for(typeof(x.begin()) it=x.begin();it!=x.end();++it)
#define all(x) x.begin(),x.end()
#define clr(x,c) memset(x,c,sizeof(x))
//---------------------------------------------------------------


void find_max_length() {
	freopen("F:/TDDOWNLOAD/garbled_email_dictionary.txt", "r", stdin);
	string s; 
	int ma = 0;
	while(cin>>s) {
		ma = max(ma, (int)s.length());
	}
	printf("ma = %d\n", ma);
}

int dp[5000][5];

void check(int &a, int b){
	a = min(a, b);
}

int main() {
	freopen("F:/TDDOWNLOAD/C-large.in", "r", stdin);
	freopen("F:/TDDOWNLOAD/C-large.out", "w", stdout);

	//find_max_length();
	FILE *fp = fopen("F:/TDDOWNLOAD/garbled_email_dictionary.txt", "r");
	char ch[15];
	set<string> st;
	while(fscanf(fp, " %s", ch)!=EOF) {
		st.insert(ch);
	}
	//printf("st.size() = %d\n", st.size());


	int Te; scanf("%d", &Te);
	for(int te=1;te<=Te;te++) {

		char ch[5555];
		scanf(" %s", ch+1);

		memset(dp, 0x3f, sizeof(dp));
		dp[0][4] = 0;
		int len = strlen(ch+1);
		for(int i=0;i<len;i++) {
			for(int j=0;j<5;j++) if(dp[i][j] < 1000000) {
				for(int L=1;L<=10;L++) {
					if(i+L > len) break;
					string s = "";
					rep(x, 0, L) s += ch[i+1+x];

					if(st.find(s) != st.end()) { //no change 
						check(dp[i+L][min(4, j+L)], dp[i][j]);
					}
					rep(x, 0, sz(s)) { //one change
						if(x+1 + j<5) continue;
						rep(vx, 0, 26) {
							string ts = s;
							ts[x] = 'a'+vx;
							if(st.find(ts)!=st.end()) {
								check(dp[i+L][min(4, sz(s)-1-x)], dp[i][j]+1);
								break;
							}
						}
					}
					rep(x, 0, sz(s)) {
						if(x+1+j < 5) continue;
						rep(y, x+5, sz(s)) {
							rep(vx, 0, 26) rep(vy, 0, 26){
								string ts = s;
								ts[x] = 'a'+vx;
								ts[y] = 'a'+vy;
								if(st.find(ts)!=st.end()) {
									check(dp[i+L][min(4, sz(s)-1-y)], dp[i][j]+2);
									break;
								}
							}
						}
					}
				}
			}
		}

		printf("Case #%d: ", te);

		int ans = 1000000;
		rep(j, 0, 5) check(ans, dp[len][j]);
		printf("%d\n", ans);
	}
}