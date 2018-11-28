#include <cstdio>
#include <ctime>
#include <algorithm>
#include <unordered_map>

using namespace std;

typedef unsigned long long ull;

const int MAXN = 30, MAXM = 10 + 2;

unordered_map<ull, int> e, f, g;

int n;
int len[MAXN];
ull a[MAXN][MAXM];

int ans;

char getstr(ull &ret){
	char c;
	while (!islower(c = getchar()));
	ret = 0;
	do{
		ret = ret * 27 + c - 'a' + 1;
	}while (islower(c = getchar()));
	return c;
}

inline void myDelete(unordered_map<ull, int> &a, ull x){
	if (a[x] == 1)
		a.erase(a.find(x));
	else
		--a[x];
}

void DFS(int d){
	if (d == n){
		int cnt = 0;
		for (unordered_map<ull, int>::iterator p = e.begin(); p != e.end(); ++p)
			cnt += f.find(p->first) != f.end();
		ans = min(ans, cnt);
		return;
	}

	for (int i=0;i<len[d];++i)
		++e[a[d][i]];
	DFS(d + 1);
	for (int i=0;i<len[d];++i)
		myDelete(e, a[d][i]);

	for (int i=0;i<len[d];++i)
		++f[a[d][i]];
	DFS(d + 1);
	for (int i=0;i<len[d];++i)
		myDelete(f, a[d][i]);
}

int main(){
	time_t start = clock();
	int cas;
	scanf("%d", &cas);
	for (int casi = 1; casi <= cas; ++casi){
		scanf("%d", &n);
		n -= 2;

		char c;
		ull temp;
		e.clear();
		do{
			c = getstr(temp);
			++e[temp];
		}while (c == ' ');
		f.clear();
		do{
			c = getstr(temp);
			++f[temp];
		}while (c == ' ');

		int ans0 = 0;
		g.clear();
		for (unordered_map<ull, int>::iterator p = e.begin(); p != e.end(); ++p)
			if (f.find(p->first) != f.end())
				g[p->first] = 1;
		for (unordered_map<ull, int>::iterator p = g.begin(); p != g.end(); ++p){
			++ans0;
			e.erase(p->first);
			f.erase(p->first);
		}

		for (int i=0;i<n;++i){
			len[i] = 0;
			do{
				c = getstr(a[i][len[i]]);
				len[i] += g.find(a[i][len[i]]) == g.end();
			}while (c == ' ');
		}

		ans = 1E6;
		DFS(0);
		printf("Case #%d: %d\n", casi, ans0 + ans);

		printf("timer = %d\n", clock() - start);
	}
	return 0;
}
