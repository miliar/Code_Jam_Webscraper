#include <cstdio>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <ctime>
//#include <cmath>
#include <vector>
#include <map>
using namespace std;
typedef long long LL;
typedef pair<int,int> pint;
typedef pair<LL,LL> pll;
#define fi first
#define se second
typedef map<int,int> mapint;
typedef vector<int> vint;
typedef vector<vint> vintp;
#define rep(i,j,k) for (int i = (j);i <= (k);i ++)
#define repd(i,j,k) for (int i = (j);i >= (k);i --)
#define ran2 (rand() % 32000 * 32000 + rand() % 32000)
#define pb push_back
#define mp make_pair
#define SIZE(i) ((int)(i.size()))
int m,n,j,k,l,i,o,p,__t;
char ch;
void read(int &a) {
	for (ch = getchar();(ch < '0' || ch > '9') && (ch != '-');ch = getchar());
	if (ch == '-') a = 0,__t = -1; else a = ch - '0',__t = 1;
	for (ch = getchar();ch >= '0' && ch <= '9';ch = getchar()) a = a * 10 + ch - '0';
	a *= __t;
}

double a[1010], b[1010];
bool flag[1010];

int main() {
	freopen("d.in","r",stdin);
	freopen("d.out","w",stdout);

	int cas = 1, id;
	for (cin >> id; id --; cas ++) {
		cout << "Case #" << cas << ": ";
		cin >> m;
		rep(i, 1, m)
			cin >> a[i];
		rep(i, 1, m)
			cin >> b[i];
		sort(a + 1, a + 1 + m);
		sort(b + 1, b + 1 + m);
		int ret = 0;


		ret = 0;
		int k = 1;
		rep(i, 1, m) {
			for (; a[k] < b[i] && k <= m; k ++);
			if (k <= m) {
				k ++;
				ret ++;
			} else 
			break;
		}		
		cout << ret << ' ';
		ret = 0;
		k = 1;
		rep(i, 1, m) {
			for (; b[k] < a[i] && k <= m; k ++);
			if (k <= m) {
				k ++;
				ret ++;
			} else 
			break;
		}
		cout << m - ret << endl;
	}

	//fclose(stdin); fclose(stdout);
}
