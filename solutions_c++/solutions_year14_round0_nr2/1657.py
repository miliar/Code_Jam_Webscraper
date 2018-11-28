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


int main() {
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);

	int cas = 1, id;
	for (cin >> id; id --; cas ++) {
		cout << "Case #" << cas << ": ";
		double C, F, X; // C = a house price F a house value X ending status
		cin >> C >> F >> X;
		double speed = 2.0;

		double tim = 0, ret = 0, answer = 1e100;

		for (int i = 0; ; i ++) {
			if ((X - ret) / speed + tim < answer)
				answer = (X - ret) / speed + tim;
			if (C / speed > F * X / (speed * (speed + F)))
				break;

			tim += C / (speed);
			//if (tim > answer)
				//break;
			speed += F;
		}
		printf("%.7lf\n", answer);
	}

	//fclose(stdin); fclose(stdout);
}
