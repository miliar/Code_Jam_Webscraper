//By Lin
#include<cstdio>
#include<cstring>
#include<iostream>
#include<algorithm>
#include<set>
#include<vector>
#include<map>
#include<queue>
#include<cctype>
#include<cmath>

#define eps 1e-9
#define sqr(x) ((x)*(x))
#define Rep(i,n) for(int i = 0; i<n; i++)
#define foreach(i,n) for( __typeof(n.begin()) i = n.begin(); i!=n.end(); i++)
#define X first
#define Y second
#define mp(x,y) make_pair(x,y)

using namespace std;
typedef long long LL;
typedef pair<int,int> pii;

#define N 100010

bool mark[10];

bool DoMark(int m) {
	for (;m; m /= 10) mark[m % 10] = true;
	Rep(i, 10) 
		if (mark[i] == false) return false;
	return true;
}

int		main(){
	int cas, n, tt = 0;
	scanf("%d", &cas);
	while (cas --) {
		scanf("%d", &n);
		printf("Case #%d: ", ++tt);
		if (n == 0) printf("INSOMNIA\n");
		else {
			int m = n;
			memset(mark, 0, sizeof mark);
			while (!DoMark(m)) m += n;
			printf("%d\n", m);
		}
	}
	return 0;
}
