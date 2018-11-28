#include <cstdio>
#include <algorithm>
#include <vector>
#include <cstring>
#include <cmath>

using namespace std;

int t,n,r,p,s;
char ans[100005],temp[100005];
bool flag;

bool check(){
	int tr = 0;
	int tp = 0;
	int ts = 0;
	for(int k = 0; k < (1 << n); k++){
		temp[k] = ans[k];
		if(ans[k] == 'R')
		tr++;
		else if(ans[k] == 'S')
		ts++;
		else
		tp++;
	}
	if(tr != r || ts != s || tp != p)
	return 0;
	for(int k = n; k >= 1; k--){
		int ind = 0;
		for(int ii = 0; ii < (1 << k); ii += 2){
			if(temp[ii] == temp[ii + 1])
			return 0;
			if(temp[ii] > temp[ii + 1])
			swap(temp[ii], temp[ii + 1]);
			if(temp[ii] == 'P' && temp[ii + 1] == 'R')
			temp[ind] = 'P';
			else if(temp[ii] == 'P' && temp[ii + 1] == 'S')
			temp[ind] = 'S';
			else
			temp[ind] = 'R';
			ind++;
		}
	}
	return 1;
}

void solve(int lv){
	if(lv == (1 << n)){
		if(!flag){
			if(check()){
				for(int ii = 0; ii < (1 << n); ii++)
				printf("%c", ans[ii]);
				flag = 1;
			}
		}
		return;
	}
	ans[lv] = 'P';
	solve(lv + 1);
	ans[lv] = 'R';
	solve(lv + 1);
	ans[lv] = 'S';
	solve(lv + 1);
}

int main(){
	scanf("%d", &t);
	int testcase = 0;
	while(++testcase <= t){
		scanf("%d%d%d%d", &n, &r, &p, &s);
		flag = 0;
		printf("Case #%d: ", testcase);
		solve(0);
		if(!flag)
		printf("IMPOSSIBLE");
		printf("\n");
	}
}

