#include <cstdio>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

vector< vector<string> > gao;

int T, cnt[3], ccc[3];
int N;

void g_init(){
	vector<string> tmp;
	tmp.push_back("P");
	tmp.push_back("R");
	tmp.push_back("S");
	gao.push_back(tmp);
	for(int i = 1; i < 13; ++i){
		tmp.clear();
		for(int j = 0; j < 3; ++j){
			string x = gao[i - 1][j];
			string y = gao[i - 1][(j + 1) % 3];
			tmp.push_back(min(x + y, y + x));
		}
		gao.push_back(tmp);
	}
}

int main(){
	g_init();
	/*for(int i = 12; i < 13; ++i){
		for(int j = 0; j < 3; ++j)
			printf("%s ", gao[i][j].c_str());
		puts("");
	}*/
	scanf("%d", &T);
	for(int xx = 1; xx <= T; ++xx){
		scanf("%d%d%d%d", &N, &cnt[1], &cnt[0], &cnt[2]);
		string ans = "";
		for(int i = 0; i < 3; ++i){
			// check
			string x = gao[N][i];
			for(int j = 0; j < 3; ++j)
				ccc[j] = cnt[j];
			bool ok = true;
			for(int j = 0; j < (1 << N); ++j){
				int dy;
				if(x[j] == 'P') dy = 0;
				else if(x[j] == 'R') dy = 1;
				else dy = 2;
				if(ccc[dy] == 0){
					ok = false;
					break;
				}
				ccc[dy]--;
			}
			if(ok){
				if(ans == "") ans = x;
				else ans = min(ans, x);
			}
		}
		printf("Case #%d: ", xx);
		if(ans == ""){
			puts("IMPOSSIBLE");
		} else {
			printf("%s\n", ans.c_str());
		}
	}
}
