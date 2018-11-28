#include <bits/stdc++.h>

using namespace std;

int M,N,ans,cnt;
string s[10];
vector<int> st[10];

void input(){
	scanf("%d%d", &M, &N);
	for (int i=0; i<M; i++){
		cin >> s[i];
		st[i].clear();
	}
}
int check(string a, string b){
	if (a.size() > b.size())
		swap(a,b);
	for (int i=0; i<(int)a.size(); i++){
		if (a[i] != b[i]){
			return i;
		}
	}
	return a.size();
}
void DFS(int cur){
	if (cur >= M){
		for (int i = 0; i<N; i++){
			if (st[i].size() == 0)
				return;
		}
		int tmp = N;
		for (int i=0; i<N; i++){
			vector<string> s2;
			for (int j=0; j<(int)st[i].size(); j++){
				s2.push_back(s[st[i][j]]);
				tmp += s2[j].size();
			}
			sort(s2.begin(),s2.end());
			for (int j=0; j<(int)s2.size()-1; j++){
				tmp -= check(s2[j],s2[j+1]);
			}
		}
		if (tmp == ans){
			cnt++;
		} else if (tmp > ans){
			ans = tmp;
			cnt = 1;
		}
		//cnt++;
		//ans = max(ans,tmp);

		return ;
	}
	for (int i=0; i<N; i++){
		st[i].push_back(cur);
		DFS(cur+1);
		st[i].pop_back();
	}
}
void solve(int nT){
	ans = -1;
	cnt = 0;
	DFS(0);
	printf("Case #%d: %d %d\n", nT, ans, cnt);
}
int main(){
	int nT;
	scanf("%d", &nT);
	for (int i=1; i<=nT; i++){
		input();
		solve(i);
	}
}