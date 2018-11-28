#include<iostream>
#include<cstdlib>
#include<cstdio>
#include<cmath>
#include<cstring>
#include<vector>
#include<set>
#include<unordered_set>
#include<algorithm>
using namespace std;

int n,k;
double ans = 0;
double a[20];

void check(vector<int> &record) {
	double f[20][20];
	memset(f,0,sizeof(f));
	f[0][0] = 1;
	for(int i=1;i<=k;i++) {
		double x = a[record[i-1]];
		f[i][0] = f[i-1][0] * (1-x);
		for(int j=1;j<=k/2;j++) {
			f[i][j] = f[i-1][j] * (1-x) + f[i-1][j-1] * x;
		}
	}
	ans = max(ans, f[k][k/2]);
}

void dfs(int last, vector<int> &record) {
	if (record.size() == k) {
		check(record);
		return;
	}
	for(int i=last+1;i<n;i++) {
		record.push_back(i);
		dfs(i, record);
		record.pop_back();
	}
}

void work() {
	scanf("%d%d",&n,&k);
	memset(a,0,sizeof(a));
	for(int i=0;i<n;i++) {
		scanf("%lf",&a[i]);
	}
	vector<int> record;
	ans = 0;
	dfs(-1, record);
	printf("%.8lf\n", ans);
}

int main() {
	// freopen("input.txt","r",stdin);
	freopen("B-small-attempt1.in","r",stdin);
	freopen("B-small-attempt1.out","w",stdout);
	int t;
	scanf("%d\n", &t);
	for(int i=0;i<t;i++) {
		printf("Case #%d: ", i+1);
		work();
	}

	return 0;
}

