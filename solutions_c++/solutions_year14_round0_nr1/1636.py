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

int b[5][5];

void add(int *a) {
	cin >> m;
	for (int i = 1; i <= 4; i ++)
		for (int j = 1; j <= 4; j ++) {
			cin >> b[i][j];
			if (i == m)
				a[b[i][j]] ++;
		}
}

int main() {
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);

	int cas = 1, id;
	for (cin >> id; id --; cas ++) {
		cout << "Case #" << cas << ": ";
		int total[40];
		memset(total, 0, sizeof total);
		add(total);
		add(total);
		int answer = 0, siz = 0;
		for (int i = 1; i < 17; i ++)
			if (total[i] == 2)
				answer = i, siz ++;
		if (siz == 1)
			cout << answer << endl;
		else 
		if (siz > 1)
			cout << "Bad magician!" << endl;
		else
			cout << "Volunteer cheated!" << endl;
	}

	//fclose(stdin); fclose(stdout);
}
