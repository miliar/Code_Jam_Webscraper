#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<string>
#include<cstring>
#include<map>
#include<algorithm>
#include<vector>
#include<queue>
#include<cmath>
#include<deque>
#include<stack>
#include<ctime>
#include<bitset>
#include<set>
using namespace std;
typedef long long ll;
int cnt[30];
string nums[10] = {
	"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"
};
vector<char> ans;
void gao(){
	memset(cnt, 0, sizeof(cnt));
	ans.clear();
	string s;
	cin>>s;
	for(int i=0;i<s.length();++i) {
		++cnt[s[i]-'A'];
	}
	while(cnt[((int)'Z')-'A']) {
		ans.push_back('0');
		for(int i=0;i<nums[0].length();++i)
			--cnt[nums[0][i]-'A'];
	}
	while(cnt[((int)'W')-'A']) {
		ans.push_back('2');
		for(int i=0;i<nums[2].length();++i)
			--cnt[nums[2][i]-'A'];
	}
	while(cnt[((int)'X')-'A']) {
		ans.push_back('6');
		for(int i=0;i<nums[6].length();++i)
			--cnt[nums[6][i]-'A'];
	}
	while(cnt[((int)'G')-'A']) {
		ans.push_back('8');
		for(int i=0;i<nums[8].length();++i)
			--cnt[nums[8][i]-'A'];
	}
	while(cnt[((int)'T')-'A']) {
		ans.push_back('3');
		for(int i=0;i<nums[3].length();++i)
			--cnt[nums[3][i]-'A'];
	}
	while(cnt[((int)'S')-'A']) {
		ans.push_back('7');
		for(int i=0;i<nums[7].length();++i)
			--cnt[nums[7][i]-'A'];
	}
	while(cnt[((int)'R')-'A']) {
		ans.push_back('4');
		for(int i=0;i<nums[4].length();++i)
			--cnt[nums[4][i]-'A'];
	}
	while(cnt[((int)'O')-'A']) {
		ans.push_back('1');
		for(int i=0;i<nums[1].length();++i)
			--cnt[nums[1][i]-'A'];
	}
	while(cnt[((int)'F')-'A']) {
		ans.push_back('5');
		for(int i=0;i<nums[5].length();++i)
			--cnt[nums[5][i]-'A'];
	}
	while(cnt[((int)'I')-'A']) {
		ans.push_back('9');
		for(int i=0;i<nums[9].length();++i)
			--cnt[nums[9][i]-'A'];
	}
	sort(ans.begin(),ans.end());
	for(int i=0;i<ans.size();++i)
		printf("%c",ans[i]);
	printf("\n");
}
void usefile(string fn) {
	freopen((fn+".in").c_str(),"r",stdin);
	freopen((fn+".out").c_str(),"w",stdout);
} 
int main() {
	usefile("A-large"); 
	int t;
	scanf("%d",&t);
	for(int i=1;i<=t;++i) {
		printf("Case #%d: ", i);
		gao();
	}
	return 0;
}