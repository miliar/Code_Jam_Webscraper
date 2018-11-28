#include<iostream>
#include<fstream>
#include<sstream>
#include<cstdio>
#include<climits>
#include<cstring>
#include<cstdlib>
#include<cassert>
#include<ctime>
#include<string>
#include<vector>
#include<algorithm>
#include<set>
#include<map>
#include<queue>
#include<utility>
#include<numeric>
#include<deque>
using namespace std;

typedef long long LL;
typedef vector<int>::iterator vii;
typedef map<int,int>::iterator mii;

string sss[10];
int cc[256];
int ans[10];

void dec(int x) {
    for (int i= 0; i<ans[x]; ++i)
        for (int j = 0; j<sss[x].length(); ++j) {
            cc[sss[x][j]]--;
        }
}

int main() {
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);
  sss[0] = "ZERO";
  sss[1] = "ONE";
  sss[2] = "TWO";
  sss[3] = "THREE";
  sss[4] = "FOUR";
  sss[5] = "FIVE";
  sss[6] = "SIX";
  sss[7] = "SEVEN";
  sss[8] = "EIGHT";
  sss[9] = "NINE";
    int T; cin>>T;
    string s;
    for (int loop = 1; loop<=T; ++loop) {
        printf("Case #%d: ", loop);
    	cin>>s;
    	int N = s.length();
    	memset(cc,0,sizeof(cc));
    	memset(ans,0,sizeof(ans));
    	for (int i = 0; i<N; ++i)
			cc[s[i]]++;
		ans[0] = cc['Z'];
		dec(0);
		ans[2] = cc['W'];
		dec(2);
		ans[4] = cc['U'];
		dec(4);
		ans[6] = cc['X'];
		dec(6);
		ans[8] = cc['G'];
		dec(8);
		ans[1] = cc['O'];
		dec(1);
		ans[3] = cc['H'];
		dec(3);
		ans[5] = cc['F'];
		dec(5);
		ans[7] = cc['S'];
		dec(7);
		ans[9] = cc['I'];
		dec(9);
		for (int i= 0; i<10; ++i)
		for (int j = 0; j<ans[i]; ++j)
		printf("%d",i);
		printf("\n");
		
    }
    return 0;
}

