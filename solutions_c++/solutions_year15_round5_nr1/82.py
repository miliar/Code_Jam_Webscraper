#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<algorithm>
#include<cstring>
#include<cmath>
#include<ctime>
#include<map>
#include<string>
#include<vector>
#include<set>

using namespace std;
#define For(i,l,r) for (int i = l; i <= r; ++i)
#define Cor(i,l,r) for (int i = l; i >= r; --i)
#define Fill(a,b) memset(a,b,sizeof(a))
#define FI first
#define SE second
#define MP make_pair
#define PII pair<int,int>
#define flt double
#define INF (0x3f3f3f3f)
#define MaxN 10203040
#define MaxNode 1020304
#define MD 1000000007

long long getLL() {
	long long ret = 0;
	char c;
	while (1) {
		c = getchar();
		if (c >= '0' && c <= '9') break ;
	}
	while (1) {
		ret = ret * 10 + c - '0';
		c = getchar();
		if (c < '0' || c > '9') break ;
	}
	return ret;
}

int getInt() {
	int ret = 0;
	char c;
	while (1) {
		c = getchar();
		if (c >= '0' && c <= '9') break ;
	}
	while (1) {
		ret = ret * 10 + c - '0';
		c = getchar();
		if (c < '0' || c > '9') break ;
	}
	return ret;
}

int tree[MaxN * 2];
void ins(int x, int val) {
	for (int z = x; z <= 2000000; z += z & -z) tree[z] += val;
}

int ask(int r) {
	int ret = 0;
	for (int z = r; z; z -= z & -z) ret += tree[z];
	return ret;
}

int n, D, S0, As, Cs, Rs, M0, Am, Cm, Rm, father[MaxN], q[MaxN], A[MaxN];
vector<int> son[MaxN];
pair<int,int> inter[MaxN];
int main() {
	//freopen("A-small-attempt0.in","r",stdin); //freopen("output.txt","w",stdout);
	int T; cin >> T;
	For(TK,1,T) {
		printf("Case #%d: ", TK);
		scanf("%d%d", &n, &D);
		scanf("%d%d%d%d", &S0, &As, &Cs, &Rs);
		scanf("%d%d%d%d", &M0, &Am, &Cm, &Rm);
		For(i,1,n) {
			A[i] = S0;
			if (i > 1) father[i] = M0 % (i - 1) + 1; else father[i] = 0;
			S0 = ((long long)S0 * As + Cs) % Rs;
			M0 = ((long long)M0 * Am + Cm) % Rm;
		}
		For(i,1,n) son[i].clear();
		For(i,2,n) son[father[i]].push_back(i);
		int hd = 0, tl = 1; q[1] = 1;
		inter[1] = {A[1], A[1]};
		while (hd < tl) {
			int vex = q[++hd];
			for (auto &y : son[vex]) {
				inter[y] = {min(inter[vex].first, A[y]), max(inter[vex].second, A[y])};
				q[++tl] = y;
			}
		}
		Fill(tree, 0);
		sort(inter + 1, inter + n + 1);	
		For(i,1,n) ins(inter[i].second + 1, 1);
		int ans = 0;
		For(i,1,n) {
			ans = max(ans, ask(inter[i].first + D + 1));
			ins(inter[i].second + 1, -1);
		}
		cout << ans << endl;
	}
	return 0;
}

