#include<bits/stdc++.h>
using namespace std;
typedef long long LL;
typedef pair<int, int> PII;

int N, R, P, S;
int valid[3];

string chu[3];
int result[300];
		
char win(char c){
	if (c == 'P') return 'R';
	if (c == 'R') return 'S';
	if (c == 'S') return 'P';
}
		
string dfs(char c, int stage){
	if (stage > N){
		return string("")+c;
	}
	string A = dfs(c, stage+1);
	string B = dfs(win(c), stage+1);
	result[win(c)]++;
	if (A < B)
		return A + B;
	else
		return B + A;
}

int main(){
	int times;
	scanf("%d", &times);
	for (int t = 1; t<=times; t++){
		scanf("%d %d %d %d", &N, &R, &P, &S);
		for (int i=0; i<=2; i++){
			// P < S < R < P
			// P R S
			result['R'] = 0;
			result['P'] = 0;
			result['S'] = 0;
			char root;
			if (i==0){
				root = 'P';
			}else if (i==1){
				root = 'S';
			}else if (i==2){
				root = 'R';
			}
			result[root]++;
			chu[i] = "";
			chu[i] = dfs(root, 1);
			valid[i] = result['P'] == P && result['R'] == R && result['S'] == S;
		}
		int index = -1;
		for (int j=0; j<=2; j++){
			if (valid[j]){
				if (index == -1 || chu[index] > chu[j]){
					index = j;
				}
			}
		}
		if (index != -1){
			printf("Case #%d: %s\n", t, chu[index].c_str());
		}else{
			printf("Case #%d: IMPOSSIBLE\n", t);
		}
	}
	return 0;
}
