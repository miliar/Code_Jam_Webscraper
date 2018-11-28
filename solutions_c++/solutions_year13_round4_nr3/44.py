#include<cstdio>
#include<iostream>
#include<cstring>
#include<algorithm>
#include<queue>
using namespace std;

const int N = 2005;

int n, a[N], b[N], ans[N], dpa[N], dpb[N], dgr[N];
bool g[N][N];

struct trs {
	int sum[2006];
	
	int lowbit(int i) {return i & (-i);}
	
	void clear() {
	  memset(sum, 0, sizeof(sum));
	}
	
	void insert(const int pos, const int val) {
		//cout << "insert" << ' ' << pos << ' ' << val << endl;
		int s = pos;
		while (s <= n) {
			sum[s] = max(sum[s], val);
		  s += lowbit(s);
		}
	}
	
	int ask(const int pos) {
		int s = pos, ret = 0;
		while (s) {
		  ret = max(ret, sum[s]);
		  s -= lowbit(s);
		}

		return ret;
	}
} tr;

int main() {
	
	freopen("C-Large.in", "r", stdin);
	freopen("C-L.out", "w", stdout);	
	
	int T;
	scanf("%d", &T);
	for (int V = 1; V <= T; ++V) {
	  scanf("%d", &n);
	  for (int i = 1; i <= n; ++i) scanf("%d", &a[i]);
	  for (int j = 1; j <= n; ++j) scanf("%d", &b[j]);
	  memset(ans, 0, sizeof(ans));
	  memset(dgr, 0, sizeof(dgr));
	  memset(g, 0, sizeof(g));
	  for (int i = 1; i <= n; ++i) {
	    for (int j = i + 1; j <= n; ++j) {
	      if (b[i] < b[j] + 1) {
	        g[i][j] = true;
	        ++dgr[j];
				}
	      if (a[i] > a[j] - 1) {
	        g[j][i] = true;
	        ++dgr[i];
				}
			}
		}
		int tag = 0;
		for (int i = 1; i <= n; ++i) {
			ans[i] = 1;
	    if (a[i] == b[i] && a[i] == 1) {
	      tag = i;
			}
		}
		for (int i = 1; i <= n; ++i) {
		  for (int j = 1; j <= n; ++j) {
				if (ans[j] == i && j != tag) ans[j] = i + 1;    
			}
			for (int j = 1; j <= n; ++j) {
			  if (g[tag][j]) --dgr[j];
			}
		  if (i < n) {
		  	//cout << i << "HAHAHAH" << endl;
				tr.clear();
				memset(dpa, 0, sizeof(dpa));
		  	for (int k = 1; k <= n; ++k) {
		  	  dpa[k] = 1;
		  	  dpa[k] = max(dpa[k], tr.ask(ans[k] - 1));
		  	  tr.insert(ans[k], dpa[k] + 1);
				}
		  	//cout << i << "HAHAHA" << endl;				
				tr.clear();
				memset(dpb, 0, sizeof(dpb));
		  	for (int k = n; k >= 1; --k) {
		  	  dpb[k] = 1;
		  	  dpb[k] = max(dpb[k], tr.ask(ans[k] - 1));
		  	  tr.insert(ans[k], dpb[k] + 1);
				}
				tag = 0;
				for (int k = 1; k <= n; ++k) {
				  if (ans[k] == i + 1 && dpa[k] == a[k] && dpb[k] == b[k] && dgr[k] == 0) {
				  	tag = k;
				  	break;
				  }
				}
				//cout << i << ' ' << tag << endl;
			}
		}
		printf("Case #%d:", V);
		for (int i = 1; i <= n; ++i) {
		  printf(" %d", ans[i]);
		}
		printf("\n");
	}
	return 0;
}

