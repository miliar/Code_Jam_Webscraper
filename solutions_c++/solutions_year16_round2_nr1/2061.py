#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <string>
#include <vector>
#include <iostream>
#include <map>
#include <set>
#include <algorithm>
#include <queue>

using namespace std;

typedef long long ll;
const double pi = atan(1.0)*4.0;
ll gcd(ll x, ll y) { return y ? gcd(y, x%y) : x; }


int alphaCnt[26];

int main(){

//	freopen("A-large.in", "r", stdin);
//	freopen("A-large.out", "w", stdout);

	int T;
	scanf("%d",&T);

	for(int test_case = 1 ; test_case <= T ; test_case++){
		char s[2001];
		scanf("%s",s);
		int len = strlen(s);

		for(int i = 0 ; i < len ; i++){
			alphaCnt[(int)s[i]-'A']++;
		}

		vector<int> ans;
		if(alphaCnt[(int)'Z'-'A'] > 0){//0
			int cnt = alphaCnt[(int)'Z'-'A'];
			alphaCnt[(int)'Z'-'A'] -= cnt;
			alphaCnt[(int)'E'-'A'] -= cnt;
			alphaCnt[(int)'R'-'A'] -= cnt;
			alphaCnt[(int)'O'-'A'] -= cnt;
			for(int i = 0 ; i < cnt ; i++) ans.push_back(0);
		}
		if(alphaCnt[(int)'U'-'A'] > 0){//4
			int cnt = alphaCnt[(int)'U'-'A'];
			alphaCnt[(int)'F'-'A'] -= cnt;
			alphaCnt[(int)'O'-'A'] -= cnt;
			alphaCnt[(int)'U'-'A'] -= cnt;
			alphaCnt[(int)'R'-'A'] -= cnt;
			for(int i = 0 ; i < cnt ; i++) ans.push_back(4);
		}
		if(alphaCnt[(int)'W'-'A'] > 0){//2
			int cnt = alphaCnt[(int)'W'-'A'];
			alphaCnt[(int)'T'-'A'] -= cnt;
			alphaCnt[(int)'W'-'A'] -= cnt;
			alphaCnt[(int)'O'-'A'] -= cnt;
			for(int i = 0 ; i < cnt ; i++) ans.push_back(2);
		}
		if(alphaCnt[(int)'G'-'A'] > 0){//8
			int cnt = alphaCnt[(int)'G'-'A'];
			alphaCnt[(int)'E'-'A'] -= cnt;
			alphaCnt[(int)'I'-'A'] -= cnt;
			alphaCnt[(int)'G'-'A'] -= cnt;
			alphaCnt[(int)'H'-'A'] -= cnt;
			alphaCnt[(int)'T'-'A'] -= cnt;
			for(int i = 0 ; i < cnt ; i++) ans.push_back(8);
		}
		if(alphaCnt[(int)'H'-'A'] > 0){//3
			int cnt = alphaCnt[(int)'H'-'A'];
			alphaCnt[(int)'T'-'A'] -= cnt;
			alphaCnt[(int)'H'-'A'] -= cnt;
			alphaCnt[(int)'R'-'A'] -= cnt;
			alphaCnt[(int)'E'-'A'] -= cnt;
			alphaCnt[(int)'E'-'A'] -= cnt;
			for(int i = 0 ; i < cnt ; i++) ans.push_back(3);
		}
		if(alphaCnt[(int)'X'-'A'] > 0){//6
			int cnt = alphaCnt[(int)'X'-'A'];
			alphaCnt[(int)'S'-'A'] -= cnt;
			alphaCnt[(int)'I'-'A'] -= cnt;
			alphaCnt[(int)'X'-'A'] -= cnt;
			for(int i = 0 ; i < cnt ; i++) ans.push_back(6);
		}
		if(alphaCnt[(int)'O'-'A'] > 0){//1
			int cnt = alphaCnt[(int)'O'-'A'];
			alphaCnt[(int)'O'-'A'] -= cnt;
			alphaCnt[(int)'N'-'A'] -= cnt;
			alphaCnt[(int)'E'-'A'] -= cnt;
			for(int i = 0 ; i < cnt ; i++) ans.push_back(1);
		}
		if(alphaCnt[(int)'F'-'A'] > 0){//5
			int cnt = alphaCnt[(int)'F'-'A'];
			alphaCnt[(int)'F'-'A'] -= cnt;
			alphaCnt[(int)'I'-'A'] -= cnt;
			alphaCnt[(int)'V'-'A'] -= cnt;
			alphaCnt[(int)'E'-'A'] -= cnt;
			for(int i = 0 ; i < cnt ; i++) ans.push_back(5);
		}
		if(alphaCnt[(int)'I'-'A'] > 0){//9
			int cnt = alphaCnt[(int)'I'-'A'];
			alphaCnt[(int)'N'-'A'] -= cnt;
			alphaCnt[(int)'I'-'A'] -= cnt;
			alphaCnt[(int)'N'-'A'] -= cnt;
			alphaCnt[(int)'E'-'A'] -= cnt;
			for(int i = 0 ; i < cnt ; i++) ans.push_back(9);
		}
		if(alphaCnt[(int)'V'-'A'] > 0){//7
			int cnt = alphaCnt[(int)'V'-'A'];
			alphaCnt[(int)'S'-'A'] -= cnt;
			alphaCnt[(int)'E'-'A'] -= cnt;
			alphaCnt[(int)'V'-'A'] -= cnt;
			alphaCnt[(int)'E'-'A'] -= cnt;
			alphaCnt[(int)'N'-'A'] -= cnt;
			for(int i = 0 ; i < cnt ; i++) ans.push_back(7);
		}

		sort(ans.begin(),ans.end());
		int size = ans.size();
		printf("Case #%d: ",test_case);
		for(int i = 0 ; i < size ; i++) 	printf("%d",ans[i]);
		printf("\n");

		memset(alphaCnt,0,sizeof(alphaCnt));
	}

	return 0;
}
