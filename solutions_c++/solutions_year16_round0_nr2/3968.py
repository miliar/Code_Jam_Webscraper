//Author: net12k44
#include <bits/stdc++.h>
using namespace std;

void solve(){	
	string s; getline(cin, s);
	string cur = "";
	for(int i = 0; i < (int)s.length(); ++i)
		cur.push_back('+');
	
	map<string, int> d;
	queue<string> q;
	q.push(cur); d[cur] = 0;	
	while (!q.empty()){
		cur = q.front(); q.pop();
		for(int i = 1; i <= (int)cur.length(); ++i){
			string ss = cur;			
			reverse(ss.begin(), ss.begin()+i);
			for(int j = 0; j < i; ++j)
				ss[j] = ss[j]=='+' ? '-' : '+';
			if (!d.count(ss)){
				q.push(ss);
				d[ss] = d[cur]+1;				
			}
		}
	}
	printf("%d\n", d[s]);
}

int main(){
	freopen("file.out","w",stdout);
	int test; scanf("%d\n",&test);	
	for(int t = 1; t <= test; ++t){
		printf("Case #%d: ", t);
		solve();
	}
}