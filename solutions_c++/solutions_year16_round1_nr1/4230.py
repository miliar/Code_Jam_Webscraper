#include<cstdio>
#include<iostream>
#include<vector>
#include<string>
#include<map>
#include<queue>
#include<stack>
#define maxn 1111
#define maxm 1111111
using namespace std;

int t;
string s, ans;
int main(){
	freopen("skj.in", "r", stdin);
	freopen("skj.out", "w", stdout);
	cin >> t;
	int cas = 1;
	while (t--){
		cin >> s;
		ans.clear();
		printf("Case #%d: ",cas++);
		ans.push_back(s[0]);
		int len = s.size();
		for (int i = 1; i<len;i++){
			if (s[i] < ans[0]) 
				ans.push_back(s[i]);
			//else ans.insert(0, s.substr(i,1));
			else ans = s[i] + ans;
		}
		len = ans.size();
		for (int i = 0; i<len; i++)
			printf("%c", ans[i]);
		printf("\n");
	}
	//system("pause");
}