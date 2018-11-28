#include <cstdio>
#include <algorithm>
#include <vector>
#include <cstring>
#include <cmath>

using namespace std;

const int INF = 1e9;
int t,n,i,j,ans,num[30];
char s[30][30];
bool used[30][30],o[30],rflag;
vector <int> order,dorder;

void exhaust(int id){
	if(id == n)
	return;
	bool ok = 0;
	int ppl = order[id];
	for(int k = 0; k < n; k++){
		if(!o[k]){
			if(s[ppl][k] == '1' || used[ppl][k]){
				ok = 1;
				o[k] = 1;
				exhaust(id + 1);
				o[k] = 0;
			}
		}
	}
	if(!ok)
	rflag = 0;
}

bool check(){
	order.clear();
	bool flag = 1;
	for(int ii = 0; ii < n; ii++)
	order.push_back(ii);
	do{
		rflag = 1;
		memset(o, 0, sizeof(o));
		exhaust(0);
		flag &= rflag;
	}while(next_permutation(order.begin(), order.end()));
	return flag;
}

void solve(int id, int p){
	if(id == n * n){
		if(check()){
			ans = min(ans, p);
		}
		return;
	}
	solve(id + 1, p);
	int x = id / n;
	int y = id % n;
	used[x][y] = 1;
	solve(id + 1, p + 1);
	used[x][y] = 0;
}

int main(){
	scanf("%d", &t);
	int testcase = 0;
	while(++testcase <= t){
		scanf("%d", &n);
		for(i = 0; i < n; i++)
		scanf("%s", s[i]);
		ans = INF;
		printf("Case #%d: ", testcase);
		solve(0, 0);
		printf("%d\n", ans);
	}
}

