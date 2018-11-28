#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<string>
#include<cstring>
#include<map>
#include<algorithm>
#include<vector>
#include<queue>
using namespace std;
typedef long long ll;
int dfs(string &s, int st, int ed, bool re) {
	int step = -1;
	if(re) {
		step = -step;
	}
	int ret = 0;
	for(int i=ed+step; i!=st+step; i+=step) {
		if(s[i] == '-') {
			int tmp1, tmp2=0xfff;
			for(int j=st; j!=i-step; j-=step) {
				s[j] = ('+'==s[j]? '-':'+');
			}
			tmp1 = dfs(s, st, i-step, re) + 1;
			//tmp2 = dfs(s, i, st+step, !re) + 1;
			//ret = min(tmp1, tmp2);
			ret = tmp1;
			for(int j=st; j!=i-step; j-=step) {
				s[j] = ('+'==s[j]? '-':'+');
			}
			break;
		}
	}
	return ret;
}
void deal() {
	string s;
	cin>>s;
	cout<<dfs(s, 0, s.length(), 0)<<endl;
}
void openFile() {
	freopen("B-large.out","w", stdout);
	freopen("B-large.in","r",stdin);
}
int main() {
	int t;
	openFile(); 
	cin>>t;
	for(int i=0;i<t;++i) {
		cout<<"Case #"<<i+1<<": ";
		deal();
	}
}