#include <bits/stdc++.h>
using namespace std;
#define ll long long
//string res[] = { "First", "Second" };
//const double pi = 3.1415926535897932384626433832795;
//int dx[] = {-1,0,1,0};
//int dy[] = {0,-1,0,1};

/*
 bool valid(int r,int c){
 return (r >= 0 && r < n && c >= 0 && c < m);
 }
 */

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	ios_base::sync_with_stdio(0) ;

	int T;
	cin >> T;
	for(int t=1;t <= T;++t) {
		string s;
		cin >> s;
		int n = 1,ans = 0,x = 2;
		for(int i=0;i<s.size()-1;++i)
			n += (s[i] != s[i+1]);

		if((s[0] == '-' && n%2 == 0) || s[0] == '+' && n%2 != 0)
			ans = n-1;
		else
			ans = n;

		printf("Case #%d: %d\n",t,ans);


	}

}
