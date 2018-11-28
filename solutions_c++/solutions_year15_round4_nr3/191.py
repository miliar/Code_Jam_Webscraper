#include <iostream>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <set>
#include <cstdlib>
using namespace std;

int n; double  R, C;
double r[100], c[100];
const double eps = 1e-8;

set<string> A[205];

template<class T> inline T abs(T a)
{return a > 0 ? a : -a;}
template<class T> void checkmax(T &a, T b)
{if (b > a) a = b;}
template<class T> void checkmin(T &a, T b)
{if (b < a) a = b;}

void process(set<string> &A, string s) {
    A.clear();
    while (true) {
        int k = s.find(" ");
        if (k == -1) break;
        string a = s.substr(0, k);
        s = s.substr(k + 1);
       // cout << a << '!' << endl;
        A.insert(a);
    }
  //  cout << s << '!' << endl;
    if (s.size()) A.insert(s);
}

char reads[10000];



struct maxFlow {
	static const int N = 205;
	static const int M = 105005;
	int head[N];
	int dest[M], next[M];
	int h[N], vh[N];
	long long f[M];
	int tot, n;
	int S, T;
	void clear()
	{tot = 1; memset(head, 0, sizeof(head));}
	void add(int x, int y, long long z, bool flag = true)
	{
		dest[++tot] = y; f[tot] = z; next[tot] = head[x]; head[x] = tot;
		if (flag)
			add(y, x, 0, false);
	}
	long long sap(int x, long long y)
	{
		if (x == T)
			return y;
		int minh = n - 1;
		long long uy = y;
		for (int k = head[x]; k != 0; k = next[k]) if (f[k] > 0) {
			int u = dest[k];
			if (h[x] == h[u] + 1) {
				long long t = sap(u, min(y, f[k]));
				f[k] -= t; f[k ^ 1] += t; y -= t;
				if (y == 0) return uy;
				if (h[S] >= n) return uy - y;
			}
			checkmin(minh, h[u]);
		}
		if (uy == y) {
			if (--vh[h[x]] == 0) h[S] = n;
			h[x] = minh + 1;
			++vh[h[x]];
		}
		return uy - y;
	}
	long long run()
	{
		memset(h, 0, sizeof(h));
		memset(vh, 0, sizeof(vh));
		vh[0] = n;
		long long totflow = 0;
		while (h[S] < n)
			totflow += sap(S, (long long)1e18);
		return totflow;
	}
} F;

int count(int x, int y) {
    set<string>::iterator iter;
    int re = 0;
    for (iter = A[x].begin(); iter != A[x].end(); iter++)
        if (A[y].count(*iter) != 0)
            re++;
    return re;
}

int main() {
    freopen("C.in","r",stdin);
    //freopen("B-small.out","w",stdout);
    int T;
    cin >> T;

    for (int o = 1; o <= T; o++) {
        cin >> n;
        for (int i = 1; i <= n; i++) {
            scanf(" %[^\n]", reads);
            string s(reads);
           // cout << s << endl;
            process(A[i], s);
        }
        if (n == 2) {
            printf("Case #%d: %d\n",o,count(1,2));
            continue;
        }
        F.clear();
        F.S = 1; F.T = 2; F.n = n;
        for (int i = 3; i <= n; i++) {
            int p = count(1,i), q = count(2,i);
            F.add(1, i, p);
            F.add(i, 2, q);
        }
        for (int i = 3; i <= n; i++)
        for (int j = i + 1; j <= n; j++) {
            int k = count(i,j);
            F.add(i,j,k);
            F.add(j,i,k);
        }
        printf("Case #%d: %d\n",o,(int)F.run());
    }
}
