#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <string>
#include <set>
#include <map>

using namespace std;

map<string, int> Dic;

int n;
vector<int> vs;
vector<int> head;

int get_id(string ss) {
	if(Dic.count(ss) == 0) Dic[ss] = (int)Dic.size();
	return Dic[ss];
}

void input() {
	scanf("%d", &n);
	char buf[1024*16];
	gets(buf);
	Dic.clear();
	vs.clear(); head.clear();
	for(int i = 0;i < n;i ++) {
		gets(buf);
		//printf("%s\n", buf);
		int len = strlen(buf);
		head.push_back(vs.size());
		for(int j = 0;j < len;) {
			int k = j;
			while(buf[k] >= 'a'&&buf[k] <= 'z') ++ k;
			buf[k] = '\0';
			vs.push_back(get_id(string(buf+j)));
			j = k+1;
		}
	}
	head.push_back(vs.size());
}

void solve() {
	int ss = 0;
	int res = 100000;
	vector<int> inE(Dic.size());
	for(int i = 0;i < (int)inE.size();i ++) inE[i] = 0;

	vector<int> tt;

	for(int S = 0;S < (1<<(n-2));S ++) {
		//if(ss%10000 == 0) printf("%d\n", ss);
		++ ss;

		tt.clear();
		for(int i = 0;i < head[1];i ++) {
			inE[vs[i]] = 1;
			tt.push_back(vs[i]);
		}
		for(int j = 0;j < n-2;j ++) {
			if(S&(1<<j)) for(int k = head[j+2];k < head[j+3];k ++) {
				inE[vs[k]] = 1;
				tt.push_back(vs[k]);
			}
		}

		int rr = 0;

		for(int i = head[1];i < head[2];i ++) if(inE[vs[i]]) {
			inE[vs[i]] = 0;
			++ rr;
		}

		for(int j = 0;j < n-2;j ++) {
			if((S&(1<<j)) == 0) for(int k = head[j+2];k < head[j+3];k ++) if(inE[vs[k]]) {
				inE[vs[k]] = 0;
				++ rr;
			}
		}

		for(int i = 0;i < tt.size();i ++) inE[vs[i]] = 0;

		if(rr < res) {
			res = rr;

			//printf("***\n");
			//for(int ii = 0;ii < (int)E.size();ii ++) printf("%s ", E[ii].c_str());
			//printf("\n");
			//for(int ii = 0;ii < (int)F.size();ii ++) printf("%s ", F[ii].c_str());
			//printf("\n");
		}
	}

	printf("%d\n", res);
}

int main() {
	freopen("C-small-attempt1.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int Case;
	scanf("%d", &Case);
	for(int cas = 1;cas <= Case;cas ++) {
		input();
		printf("Case #%d: ", cas);
		solve();
	}
}